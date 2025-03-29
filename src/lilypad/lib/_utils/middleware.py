"""Utilities for middleware for Lilypad prompts and Mirascope calls."""

from __future__ import annotations

import json
import base64
import logging
from io import BytesIO
from uuid import UUID
from typing import TYPE_CHECKING, Any, TypeVar, ParamSpec, cast
from contextlib import contextmanager, _GeneratorContextManager
from collections.abc import Callable, Generator

from pydantic import BaseModel
from mirascope.core import base as mb
from opentelemetry.trace import Span, Status, StatusCode, SpanContext, get_tracer
from mirascope.integrations import middleware_factory
from opentelemetry.util.types import AttributeValue
from mirascope.integrations._middleware_factory import SyncFunc, AsyncFunc

from . import jsonable_encoder
from .settings import get_settings
from .functions import ArgValues

if TYPE_CHECKING:
    from ...types.projects.functions import FunctionPublic


_P = ParamSpec("_P")
_R = TypeVar("_R")


try:
    import PIL
    import PIL.WebPImagePlugin
except ImportError:

    class PIL:
        class WebPImagePlugin:
            class WebPImageFile:
                def save(self, *args, **kwargs):
                    raise NotImplementedError("Pillow is not installed. Please install Pillow to use this feature.")


logger = logging.getLogger(__name__)


class SpanContextHolder:
    """Holds the OpenTelemetry SpanContext."""

    def __init__(self) -> None:
        self._span_context: SpanContext | None = None

    def set_span_context(self, span: Span) -> None:
        self._span_context = span.get_span_context()

    @property
    def span_context(self) -> SpanContext | None:
        return self._span_context


def _get_custom_context_manager(
    function: FunctionPublic,
    arg_values: ArgValues,
    is_async: bool,
    prompt_template: str | None = None,
    project_uuid: UUID | None = None,
    span_context_holder: SpanContextHolder | None = None,
) -> Callable[..., _GeneratorContextManager[Span]]:
    @contextmanager
    def custom_context_manager(
        fn: SyncFunc | AsyncFunc,
    ) -> Generator[Span, Any, None]:
        tracer = get_tracer("lilypad")
        new_project_uuid = project_uuid or get_settings().project_id
        jsonable_arg_values = {}
        for arg_name, arg_value in arg_values.items():
            try:
                serialized_arg_value = jsonable_encoder(arg_value)
            except ValueError:
                serialized_arg_value = "could not serialize"
            jsonable_arg_values[arg_name] = serialized_arg_value
        with tracer.start_as_current_span(f"{fn.__name__}") as span:
            attributes: dict[str, AttributeValue] = {
                "lilypad.project_uuid": str(new_project_uuid) if new_project_uuid else "",
                "lilypad.type": "function",
                "lilypad.function.uuid": str(function.uuid),
                "lilypad.function.name": fn.__name__,
                "lilypad.function.signature": function.signature,
                "lilypad.function.code": function.code,
                "lilypad.function.arg_types": json.dumps(function.arg_types),
                "lilypad.function.arg_values": json.dumps(jsonable_arg_values),
                "lilypad.function.prompt_template": prompt_template or "",
                "lilypad.function.version": function.version_num if function.version_num else -1,
                "lilypad.is_async": is_async,
            }
            filtered_attributes = {k: v for k, v in attributes.items() if v is not None}
            span.set_attributes(filtered_attributes)
            if span_context_holder:
                span_context_holder.set_span_context(span)
            yield span

    return custom_context_manager


def encode_gemini_part(
    part: str | dict | PIL.WebPImagePlugin.WebPImageFile,
) -> str | dict:
    if isinstance(part, dict):
        if "mime_type" in part and "data" in part:
            # Handle binary data by base64 encoding it
            return {
                "mime_type": part["mime_type"],
                "data": base64.b64encode(part["data"]).decode("utf-8"),
            }
        return part
    elif isinstance(part, PIL.WebPImagePlugin.WebPImageFile):
        buffered = BytesIO()
        part.save(buffered, format="WEBP")  # Use "WEBP" to maintain the original format
        img_bytes = buffered.getvalue()
        return {
            "mime_type": "image/webp",
            "data": base64.b64encode(img_bytes).decode("utf-8"),
        }
    return part


def _serialize_proto_data(data: list[dict]) -> str:
    serializable_data = []
    for item in data:
        serialized_item = item.copy()
        if "parts" in item:
            serialized_item["parts"] = [encode_gemini_part(part) for part in item["parts"]]
        serializable_data.append(serialized_item)

    return json.dumps(serializable_data)


