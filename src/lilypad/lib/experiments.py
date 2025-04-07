"""Experimentation framework for evaluating and comparing functions."""

import csv
import asyncio
import inspect
import datetime
import concurrent.futures
from typing import Any, Generic, TypeVar, Protocol, TypeAlias, TypedDict, cast
from collections.abc import Callable, Sequence, Coroutine
from typing_extensions import Self, ParamSpec

from pydantic import BaseModel, ConfigDict
from rich.text import Text
from rich.table import Table
from rich.console import Console
from opentelemetry import trace
from mirascope.core.base import BaseCallResponse
from opentelemetry.trace import Span as OTSpan, Status, Tracer, StatusCode

from lilypad.lib.traces import Trace, AsyncTrace

P = ParamSpec("P")
R = TypeVar("R")


class MetricFn(Protocol[R]):
    """Protocol for a metric function comparing actual and ideal values."""

    def __call__(self, actual: R, ideal: R) -> bool | float | int:
        """
        Compares the actual output to the ideal output.

        Args:
            actual: The actual output from the function under test.
            ideal: The ideal/expected output for the test case.

        Returns:
            A boolean, float, or integer representing the metric score.
        """
        ...


class MetricFnWithArgs(Protocol[P, R]):
    """Protocol for a metric function that also accepts test case arguments."""

    def __call__(self, actual: R, ideal: R, *args: P.args, **kwargs: P.kwargs) -> bool | float | int:
        """
        Compares the actual output to the ideal output, using test case inputs.

        Args:
            actual: The actual output from the function under test.
            ideal: The ideal/expected output for the test case.
            *args: Positional arguments supplied to the function for this test case.
            **kwargs: Keyword arguments supplied to the function for this test case.

        Returns:
            A boolean, float, or integer representing the metric score.
        """
        ...


MetricFuncType: TypeAlias = MetricFn[R] | MetricFnWithArgs[P, R]

_SUMMARY_FORMAT_PERCENTAGE = "percentage"
_SUMMARY_FORMAT_FLOAT = "float"
_SUMMARY_FORMAT_NA = "na"
_SUMMARY_FORMAT_ERROR = "error"

_OTEL_TRACE_PROVIDER_NAME = "lilypad.experiment"


class ExperimentCase(BaseModel, Generic[P, R]):
    """Represents a single test case with inputs and expected output."""

    args: tuple
    kwargs: dict[str, Any]
    ideal: R
    model_config = ConfigDict(arbitrary_types_allowed=True)


class MetricInfo(TypedDict):
    """Stores information about a registered metric using TypedDict."""

    name: str
    metric_fn: MetricFuncType


class VersionResult(BaseModel, Generic[R]):
    """Stores the execution results for a specific function version on a single case."""

    version_name: str
    actual: R | None = None
    metric_results: dict[str, bool | float | int | str]
    error: Exception | None = None
    model_config = ConfigDict(arbitrary_types_allowed=True)


_MetricInfoEntry: TypeAlias = tuple[MetricInfo, bool]
_AllResults: TypeAlias = list[list[VersionResult[R]]]
_SummaryResultData: TypeAlias = dict[str, dict[str, tuple[float, str]]]


