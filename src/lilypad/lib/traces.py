"""This module contains the `generation` decorator and related utilities for tracing."""
from __future__ import annotations

import json
import inspect
import threading
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Protocol,
    ParamSpec,
    TypeAlias,
    overload,
)
from functools import wraps
from contextlib import contextmanager
from collections.abc import Callable, Coroutine, Generator

from pydantic import BaseModel
from opentelemetry.trace import Span, get_tracer, get_tracer_provider
from opentelemetry.util.types import AttributeValue
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from ._utils import (
    call_safely,
    fn_is_async,
    jsonable_encoder,
    inspect_arguments,
    get_qualified_name,
)
from ._utils.settings import get_settings

_P = ParamSpec("_P")
_R = TypeVar("_R")

if TYPE_CHECKING:
    from ..lib import spans

TRACE_TYPE = "trace"

def _get_batch_span_processor() -> BatchSpanProcessor | None:
    """Get the BatchSpanProcessor from the current TracerProvider.

    Retrieve the BatchSpanProcessor from the current TracerProvider dynamically.
    This avoids using a global variable by inspecting the provider's _active_span_processors.
    """
    tracer_provider = get_tracer_provider()
    processor = getattr(tracer_provider, "_active_span_processor", None)
    if not processor:
        return None
    _span_processors = getattr(processor, "_span_processors", None)
    if _span_processors:
        for processor in _span_processors:
            if isinstance(processor, BatchSpanProcessor):
                return processor
    return None


# Global counter and lock for span order.
_span_counter_lock = threading.Lock()
_span_counter = 0


@contextmanager
def span_order_context(span: Span) -> Generator[None, None, None]:
    """Assign an explicit order to a span using a global counter."""
    global _span_counter
    with _span_counter_lock:
        _span_counter += 1
    yield

class TraceDecoratedFunctionWithContext(Protocol[_P, _R]):
    """Protocol for the `generation` decorator return type."""

    def __call__(self, trace_ctx: spans.Span, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

class TraceDecorator(Protocol):
    """Protocol for the `generation` decorator return type."""

    @overload
    def __call__(self, fn: TraceDecoratedFunctionWithContext[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...

    @overload
    def __call__(self, fn: TraceDecoratedFunctionWithContext[_P, _R]) -> Callable[_P, _R]: ...

    @overload
    def __call__(self, fn: Callable[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...

    @overload
    def __call__(self, fn: Callable[_P, _R]) -> Callable[_P, _R]: ...

    def __call__(
        self, fn: TraceDecoratedFunctionWithContext[_P, Coroutine[Any, Any, _R]] | TraceDecoratedFunctionWithContext[_P, _R] | Callable[_P, _R] | Callable[_P, Coroutine[Any, Any, _R]]
    ) -> Callable[_P, _R] | Callable[_P, Coroutine[Any, Any, _R]]:
        """Protocol `call` definition for `generation` decorator return type."""
        ...


_TraceAttribute: TypeAlias = dict[str, AttributeValue]


class _ResultHolder:
    """A class to hold the result of a function call."""

    def __init__(self) -> None:
        self.result = None

    def set_result(self, result: Any) -> None:
        """Set the result attribute."""
        self.result: Any = result


@contextmanager
def _set_span_attributes(
    trace_type: str, span: Span, span_attribute: _TraceAttribute, is_async: bool
) -> Generator[_ResultHolder, None, None]:
    """Set the attributes on the span."""
    settings = get_settings()
    span_attribute["lilypad.project_uuid"] = settings.project_id if settings.project_id else ""
    span_attribute["lilypad.type"] = trace_type
    span_attribute["lilypad.is_async"] = is_async
    span.set_attributes(span_attribute)
    result_holder = _ResultHolder()
    yield result_holder
    original_output = result_holder.result
    output_for_span = original_output.model_dump() if isinstance(original_output, BaseModel) else original_output
    span.set_attribute(f"lilypad.{trace_type}.output", str(output_for_span))


def _construct_trace_attributes(
    arg_types: dict[str, str],
    arg_values: dict[str, Any],
) -> dict[str, AttributeValue]:
    jsonable_arg_values = {}
    for arg_name, arg_value in arg_values.items():
        try:
            serialized_arg_value = jsonable_encoder(arg_value)
        except ValueError:
            serialized_arg_value = "could not serialize"
        jsonable_arg_values[arg_name] = serialized_arg_value
    return {
        "lilypad.trace.arg_types": json.dumps(arg_types),
        "lilypad.trace.arg_values": json.dumps(jsonable_arg_values),
    }


def trace() -> TraceDecorator:
    """The tracing LLM generations.

    The decorated function will trace and log automatically.

    Returns:
        TraceDecorator: The `trace` decorator return protocol.
    """

    @overload
    def decorator(fn: TraceDecoratedFunctionWithContext[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...

    @overload
    def decorator(fn: TraceDecoratedFunctionWithContext[_P, _R]) -> Callable[_P, _R]: ...

    @overload
    def decorator(fn: Callable[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...

    @overload
    def decorator(fn: Callable[_P, _R]) -> Callable[_P, _R]: ...

    def decorator(
        fn: TraceDecoratedFunctionWithContext[_P, Coroutine[Any, Any, _R]]
            | TraceDecoratedFunctionWithContext[_P, _R]
            | Callable[_P, _R]
            | Callable[_P, Coroutine[Any, Any, _R]],
    ) -> Callable[_P, _R] | Callable[_P, Coroutine[Any, Any, _R]]:
        signature = inspect.signature(fn)

        if fn_is_async(fn):

            @call_safely(fn)
            async def inner_async(*args: _P.args, **kwargs: _P.kwargs) -> _R:
                bound_args = signature.bind_partial(*args, **kwargs)

                with (
                    get_tracer("lilypad").start_as_current_span(get_qualified_name(fn)) as span,
                    span_order_context(span),
                ):
                    if "trace_ctx" in bound_args.arguments:
                        args = tuple((span, *args))
                    arg_types, arg_values = inspect_arguments(fn, *args, **kwargs)
                    arg_values.pop("trace_ctx", None)
                    arg_types, arg_values = inspect_arguments(fn, *args, **kwargs)
                    trace_attribute = _construct_trace_attributes(
                        arg_types=arg_types,
                        arg_values=arg_values,
                    )
                    with _set_span_attributes(TRACE_TYPE, span, trace_attribute, is_async=True) as result_holder:
                        output = await fn(*args, **kwargs)
                        result_holder.set_result(output)
                return output  # pyright: ignore [reportReturnType]

            return inner_async

        else:

            @call_safely(fn)
            def inner(*args: _P.args, **kwargs: _P.kwargs) -> _R:
                bound_args = signature.bind_partial(*args, **kwargs)
                with (
                    get_tracer("lilypad").start_as_current_span(get_qualified_name(fn)) as span,
                    span_order_context(span),
                ):
                    if "trace_ctx" in bound_args.arguments:
                        args = tuple((span, *args))
                    arg_types, arg_values = inspect_arguments(fn, *args, **kwargs)
                    arg_values.pop("trace_ctx", None)
                    trace_attribute = _construct_trace_attributes(
                        arg_types=arg_types,
                        arg_values=arg_values,
                    )
                    with _set_span_attributes(TRACE_TYPE, span, trace_attribute, is_async=False) as result_holder:
                        output = fn(*args, **kwargs)
                        result_holder.set_result(output)
                return output  # pyright: ignore [reportReturnType]
            return inner  # pyright: ignore [reportReturnType]

    return decorator