def _set_call_response_attributes(response: mb.BaseCallResponse, span: Span) -> None:
    try:
        output = json.dumps(jsonable_encoder(response.message_param))
    except TypeError:
        output = str(response.message_param)
    try:
        messages = json.dumps(jsonable_encoder(response.messages))
    except TypeError:
        messages = _serialize_proto_data(response.messages)  # Gemini
    attributes: dict[str, AttributeValue] = {
        "lilypad.function.output": output,
        "lilypad.function.messages": messages,
    }
    span.set_attributes(attributes)


def _set_response_model_attributes(result: BaseModel | mb.BaseType, span: Span) -> None:
    if isinstance(result, BaseModel):
        completion = result.model_dump_json()
        # Safely handle the case where result._response might be None
        if (_response := getattr(result, "_response", None)) and (
            _response_messages := getattr(_response, "messages", None)
        ):
            messages = json.dumps(jsonable_encoder(_response_messages))
        else:
            messages = None
    else:
        if not isinstance(result, str | int | float | bool):
            result = str(result)
        completion = result
        messages = None

    attributes: dict[str, AttributeValue] = {
        "lilypad.function.output": completion,
    }
    if messages:
        attributes["lilypad.function.messages"] = messages
    span.set_attributes(attributes)


def _handle_call_response(result: mb.BaseCallResponse, fn: Callable, span: Span | None) -> None:
    if span is None:
        return
    _set_call_response_attributes(result, span)


def _handle_stream(stream: mb.BaseStream, fn: Callable, span: Span | None) -> None:
    if span is None:
        return
    call_response = cast(mb.BaseCallResponse, stream.construct_call_response())
    _set_call_response_attributes(call_response, span)


def _handle_response_model(result: BaseModel | mb.BaseType, fn: Callable, span: Span | None) -> None:
    if span is None:
        return

    _set_response_model_attributes(result, span)


def _handle_structured_stream(result: mb.BaseStructuredStream, fn: Callable, span: Span | None) -> None:
    if span is None:
        return

    _set_response_model_attributes(result.constructed_response_model, span)


async def _handle_call_response_async(result: mb.BaseCallResponse, fn: Callable, span: Span | None) -> None:
    if span is None:
        return

    _set_call_response_attributes(result, span)


async def _handle_stream_async(stream: mb.BaseStream, fn: Callable, span: Span | None) -> None:
    if span is None:
        return
    call_response = cast(mb.BaseCallResponse, stream.construct_call_response())
    _set_call_response_attributes(call_response, span)


async def _handle_response_model_async(result: BaseModel | mb.BaseType, fn: Callable, span: Span | None) -> None:
    if span is None:
        return
    _set_response_model_attributes(result, span)


async def _handle_structured_stream_async(result: mb.BaseStructuredStream, fn: Callable, span: Span | None) -> None:
    if span is None:
        return
    _set_response_model_attributes(result.constructed_response_model, span)


def _handle_error(error: Exception, fn: SyncFunc | AsyncFunc, span: Span | None) -> None:
    """Records the exception on the span. Does not suppress the error."""
    if span and span.is_recording():
        span.record_exception(error)
        span.set_status(Status(StatusCode.ERROR, f"{type(error).__name__}: {error}"))
    elif span is None:
        fn_name = getattr(fn, "__name__", "unknown_function")
        logger.error(f"Error during sync execution of {fn_name} (span not available): {error}")


async def _handle_error_async(error: Exception, fn: SyncFunc | AsyncFunc, span: Span | None) -> None:
    """Records the exception on the span. Does not suppress the error."""
    _handle_error(error, fn, span)


def create_mirascope_middleware(
    function: FunctionPublic,
    arg_values: ArgValues,
    is_async: bool,
    prompt_template: str | None = None,
    project_uuid: UUID | None = None,
    span_context_holder: SpanContextHolder | None = None,
) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]:
    """Creates the middleware decorator for a Lilypad/Mirascope function."""
    cm_callable: Callable[[SyncFunc | AsyncFunc], _GeneratorContextManager[Span]] = _get_custom_context_manager(
        function,
        arg_values,
        is_async,
        prompt_template,
        project_uuid,
        span_context_holder,
    )

    return middleware_factory(
        custom_context_manager=cm_callable,
        handle_call_response=_handle_call_response,
        handle_call_response_async=_handle_call_response_async,
        handle_stream=_handle_stream,
        handle_stream_async=_handle_stream_async,
        handle_response_model=_handle_response_model,
        handle_response_model_async=_handle_response_model_async,
        handle_structured_stream=_handle_structured_stream,
        handle_structured_stream_async=_handle_structured_stream_async,
        handle_error=_handle_error,
        handle_error_async=_handle_error_async,
    )


__all__ = ["create_mirascope_middleware", "SpanContextHolder"]