class Experiment(Generic[P, R]):
    """
    Manages and runs experiments to evaluate and compare function versions.

    Supports both synchronous and asynchronous functions via `run` and `arun`
    methods respectively. Handles result collection, metric evaluation,
    reporting (Rich tables), CSV export, and OpenTelemetry tracing.

    Generic Parameters:
        P: ParamSpec representing the parameters of the function under test.
        R: TypeVar representing the return type (or awaitable inner type) of the function.
    """

    def __init__(self, fn: Callable[P, R]) -> None:
        """
        Initializes an Experiment with the primary function to test.

        Args:
            fn: The primary function (sync or async) to be tested.
        """
        if not callable(fn):
            raise TypeError("The function provided must be callable.")
        self._target_fn: Callable[P, R] = fn
        self._is_target_async = inspect.iscoroutinefunction(fn)
        self._metrics: list[_MetricInfoEntry] = []
        self._cases: list[ExperimentCase[P, R]] = []
        self._console = Console()

    def _calculate_accepts_args(self, metric_fn: Callable[..., Any]) -> bool:
        """Determines if a metric function accepts extra args based on signature."""
        try:
            sig = inspect.signature(metric_fn)
            sig.bind("a", "i", *[], **{})
            hvp = any(p.kind == p.VAR_POSITIONAL for p in sig.parameters.values())
            hvk = any(p.kind == p.VAR_KEYWORD for p in sig.parameters.values())
            npk = sum(1 for p in sig.parameters.values() if p.kind in (p.POSITIONAL_OR_KEYWORD, p.POSITIONAL_ONLY))
            return hvp or hvk or npk > 2
        except TypeError:
            return False

    def metric(self, name: str) -> Callable[[MetricFn | MetricFnWithArgs], None]:
        """
        Returns a decorator to register a metric function for the experiment.

        Args:
            name: A unique display name for the metric.

        Returns:
            A decorator function that takes a metric function (MetricFn or
            MetricFnWithArgs) and registers it. The decorator itself returns None.

        Raises:
            ValueError: If the metric name is empty or already exists.
            TypeError: If the decorated object is not callable.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Metric name must be non-empty")

        def decorator(metric_fn: MetricFn | MetricFnWithArgs) -> None:
            if not callable(metric_fn):
                raise TypeError("Metric must be callable")
            if any(m["name"] == name for m, _ in self._metrics):
                raise ValueError(f"Metric '{name}' exists")
            accepts_args = self._calculate_accepts_args(metric_fn)
            metric_info: MetricInfo = {"name": name, "metric_fn": metric_fn}
            self._metrics.append((metric_info, accepts_args))

        return decorator

    def add_case(self, ideal: R, *args: P.args, **kwargs: P.kwargs) -> Self:
        """
        Adds a test case to the experiment.

        Args:
            ideal: The expected result (ideal output) for this test case.
            *args: Positional arguments to pass to the function under test.
            **kwargs: Keyword arguments to pass to the function under test.

        Returns:
            The Experiment instance itself, allowing for method chaining.
        """
        case = ExperimentCase[P, R](args=args, kwargs=kwargs, ideal=ideal)
        self._cases.append(case)
        return self

    def _get_function_name(self, func: Callable[P, R], index: int, all_funcs: Sequence[AnyCallable]) -> str:
        """
        Generates a unique, human-readable name for a function version (sync or async).

        Args:
            func: The function callable.
            index: The index of the function in the list of versions being run.
            all_funcs: The sequence of all functions being run in this experiment.

        Returns:
            A unique string name for the function version.
        """
        base_name = getattr(func, "__name__", f"func_{index}")
        duplicates = [i for i, f in enumerate(all_funcs) if getattr(f, "__name__", f"func_{i}") == base_name]
        if len(duplicates) > 1:
            try:
                name_index = duplicates.index(index)
                return f"{base_name} ({name_index + 1})"
            except ValueError:
                return f"{base_name}_{index}"
        return base_name

    def _extract_result(self, result: Any) -> Any:
        """Extracts the underlying result if wrapped in Trace or BaseCallResponse."""
        if isinstance(result, (AsyncTrace, Trace)):
            result = result.response
        if isinstance(result, BaseCallResponse):
            result = result.content
        return result

    def _sync_run_case_version(
        self, case: ExperimentCase[P, R], func_version: Callable[P, R], version_name: str
    ) -> VersionResult[R]:
        """Runs a single synchronous function version against a single test case."""
        actual_result: R | None = None
        run_error: Exception | None = None
        metric_outputs: dict[str, bool | float | int | str] = {}
        actual_unwrapped_result: R | None = None

        try:
            raw_result = func_version(*case.args, **case.kwargs)
            actual_unwrapped_result = self._extract_result(raw_result)
            for metric_info, accepts_args in self._metrics:
                try:
                    metric_fn = metric_info["metric_fn"]
                    metric_name = metric_info["name"]
                    if accepts_args:
                        mfn_args = cast(MetricFnWithArgs[P, R], metric_fn)
                        metric_outputs[metric_name] = mfn_args(
                            actual_unwrapped_result, case.ideal, *case.args, **case.kwargs
                        )
                    else:
                        mfn_simple = cast(MetricFn[R], metric_fn)
                        metric_outputs[metric_name] = mfn_simple(actual_unwrapped_result, case.ideal)
                except Exception as metric_error:
                    metric_outputs[metric_info["name"]] = f"[red]Error: {metric_error}[/red]"
        except Exception as e:
            run_error = e
            for metric_info, _ in self._metrics:
                metric_outputs[metric_info["name"]] = "[grey50]N/A (Func Err)[/grey50]"

        return VersionResult[R](
            version_name=version_name, actual=actual_unwrapped_result, metric_results=metric_outputs, error=run_error
        )

    def _sync_collect_all_results_with_tracing(
        self, versions_to_run: tuple[Callable[P, R], ...], tracer: Tracer, num_threads: int | None
    ) -> _AllResults:
        """Collects results synchronously, potentially using threads (implementation deferred)."""
        all_results: _AllResults = []
        if num_threads and num_threads > 1:
            self._console.print(
                f"[yellow]Warning: Parallel execution with num_threads={num_threads} is not yet implemented. Running sequentially.[/yellow]"
            )

        for i, case in enumerate(self._cases):
            case_results: list[VersionResult[R]] = []
            for j, func_version in enumerate(versions_to_run):
                version_name = self._get_function_name(func_version, j, versions_to_run)
                span_name = f"case_{i + 1}_{version_name}"
                with tracer.start_as_current_span(span_name) as exec_span:
                    exec_span.set_attribute("experiment.case.index", i + 1)
                    try:
                        exec_span.set_attribute("experiment.case.args", repr(case.args))
                        exec_span.set_attribute("experiment.case.kwargs", repr(case.kwargs))
                        exec_span.set_attribute("experiment.case.ideal", repr(case.ideal))
                    except Exception:
                        exec_span.set_attribute("experiment.case.inputs.error", "Serialization failed")
                    exec_span.set_attribute("experiment.version.name", version_name)

                    version_result = self._sync_run_case_version(case, func_version, version_name)

                    if version_result.error:
                        exec_span.set_status(Status(StatusCode.ERROR, str(version_result.error)))
                        exec_span.record_exception(version_result.error)
                        exec_span.set_attribute("experiment.result.actual", "N/A (Func Err)")
                    else:
                        exec_span.set_status(Status(StatusCode.OK))
                        try:
                            exec_span.set_attribute("experiment.result.actual", repr(version_result.actual))
                        except Exception:
                            exec_span.set_attribute("experiment.result.actual", "Serialization failed")

                    for metric_name, metric_value in version_result.metric_results.items():
                        attr_key = f"experiment.metric.{metric_name}"
                        if isinstance(metric_value, str) and metric_value.startswith("["):
                            clean = Text.from_markup(metric_value).plain
                            exec_span.set_attribute(attr_key, clean)
                        elif isinstance(metric_value, (str, bool, int, float)):
                            exec_span.set_attribute(attr_key, metric_value)
                        else:
                            exec_span.set_attribute(attr_key, str(metric_value))
                    case_results.append(version_result)
            all_results.append(case_results)
        return all_results

    async def _async_run_case_version(
        self, case: ExperimentCase[P, R], func_version: Callable[P, R], version_name: str
    ) -> VersionResult[R]:
        """Runs a single function version (sync or async) against a single test case."""
        actual_result: R | None = None
        run_error: Exception | None = None
        metric_outputs: dict[str, bool | float | int | str] = {}
        is_async_func = inspect.iscoroutinefunction(func_version)
        actual_unwrapped_result: R | None = None

        try:
            raw_result: Any
            if is_async_func:
                async_func = cast(Callable[P, Coroutine[Any, Any, Any]], func_version)
                raw_result = await async_func(*case.args, **case.kwargs)
            else:
                sync_func = cast(Callable[P, Any], func_version)
                raw_result = sync_func(*case.args, **case.kwargs)

            actual_unwrapped_result = self._extract_result(raw_result)

            for metric_info, accepts_args in self._metrics:
                try:
                    metric_fn = metric_info["metric_fn"]
                    metric_name = metric_info["name"]
                    if accepts_args:
                        mfn_args = cast(MetricFnWithArgs[P, R], metric_fn)
                        metric_outputs[metric_name] = mfn_args(
                            actual_unwrapped_result, case.ideal, *case.args, **case.kwargs
                        )
                    else:
                        mfn_simple = cast(MetricFn[R], metric_fn)
                        metric_outputs[metric_name] = mfn_simple(actual_unwrapped_result, case.ideal)
                except Exception as metric_error:
                    metric_outputs[metric_info["name"]] = f"[red]Error: {metric_error}[/red]"
        except Exception as e:
            run_error = e
            for metric_info, _ in self._metrics:
                metric_outputs[metric_info["name"]] = "[grey50]N/A (Func Err)[/grey50]"

        return VersionResult[R](
            version_name=version_name, actual=actual_unwrapped_result, metric_results=metric_outputs, error=run_error
        )

    async def _async_collect_all_results_with_tracing(
        self, versions_to_run: tuple[Callable[P, R], ...], tracer: Tracer
    ) -> _AllResults:
        """Collects results asynchronously (implementation deferred for gather)."""
        all_results: _AllResults = []
        for i, case in enumerate(self._cases):
            case_results: list[VersionResult[R]] = []
            for j, func_version in enumerate(versions_to_run):
                version_name = self._get_function_name(func_version, j, versions_to_run)
                span_name = f"case_{i + 1}_{version_name}"
                with tracer.start_as_current_span(span_name) as exec_span:
                    exec_span.set_attribute("experiment.case.index", i + 1)
                    try:
                        exec_span.set_attribute("experiment.case.args", repr(case.args))
                        exec_span.set_attribute("experiment.case.kwargs", repr(case.kwargs))
                        exec_span.set_attribute("experiment.case.ideal", repr(case.ideal))
                    except Exception:
                        exec_span.set_attribute("experiment.case.inputs.error", "Serialization failed")
                    exec_span.set_attribute("experiment.version.name", version_name)

                    version_result = await self._async_run_case_version(case, func_version, version_name)

                    if version_result.error:
                        exec_span.set_status(Status(StatusCode.ERROR, str(version_result.error)))
                        exec_span.record_exception(version_result.error)
                        exec_span.set_attribute("experiment.result.actual", "N/A (Func Err)")
                    else:
                        exec_span.set_status(Status(StatusCode.OK))
                        try:
                            exec_span.set_attribute("experiment.result.actual", repr(version_result.actual))
                        except Exception:
                            exec_span.set_attribute("experiment.result.actual", "Serialization failed")

                    for metric_name, metric_value in version_result.metric_results.items():
                        attr_key = f"experiment.metric.{metric_name}"
                        if isinstance(metric_value, str) and metric_value.startswith("["):
                            clean = Text.from_markup(metric_value).plain
                            exec_span.set_attribute(attr_key, clean)
                        elif isinstance(metric_value, (str, bool, int, float)):
                            exec_span.set_attribute(attr_key, metric_value)
                        else:
                            exec_span.set_attribute(attr_key, str(metric_value))
                    case_results.append(version_result)
            all_results.append(case_results)
        return all_results

    def _save_results_to_csv(self, all_results: _AllResults, csv_filename: str, metric_names: list[str]) -> None:
        """Saves the detailed experiment results to a CSV file."""
        try:
            self._console.print(f"[info]Saving detailed results to [bold]{csv_filename}[/bold]...[/info]")
            with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
                csv_writer: csv._writer = csv.writer(csvfile)
                header: list[str] = (
                    ["Case #", "Args", "Kwargs", "Ideal", "Version", "Actual"] + metric_names + ["Error"]
                )
                csv_writer.writerow(header)
                for case_idx, case_data in enumerate(self._cases):
                    for version_result in all_results[case_idx]:
                        metric_values_for_row: list[str] = []
                        for name in metric_names:
                            result = version_result.metric_results.get(name)
                            if isinstance(result, (bool, int, float)):
                                metric_values_for_row.append(str(result))
                            elif isinstance(result, str) and result.startswith(("[red]Error:", "[grey50]N/A")):
                                clean = Text.from_markup(result).plain
                                metric_values_for_row.append(clean)
                            else:
                                metric_values_for_row.append(str(result))
                        row_data: list[Any] = (
                            [
                                case_idx + 1,
                                repr(case_data.args),
                                repr(case_data.kwargs),
                                repr(case_data.ideal),
                                version_result.version_name,
                                repr(version_result.actual) if version_result.error is None else "N/A (Func Err)",
                            ]
                            + metric_values_for_row
                            + [str(version_result.error) if version_result.error else ""]
                        )
                        csv_writer.writerow(row_data)
            self._console.print(f"[info]Successfully saved results to [bold]{csv_filename}[/bold][/info]")
        except IOError as e:
            self._console.print(f"[bold red]Error saving results to CSV:[/bold red] {e}")
            raise e
        except Exception as e:
            self._console.print(f"[bold red]Unexpected error during CSV export:[/bold red] {e}")
            raise e

    def _calculate_summary(
        self, all_results: _AllResults, unique_version_names: list[str], metric_names: list[str]
    ) -> _SummaryResultData:
        """Calculates summary statistics for each metric per version."""
        summary_results: _SummaryResultData = {}
        if not all_results or not all_results[0]:
            return summary_results
        for version_name in unique_version_names:
            summary_results[version_name] = {}
            version_index = -1
            try:
                version_index = unique_version_names.index(version_name)
            except ValueError:
                continue
            for metric_name in metric_names:
                valid: list[bool | float | int] = []
                for case_idx in range(len(self._cases)):
                    if case_idx < len(all_results) and version_index < len(all_results[case_idx]):
                        vr = all_results[case_idx][version_index]
                        if vr.error is None:
                            mr = vr.metric_results.get(metric_name)
                            if isinstance(mr, (bool, int, float)):
                                valid.append(mr)
                if not valid:
                    summary_results[version_name][metric_name] = (0.0, _SUMMARY_FORMAT_NA)
                    continue
                first = valid[0]
                if isinstance(first, bool):
                    t_count = sum(1 for r in valid if r is True)
                    val = t_count / len(valid) if valid else 0.0
                    summary_results[version_name][metric_name] = (val, _SUMMARY_FORMAT_PERCENTAGE)
                elif isinstance(first, (int, float)):
                    numeric: list[float] = [float(r) for r in valid]
                    val = sum(numeric) / len(numeric) if numeric else 0.0
                    summary_results[version_name][metric_name] = (val, _SUMMARY_FORMAT_FLOAT)
                else:
                    summary_results[version_name][metric_name] = (0.0, _SUMMARY_FORMAT_ERROR)
        return summary_results

    def _display_summary(self, summary_results: _SummaryResultData, metric_names: list[str]) -> None:
        """Displays the calculated summary statistics in a Rich table."""
        summary_table = Table(
            title="[bold cyan]Experiment Summary[/bold cyan]",
            show_header=True,
            header_style="bold magenta",
            expand=True,
        )
        summary_table.add_column("Version", style="dim", min_width=15)
        for name in metric_names:
            summary_table.add_column(name, justify="center", min_width=10)
        for version_name, metric_summaries in summary_results.items():
            row_data: list[str] = [version_name]
            for metric_name in metric_names:
                summary_data = metric_summaries.get(metric_name)
                display = "[grey50]N/A[/grey50]"
                if summary_data:
                    val, fmt = summary_data
                    if fmt == _SUMMARY_FORMAT_PERCENTAGE:
                        display = f"{val:.1%}"
                    elif fmt == _SUMMARY_FORMAT_FLOAT:
                        display = f"{val:.4f}"
                    elif fmt == _SUMMARY_FORMAT_NA:
                        display = "[grey50]N/A[/grey50]"
                    elif fmt == _SUMMARY_FORMAT_ERROR:
                        display = "[bold red]Error[/bold red]"
                    else:
                        display = str(val)
                row_data.append(display)
            summary_table.add_row(*row_data)
        self._console.print(summary_table)

    def _display_details(self, all_results: _AllResults, metric_names: list[str]) -> None:
        """Displays the detailed results for all cases and versions in a single table."""
        if not self._cases:
            return

        self._console.print(f"[bold cyan]Detailed Results ({len(self._cases)} cases):[/bold cyan]")
        detail_table = Table(
            title="Detailed Experiment Results",
            show_header=True,
            header_style="bold magenta",
            expand=True,
            show_lines=True,
        )
        detail_table.add_column("Case #", style="dim", justify="right", no_wrap=True)
        detail_table.add_column("Inputs", style="yellow", overflow="fold", min_width=30, ratio=2)
        detail_table.add_column("Ideal", style="green", overflow="fold", min_width=15, ratio=1)
        detail_table.add_column("Version", style="dim", min_width=15)
        detail_table.add_column("Actual Output", style="cyan", overflow="fold", min_width=20, ratio=2)
        if self._metrics:
            for name in metric_names:
                detail_table.add_column(name, justify="center", min_width=10)
        detail_table.add_column("Error", style="red", overflow="fold", min_width=15, ratio=1)

        for i, case in enumerate(self._cases):
            case_num_str = str(i + 1)
            inputs_repr = f"Args: {case.args!r}\nKwargs: {case.kwargs!r}"
            ideal_repr = repr(case.ideal)
            if i < len(all_results):
                case_run_results = all_results[i]
                for version_result in case_run_results:
                    row_data: list[str] = [case_num_str, inputs_repr, ideal_repr, version_result.version_name]
                    if version_result.error:
                        row_data.append("[grey50]N/A (Func Err)[/grey50]")
                        if self._metrics:
                            row_data.extend(["[grey50]N/A[/grey50]"] * len(metric_names))
                        row_data.append(str(version_result.error))
                    else:
                        row_data.append(repr(version_result.actual))
                        if self._metrics:
                            for name in metric_names:
                                result = version_result.metric_results.get(name, "[grey50]Missing[/grey50]")
                                if isinstance(result, bool):
                                    row_data.append(
                                        "[green][bold]True[/bold][/green]"
                                        if result
                                        else "[red][bold]False[/bold][/red]"
                                    )
                                elif isinstance(result, (int, float)):
                                    row_data.append(f"{result:.4f}" if isinstance(result, float) else str(result))
                                else:
                                    row_data.append(str(result))
                        row_data.append("")
                    detail_table.add_row(*row_data)
            else:
                detail_table.add_row(
                    case_num_str,
                    inputs_repr,
                    ideal_repr,
                    "[grey50]No results[/grey50]",
                    "",
                    *[""] * len(metric_names),
                    "",
                )
        self._console.print(detail_table)

    def run(self, *versions: Callable[P, R], num_threads: int | None = None) -> None:
        """
        Runs the experiment synchronously for all registered cases and metrics.

        This method assumes the target function and all provided versions are
        synchronous. If an asynchronous function is detected, it raises a TypeError.
        Results are collected sequentially, saved to CSV, and displayed.

        Args:
            *versions: Additional synchronous function versions to test.
            num_threads: If provided and > 1, currently issues a warning as
                         parallel execution is not yet implemented.

        Raises:
            TypeError: If the target function or any provided version is async.
        """
        if self._is_target_async:
            raise TypeError("Target function is async. Use arun() instead.")
        async_versions = [v for v in versions if inspect.iscoroutinefunction(v)]
        if async_versions:
            raise TypeError(
                f"Sync run() called with async versions: {[getattr(v, '__name__', '...') for v in async_versions]}. Use arun()."
            )

        if not self._cases:
            self._console.print("[yellow]Warning: No test cases added. Nothing to run.[/yellow]")
            return

        tracer: Tracer = trace.get_tracer(_OTEL_TRACE_PROVIDER_NAME)
        sync_versions_to_run = cast(tuple[Callable[P, R], ...], (self._target_fn,) + versions)

        with tracer.start_as_current_span("Experiment.run[sync]") as run_span:
            timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            csv_filename: str = f"run_{timestamp}.csv"
            num_versions: int = len(sync_versions_to_run)
            metric_names: list[str] = [m["name"] for m, _ in self._metrics]
            unique_version_names: list[str] = [
                self._get_function_name(f, i, sync_versions_to_run) for i, f in enumerate(sync_versions_to_run)
            ]

            run_span.set_attribute("experiment.execution_mode", "sync")
            run_span.set_attribute("experiment.num_cases", len(self._cases))
            run_span.set_attribute("experiment.num_versions", num_versions)
            run_span.set_attribute("experiment.metric_names", metric_names)
            run_span.set_attribute("experiment.version_names", unique_version_names)
            if num_threads:
                run_span.set_attribute("experiment.requested_threads", num_threads)

            self._console.print(
                f"\n[bold cyan]Running Experiment (Sync) ({len(self._cases)} cases, {num_versions} versions)...[/bold cyan]"
            )

            all_results = self._sync_collect_all_results_with_tracing(sync_versions_to_run, tracer, num_threads)

            try:
                self._save_results_to_csv(all_results, csv_filename, metric_names)
                run_span.set_attribute("experiment.csv_output_file", csv_filename)
            except Exception as e:
                run_span.record_exception(e)
                run_span.set_status(Status(StatusCode.ERROR, f"CSV saving failed: {e}"))

            if self._metrics:
                try:
                    summary_data = self._calculate_summary(all_results, unique_version_names, metric_names)
                    self._display_summary(summary_data, metric_names)
                    self._console.print("-" * 80)
                except Exception as e:
                    self._console.print(f"[bold red]Error during summary display:[/bold red] {e}")
                    run_span.record_exception(e)
            else:
                self._console.print("[yellow]Warning: No metrics added. Skipping summary.[/yellow]")

            try:
                self._display_details(all_results, metric_names)
            except Exception as e:
                self._console.print(f"[bold red]Error during detailed results display:[/bold red] {e}")
                run_span.record_exception(e)

    async def arun(self, *versions: Callable[P, Coroutine[Any, Any, R]]) -> None:
        """
        Runs the experiment asynchronously for all registered cases and metrics.

        This method assumes the target function and all provided versions are
        asynchronous. If a synchronous function is detected, it raises a TypeError.
        Results are collected (currently sequentially using await), saved to CSV,
        and displayed in the console.

        Args:
            *versions: Additional asynchronous function versions to test.

        Raises:
            TypeError: If the target function or any provided version is sync.
        """
        if not self._is_target_async:
            raise TypeError("Target function is sync. Use run() instead.")
        sync_versions = [v for v in versions if not inspect.iscoroutinefunction(v)]
        if sync_versions:
            raise TypeError(
                f"Async arun() called with sync versions: {[getattr(v, '__name__', '...') for v in sync_versions]}. Use run()."
            )

        if not self._cases:
            self._console.print("[yellow]Warning: No test cases added. Nothing to run.[/yellow]")
            return

        tracer: Tracer = trace.get_tracer(_OTEL_TRACE_PROVIDER_NAME)
        async_versions_to_run = cast(tuple[Callable[P, R], ...], (self._target_fn,) + versions)

        with tracer.start_as_current_span("Experiment.run[async]") as run_span:
            timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            csv_filename: str = f"run_{timestamp}.csv"
            num_versions: int = len(async_versions_to_run)
            metric_names: list[str] = [m["name"] for m, _ in self._metrics]
            unique_version_names: list[str] = [
                self._get_function_name(f, i, async_versions_to_run) for i, f in enumerate(async_versions_to_run)
            ]

            run_span.set_attribute("experiment.execution_mode", "async")
            run_span.set_attribute("experiment.num_cases", len(self._cases))
            run_span.set_attribute("experiment.num_versions", num_versions)
            run_span.set_attribute("experiment.metric_names", metric_names)
            run_span.set_attribute("experiment.version_names", unique_version_names)

            self._console.print(
                f"\n[bold cyan]Running Experiment (Async) ({len(self._cases)} cases, {num_versions} versions)...[/bold cyan]"
            )

            all_results = await self._async_collect_all_results_with_tracing(async_versions_to_run, tracer)

            try:
                self._save_results_to_csv(all_results, csv_filename, metric_names)
                run_span.set_attribute("experiment.csv_output_file", csv_filename)
            except Exception as e:
                run_span.record_exception(e)
                run_span.set_status(Status(StatusCode.ERROR, f"CSV saving failed: {e}"))

            if self._metrics:
                try:
                    summary_data = self._calculate_summary(all_results, unique_version_names, metric_names)
                    self._display_summary(summary_data, metric_names)
                    self._console.print("-" * 80)
                except Exception as e:
                    self._console.print(f"[bold red]Error during summary display:[/bold red] {e}")
                    run_span.record_exception(e)
            else:
                self._console.print("[yellow]Warning: No metrics added. Skipping summary.[/yellow]")

            try:
                self._display_details(all_results, metric_names)
            except Exception as e:
                self._console.print(f"[bold red]Error during detailed results display:[/bold red] {e}")
                run_span.record_exception(e)
