# src/lilypad/lib/experiments.py
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
R = TypeVar("R")  # Represents the UNWRAPPED result type expected by metrics/ideal

AnyCallable: TypeAlias = Callable[..., Any | Coroutine[Any, Any, Any]]


class MetricFn(Protocol[R]):
    """Protocol for a metric function comparing actual and ideal values."""

    def __call__(self, actual: R, ideal: R) -> bool | float | int:
        """
        Compares the actual (unwrapped) output to the ideal output.

        Args:
            actual: The actual, potentially unwrapped output from the function.
            ideal: The ideal/expected output for the test case.

        Returns:
            A boolean, float, or integer representing the metric score.
        """
        ...


class MetricFnWithArgs(Protocol[R, P]):
    """Protocol for a metric function that also accepts test case arguments."""

    def __call__(self, actual: R, ideal: R, *args: P.args, **kwargs: P.kwargs) -> bool | int | float:
        """
        Compares the actual (unwrapped) output to the ideal output, using inputs.

        Args:
            actual: The actual, potentially unwrapped output from the function.
            ideal: The ideal/expected output for the test case.
            *args: Positional arguments supplied to the function for this test case.
            **kwargs: Keyword arguments supplied to the function for this test case.

        Returns:
            A boolean, float, or integer representing the metric score.
        """
        ...


MetricFuncType: TypeAlias = MetricFn[R] | MetricFnWithArgs[R, P]

_SUMMARY_FORMAT_PERCENTAGE = "percentage"
_SUMMARY_FORMAT_FLOAT = "float"
_SUMMARY_FORMAT_NA = "na"
_SUMMARY_FORMAT_ERROR = "error"

_OTEL_TRACE_PROVIDER_NAME = "lilypad.experiment"


class ExperimentCase(BaseModel, Generic[P, R]):
    """Represents a single test case with inputs and expected output."""

    args: tuple
    kwargs: dict[str, Any]
    ideal: R  # Ideal output (expected type R)
    model_config = ConfigDict(arbitrary_types_allowed=True)


class MetricInfo(TypedDict):
    """Stores information about a registered metric using TypedDict."""

    name: str
    metric_fn: MetricFuncType[R, P]  # Uses R and P


class VersionResult(BaseModel, Generic[R]):
    """Stores the execution results for a specific function version on a single case."""

    case_index: int
    version_index: int
    version_name: str
    actual_raw: Any | None = None  # Store the raw return value
    actual_unwrapped: R | None = None  # Store the unwrapped value (type R)
    metric_results: dict[str, bool | float | int | str]
    error: Exception | None = None
    model_config = ConfigDict(arbitrary_types_allowed=True)


_MetricInfoEntry: TypeAlias = tuple[MetricInfo, bool]  # MetricInfo and accepts_args flag
_AllResults: TypeAlias = list[list[VersionResult[R] | None]]
_SummaryResultData: TypeAlias = dict[str, dict[str, tuple[float, str]]]


class Experiment(Generic[P, R]):
    """
    Manages and runs experiments to evaluate and compare function versions.

    Supports both synchronous and asynchronous functions via `run` and `arun`
    methods respectively. Handles result collection (sequentially or in parallel),
    metric evaluation against the unwrapped function result, reporting (Rich tables),
    CSV export, and OpenTelemetry tracing.

    Generic Parameters:
        P: ParamSpec representing the parameters of the function under test.
        R: TypeVar representing the **unwrapped** return type expected by metrics
           and the `ideal` value in test cases.
    """

    def __init__(self, fn: Callable[P, Any | Coroutine[Any, Any, Any]]) -> None:
        """
        Initializes an Experiment with the primary function to test.

        Args:
            fn: The primary function (sync or async) to be tested. Its raw return
                value will be processed by `_extract_result` before metric evaluation.
        """
        if not callable(fn):
            raise TypeError("The function provided must be callable.")
        self._target_fn: AnyCallable = fn
        self._is_target_async = inspect.iscoroutinefunction(fn)
        self._metrics: list[_MetricInfoEntry] = []
        self._cases: list[ExperimentCase[P, R]] = []
        self._console = Console()
        self._tracer: Tracer = trace.get_tracer(_OTEL_TRACE_PROVIDER_NAME)
        try:
            self._target_signature = inspect.signature(self._target_fn)
        except ValueError:  # Handle cases where signature cannot be retrieved (e.g., builtins)
            self._target_signature = None

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

    def metric(self, name: str) -> Callable[[MetricFuncType[R, P]], None]:
        """
        Returns a decorator to register a metric function for the experiment.

        The metric function will receive the **unwrapped** result of the function
        execution as its `actual` argument.

        Args:
            name: A unique display name for the metric.

        Returns:
            A decorator function that takes a metric function and registers it.

        Raises:
            ValueError: If the metric name is empty or already exists.
            TypeError: If the decorated object is not callable.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Metric name must be non-empty")

        def decorator(metric_fn: MetricFuncType[R, P]) -> None:
            if not callable(metric_fn):
                raise TypeError("Metric must be callable")
            if any(m["name"] == name for m, _ in self._metrics):
                raise ValueError(f"Metric '{name}' exists")
            accepts_args = self._calculate_accepts_args(metric_fn)
            # Cast metric_fn to satisfy MetricInfo type definition
            metric_info: MetricInfo = {"name": name, "metric_fn": cast(MetricFuncType, metric_fn)}
            self._metrics.append((metric_info, accepts_args))

        return decorator

    def add_case(self, ideal: R, *args: P.args, **kwargs: P.kwargs) -> Self:
        """
        Adds a test case to the experiment.

        Args:
            ideal: The expected result (ideal output) for this test case. Should
                   match the **unwrapped** return type R.
            *args: Positional arguments to pass to the function under test.
            **kwargs: Keyword arguments to pass to the function under test.

        Returns:
            The Experiment instance itself, allowing for method chaining.
        """
        case = ExperimentCase[P, R](args=args, kwargs=kwargs, ideal=ideal)
        self._cases.append(case)
        return self

    def _get_function_name(self, func: AnyCallable, index: int, all_funcs: Sequence[AnyCallable]) -> str:
        """
        Generates a unique, human-readable name for a function version.
        Uses `version_number` attribute if available, otherwise handles duplicates.
        """
        base_name = getattr(func, "__name__", f"func_{index}")
        # Attempt to get version number if attached by @trace decorator
        if version_number := getattr(func, "version_number", None):
            return f"{base_name}_v{version_number}"

        # Fallback duplicate handling based on position in list
        duplicates = [i for i, f in enumerate(all_funcs) if getattr(f, "__name__", f"func_{i}") == base_name]
        if len(duplicates) > 1:
            # Use index suffix if version number not found and duplicates exist
            return f"{base_name}_{index}"

        return base_name  # Return base name if no collision or version number

    def _extract_result(self, result: Any) -> Any:
        """Extracts the underlying result if wrapped in Trace."""
        if isinstance(result, (AsyncTrace, Trace)):
            result = result.response
        return result

    def _calculate_metrics(
        self, actual_unwrapped: R | None, case: ExperimentCase[P, R]
    ) -> dict[str, bool | float | int | str]:
        """Calculates all registered metrics against the unwrapped actual result."""
        metric_outputs: dict[str, bool | float | int | str] = {}
        if actual_unwrapped is None:
            for metric_info, _ in self._metrics:
                metric_outputs[metric_info["name"]] = "[grey50]N/A (Func Err)[/grey50]"
            return metric_outputs

        for metric_info, accepts_args in self._metrics:
            metric_name = metric_info["name"]
            try:
                metric_fn = metric_info["metric_fn"]
                if accepts_args:
                    mfn_args = cast(MetricFnWithArgs[R, P], metric_fn)
                    # Pass unwrapped result to metric
                    metric_outputs[metric_name] = mfn_args(actual_unwrapped, case.ideal, *case.args, **case.kwargs)
                else:
                    mfn_simple = cast(MetricFn[R], metric_fn)
                    # Pass unwrapped result to metric
                    metric_outputs[metric_name] = mfn_simple(actual_unwrapped, case.ideal)
            except Exception as metric_error:
                metric_outputs[metric_name] = f"[red]Error: {metric_error}[/red]"
        return metric_outputs

    def _set_span_attributes_from_result(self, span: OTSpan, version_result: VersionResult[R]) -> None:
        """Sets OpenTelemetry span attributes based on the VersionResult."""
        if version_result.error:
            span.set_status(Status(StatusCode.ERROR, str(version_result.error)))
            span.record_exception(version_result.error)
            span.set_attribute("experiment.result.actual_raw", "N/A (Func Err)")
            span.set_attribute("experiment.result.actual_unwrapped", "N/A (Func Err)")
        else:
            span.set_status(Status(StatusCode.OK))
            try:
                # Store both raw and unwrapped representations if possible
                span.set_attribute("experiment.result.actual_raw", repr(version_result.actual_raw))
                span.set_attribute("experiment.result.actual_unwrapped", repr(version_result.actual_unwrapped))
            except Exception:
                span.set_attribute("experiment.result.actual_raw", "Serialization failed")
                span.set_attribute("experiment.result.actual_unwrapped", "Serialization failed")

        for metric_name, metric_value in version_result.metric_results.items():
            attr_key = f"experiment.metric.{metric_name}"
            if isinstance(metric_value, str) and metric_value.startswith("["):
                clean = Text.from_markup(metric_value).plain
                span.set_attribute(attr_key, clean)
            elif isinstance(metric_value, (str, bool, int, float)):
                span.set_attribute(attr_key, metric_value)
            else:
                span.set_attribute(attr_key, str(metric_value))

    def _format_inputs(self, case: ExperimentCase[P, R]) -> str:
        """Formats case inputs into a string representation."""
        if not self._target_signature:
            # Fallback if signature retrieval failed
            return f"Args: {case.args!r}, Kwargs: {case.kwargs!r}"
        try:
            bound_args = self._target_signature.bind_partial(*case.args, **case.kwargs)
            bound_args.apply_defaults()
            parts = []
            for name, value in bound_args.arguments.items():
                parts.append(f"{name}={repr(value)}")
            return ", ".join(parts)
        except TypeError:
            # Fallback if binding fails
            return f"Args: {case.args!r}, Kwargs: {case.kwargs!r}"

    def _execute_and_trace_sync(
        self,
        case_idx: int,
        case: ExperimentCase[P, R],
        func_version: Callable[P, R],
        version_name: str,
        version_idx: int,
    ) -> VersionResult[R]:
        """Executes a sync function, calculates metrics, traces, and returns results."""
        span_name = f"case_{case_idx + 1}_{version_name}"
        with self._tracer.start_as_current_span(span_name) as exec_span:
            exec_span.set_attribute("experiment.case.index", case_idx + 1)
            try:
                exec_span.set_attribute("experiment.case.inputs", self._format_inputs(case))
                exec_span.set_attribute("experiment.case.ideal", repr(case.ideal))
            except Exception:
                exec_span.set_attribute("experiment.case.inputs.error", "Serialization failed")
            exec_span.set_attribute("experiment.version.name", version_name)
            exec_span.set_attribute("experiment.version.index", version_idx)

            run_error: Exception | None = None
            actual_raw_result: Any | None = None
            actual_unwrapped_result: R | None = None
            metric_outputs: dict[str, bool | float | int | str] = {}

            try:
                raw_result = func_version(*case.args, **case.kwargs)
                actual_raw_result = raw_result  # Store raw result
                actual_unwrapped_result = self._extract_result(raw_result)
                metric_outputs = self._calculate_metrics(actual_unwrapped_result, case)
            except Exception as e:
                run_error = e
                metric_outputs = self._calculate_metrics(None, case)

            version_result = VersionResult[R](
                case_index=case_idx,
                version_index=version_idx,
                version_name=version_name,
                actual_raw=actual_raw_result,
                actual_unwrapped=actual_unwrapped_result,
                metric_results=metric_outputs,
                error=run_error,
            )
            self._set_span_attributes_from_result(exec_span, version_result)
            return version_result

    async def _execute_and_trace_async(
        self, case_idx: int, case: ExperimentCase[P, R], func_version: AnyCallable, version_name: str, version_idx: int
    ) -> VersionResult[R]:
        """Executes a sync or async function, calculates metrics, traces, and returns results."""
        span_name = f"case_{case_idx + 1}_{version_name}"
        with self._tracer.start_as_current_span(span_name) as exec_span:
            exec_span.set_attribute("experiment.case.index", case_idx + 1)
            try:
                exec_span.set_attribute("experiment.case.inputs", self._format_inputs(case))
                exec_span.set_attribute("experiment.case.ideal", repr(case.ideal))
            except Exception:
                exec_span.set_attribute("experiment.case.inputs.error", "Serialization failed")
            exec_span.set_attribute("experiment.version.name", version_name)
            exec_span.set_attribute("experiment.version.index", version_idx)

            run_error: Exception | None = None
            actual_raw_result: Any | None = None
            actual_unwrapped_result: R | None = None
            metric_outputs: dict[str, bool | float | int | str] = {}

            try:
                raw_result: Any
                if inspect.iscoroutinefunction(func_version):
                    async_callable = cast(Callable[P, Coroutine[Any, Any, Any]], func_version)
                    raw_result = await async_callable(*case.args, **case.kwargs)
                else:
                    sync_callable = cast(Callable[P, Any], func_version)
                    raw_result = await asyncio.to_thread(sync_callable, *case.args, **case.kwargs)

                actual_raw_result = raw_result  # Store raw result
                actual_unwrapped_result = self._extract_result(raw_result)
                metric_outputs = self._calculate_metrics(actual_unwrapped_result, case)
            except Exception as e:
                run_error = e
                metric_outputs = self._calculate_metrics(None, case)

            version_result = VersionResult[R](
                case_index=case_idx,
                version_index=version_idx,
                version_name=version_name,
                actual_raw=actual_raw_result,
                actual_unwrapped=actual_unwrapped_result,
                metric_results=metric_outputs,
                error=run_error,
            )
            self._set_span_attributes_from_result(exec_span, version_result)
            return version_result

    def _collect_sequential(self, versions_to_run: tuple[Callable[P, R], ...]) -> _AllResults:
        """Collects results sequentially for synchronous execution."""
        all_results: _AllResults = [[None for _ in versions_to_run] for _ in self._cases]
        for i, case in enumerate(self._cases):
            for j, func_version in enumerate(versions_to_run):
                version_name = self._get_function_name(func_version, j, versions_to_run)
                result = self._execute_and_trace_sync(i, case, func_version, version_name, j)
                all_results[i][j] = result
        return all_results

    def _collect_parallel_sync(self, versions_to_run: tuple[Callable[P, R], ...], num_threads: int) -> _AllResults:
        """Collects results in parallel using threads for synchronous execution."""
        all_results: _AllResults = [[None for _ in versions_to_run] for _ in self._cases]
        futures_map: dict[concurrent.futures.Future[VersionResult[R]], tuple[int, int]] = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            for i, case in enumerate(self._cases):
                for j, func_version in enumerate(versions_to_run):
                    version_name = self._get_function_name(func_version, j, versions_to_run)
                    future = executor.submit(self._execute_and_trace_sync, i, case, func_version, version_name, j)
                    futures_map[future] = (i, j)

            for future in concurrent.futures.as_completed(futures_map):
                case_idx, version_idx = futures_map[future]
                try:
                    result = future.result()
                    all_results[case_idx][version_idx] = result
                except Exception as exc:
                    self._console.print(
                        f"[bold red]Error in parallel task ({case_idx},{version_idx}): {exc}[/bold red]"
                    )
                    version_name = self._get_function_name(versions_to_run[version_idx], version_idx, versions_to_run)
                    all_results[case_idx][version_idx] = VersionResult[R](
                        case_index=case_idx,
                        version_index=version_idx,
                        version_name=version_name,
                        error=exc,
                        metric_results={},
                    )
        return all_results

    async def _collect_parallel_async(self, versions_to_run: tuple[AnyCallable, ...]) -> _AllResults:
        """Collects results in parallel using asyncio.gather for asynchronous execution."""
        all_results: _AllResults = [[None for _ in versions_to_run] for _ in self._cases]
        tasks: list[asyncio.Task[VersionResult[R]]] = []
        indices: list[tuple[int, int]] = []

        for i, case in enumerate(self._cases):
            for j, func_version in enumerate(versions_to_run):
                version_name = self._get_function_name(func_version, j, versions_to_run)
                tasks.append(asyncio.create_task(self._execute_and_trace_async(i, case, func_version, version_name, j)))
                indices.append((i, j))

        gathered_results = await asyncio.gather(*tasks, return_exceptions=True)

        for idx, result_or_exc in enumerate(gathered_results):
            case_idx, version_idx = indices[idx]
            version_name = self._get_function_name(versions_to_run[version_idx], version_idx, versions_to_run)
            if isinstance(result_or_exc, Exception):
                self._console.print(
                    f"[bold red]Error in async task ({case_idx},{version_idx}): {result_or_exc}[/bold red]"
                )
                all_results[case_idx][version_idx] = VersionResult[R](
                    case_index=case_idx,
                    version_index=version_idx,
                    version_name=version_name,
                    error=result_or_exc,
                    metric_results={},
                )
            elif isinstance(result_or_exc, VersionResult):
                all_results[case_idx][version_idx] = result_or_exc
            else:
                self._console.print(
                    f"[bold red]Unexpected result type ({case_idx},{version_idx}): {type(result_or_exc)}[/bold red]"
                )
                all_results[case_idx][version_idx] = VersionResult[R](
                    case_index=case_idx,
                    version_index=version_idx,
                    version_name=version_name,
                    error=Exception(f"Unexpected result type: {type(result_or_exc)}"),
                    metric_results={},
                )
        return all_results

    def _save_results_to_csv(self, all_results: _AllResults, csv_filename: str, metric_names: list[str]) -> None:
        """Saves the detailed experiment results to a CSV file."""
        try:
            self._console.print(f"[info]Saving detailed results to [bold]{csv_filename}[/bold]...[/info]")
            with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
                csv_writer: csv._writer = csv.writer(csvfile)
                header: list[str] = (
                    ["Case #", "Inputs", "Ideal", "Version", "Actual (Unwrapped)"] + metric_names + ["Error"]
                )
                csv_writer.writerow(header)
                for case_idx, case_data in enumerate(self._cases):
                    if case_idx < len(all_results):
                        for version_result in all_results[case_idx]:
                            if version_result is None:
                                continue
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
                                    self._format_inputs(case_data),
                                    repr(case_data.ideal),
                                    version_result.version_name,
                                    repr(version_result.actual_unwrapped)
                                    if version_result.error is None
                                    else "N/A (Func Err)",
                                ]
                                + metric_values_for_row
                                + [str(version_result.error) if version_result.error else ""]
                            )
                            csv_writer.writerow(row_data)
            self._console.print(f"[info]Successfully saved results to [bold]{csv_filename}[/bold][/info]")
        except IOError as e:
            self._console.print(f"[bold red]Error saving results to CSV:[/bold red] {e}")
        except Exception as e:
            self._console.print(f"[bold red]Unexpected error during CSV export:[/bold red] {e}")

    def _calculate_summary(
        self, all_results: _AllResults, unique_version_names: list[str], metric_names: list[str]
    ) -> _SummaryResultData:
        """Calculates summary statistics for each metric per version."""
        summary_results: _SummaryResultData = {}
        if not all_results or not all_results[0]:
            return summary_results

        for version_index, version_name in enumerate(unique_version_names):
            summary_results[version_name] = {}
            for metric_name in metric_names:
                valid: list[bool | float | int] = []
                for case_idx in range(len(self._cases)):
                    if case_idx < len(all_results) and version_index < len(all_results[case_idx]):
                        vr = all_results[case_idx][version_index]
                        if vr and vr.error is None:
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

    def _display_details(
        self, all_results: _AllResults, metric_names: list[str], versions_to_run: Sequence[AnyCallable]
    ) -> None:
        """Displays the detailed results with rows per case and columns per version."""
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

        # Define static columns
        detail_table.add_column("Case #", style="dim", justify="right", no_wrap=True)
        detail_table.add_column("Inputs", style="yellow", overflow="fold", min_width=30, ratio=2)
        detail_table.add_column("Ideal", style="green", overflow="fold", min_width=15, ratio=1)

        # Define dynamic columns per version
        version_names = [self._get_function_name(f, i, versions_to_run) for i, f in enumerate(versions_to_run)]
        for version_name in version_names:
            detail_table.add_column(f"{version_name} - Output", style="cyan", overflow="fold", min_width=20, ratio=2)
            if self._metrics:
                for metric_name in metric_names:
                    detail_table.add_column(f"{version_name} - {metric_name}", justify="center", min_width=10)
            detail_table.add_column(f"{version_name} - Error", style="red", overflow="fold", min_width=15, ratio=1)

        # Populate rows
        for i, case in enumerate(self._cases):
            row_data: list[str] = [str(i + 1), self._format_inputs(case), repr(case.ideal)]
            if i < len(all_results):
                case_run_results = all_results[i]
                for j, version_result in enumerate(case_run_results):
                    if version_result is None:  # Handle potential task failure
                        row_data.append("[grey50]Task Error[/grey50]")
                        if self._metrics:
                            row_data.extend([""] * len(metric_names))
                        row_data.append("")  # Error column
                        continue

                    # Append Actual Output
                    if version_result.error:
                        row_data.append("[grey50]N/A (Func Err)[/grey50]")
                    else:
                        row_data.append(repr(version_result.actual_unwrapped))  # Show unwrapped

                    # Append Metrics
                    if self._metrics:
                        for name in metric_names:
                            result = version_result.metric_results.get(name, "[grey50]Missing[/grey50]")
                            if isinstance(result, bool):
                                row_data.append(
                                    "[green][bold]True[/bold][/green]" if result else "[red][bold]False[/bold][/red]"
                                )
                            elif isinstance(result, (int, float)):
                                row_data.append(f"{result:.4f}" if isinstance(result, float) else str(result))
                            else:
                                row_data.append(str(result))

                    # Append Error
                    row_data.append(str(version_result.error) if version_result.error else "")
            else:
                # Case where no results are available for the row (should not happen if populated correctly)
                num_version_cols = len(versions_to_run) * (1 + (len(metric_names) if self._metrics else 0) + 1)
                row_data.extend(["[grey50]No results[/grey50]"] * num_version_cols)

            detail_table.add_row(*row_data)

        self._console.print(detail_table)

    def _post_process_results(
        self,
        all_results: _AllResults,
        unique_version_names: list[str],
        metric_names: list[str],
        run_span: OTSpan,
        csv_filename: str,
        versions_ran: Sequence[AnyCallable],
    ) -> None:
        """Handles saving, summary, and detailed display after results are collected."""
        try:
            self._save_results_to_csv(all_results, csv_filename, metric_names)
            run_span.set_attribute("experiment.csv_output_file", csv_filename)
        except Exception as e:
            self._console.print(f"[bold red]Failed during CSV saving:[/bold red] {e}")
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
            # Pass versions_ran to details display for column generation
            self._display_details(all_results, metric_names, versions_ran)
        except Exception as e:
            self._console.print(f"[bold red]Error during detailed results display:[/bold red] {e}")
            run_span.record_exception(e)

    def run(self, *versions: Callable[P, R], num_threads: int | None = None, include_target_fn: bool = True) -> None:
        """
        Runs the experiment synchronously for all registered cases and metrics.

        Requires the target function and all provided versions to be synchronous.
        Uses a ThreadPoolExecutor for parallel execution if num_threads > 1.

        Args:
            *versions: Additional synchronous function versions to test.
            num_threads: The number of worker threads for parallel execution. Default is sequential.
            include_target_fn: Whether to include the initial target function. Defaults to True.

        Raises:
            TypeError: If the target function or any provided version is async.
        """
        target_fn_sync: Callable[P, R] | None = None
        if include_target_fn:
            if self._is_target_async:
                raise TypeError(
                    f"Target function '{getattr(self._target_fn, '__name__', '...')}' is async. Use arun() instead or set include_target_fn=False."
                )
            target_fn_sync = cast(Callable[P, R], self._target_fn)

        sync_versions: list[Callable[P, R]] = []
        for v in versions:
            if inspect.iscoroutinefunction(v):
                raise TypeError(f"Sync run() called with async version: {getattr(v, '__name__', '...')}. Use arun().")
            sync_versions.append(v)

        versions_to_run_list: list[Callable[P, R]] = []
        if target_fn_sync:
            versions_to_run_list.append(target_fn_sync)
        versions_to_run_list.extend(sync_versions)

        if not versions_to_run_list:
            self._console.print(
                "[yellow]Warning: No functions selected to run (check include_target_fn and versions).[/yellow]"
            )
            return

        if not self._cases:
            self._console.print("[yellow]Warning: No test cases added. Nothing to run.[/yellow]")
            return

        versions_to_run = tuple(versions_to_run_list)

        with self._tracer.start_as_current_span("Experiment.run[sync]") as run_span:
            timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            csv_filename: str = f"run_{timestamp}.csv"
            num_versions: int = len(versions_to_run)
            metric_names: list[str] = [m["name"] for m, _ in self._metrics]
            unique_version_names: list[str] = [
                self._get_function_name(f, i, versions_to_run) for i, f in enumerate(versions_to_run)
            ]

            run_span.set_attribute("experiment.execution_mode", "sync")
            run_span.set_attribute("experiment.num_cases", len(self._cases))
            run_span.set_attribute("experiment.num_versions", num_versions)
            run_span.set_attribute("experiment.metric_names", metric_names)
            run_span.set_attribute("experiment.version_names", unique_version_names)
            parallel = num_threads is not None and num_threads > 1
            run_span.set_attribute("experiment.parallel", parallel)
            if parallel:
                run_span.set_attribute("experiment.num_threads", num_threads)

            self._console.print(
                f"\n[bold cyan]Running Experiment (Sync{' Parallel' if parallel else ''}) "
                f"({len(self._cases)} cases, {num_versions} versions)...[/bold cyan]"
            )

            all_results: _AllResults
            if parallel:
                all_results = self._collect_parallel_sync(versions_to_run, cast(int, num_threads))
            else:
                all_results = self._collect_sequential(versions_to_run)

            self._post_process_results(
                all_results, unique_version_names, metric_names, run_span, csv_filename, versions_to_run
            )

    async def arun(self, *versions: AnyCallable, include_target_fn: bool = True) -> None:
        """
        Runs the experiment asynchronously for all registered cases and metrics.

        Accepts a mix of sync/async functions. Executes using asyncio.gather.

        Args:
            *versions: Additional sync or async function versions to test.
            include_target_fn: Whether to include the initial target function. Defaults to True.
        """
        if not include_target_fn and not versions:
            self._console.print(
                "[yellow]Warning: No versions provided and include_target_fn=False. Nothing to run.[/yellow]"
            )
            return
        if not self._cases:
            self._console.print("[yellow]Warning: No test cases added. Nothing to run.[/yellow]")
            return

        versions_to_run_list: list[AnyCallable] = []
        if include_target_fn:
            versions_to_run_list.append(self._target_fn)
        versions_to_run_list.extend(versions)

        if not versions_to_run_list:
            self._console.print(
                "[yellow]Warning: No functions selected to run (check include_target_fn and versions).[/yellow]"
            )
            return

        versions_to_run = tuple(versions_to_run_list)

        with self._tracer.start_as_current_span("Experiment.run[async]") as run_span:
            timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            csv_filename: str = f"run_{timestamp}.csv"
            num_versions: int = len(versions_to_run)
            metric_names: list[str] = [m["name"] for m, _ in self._metrics]
            unique_version_names: list[str] = [
                self._get_function_name(f, i, versions_to_run) for i, f in enumerate(versions_to_run)
            ]

            run_span.set_attribute("experiment.execution_mode", "async")
            run_span.set_attribute("experiment.num_cases", len(self._cases))
            run_span.set_attribute("experiment.num_versions", num_versions)
            run_span.set_attribute("experiment.metric_names", metric_names)
            run_span.set_attribute("experiment.version_names", unique_version_names)
            run_span.set_attribute("experiment.parallel", True)

            self._console.print(
                f"\n[bold cyan]Running Experiment (Async Parallel) "
                f"({len(self._cases)} cases, {num_versions} versions)...[/bold cyan]"
            )

            all_results = await self._collect_parallel_async(versions_to_run)

            self._post_process_results(
                all_results, unique_version_names, metric_names, run_span, csv_filename, versions_to_run
            )
