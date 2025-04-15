# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["FunctionRunPlaygroundResponse", "TraceContext"]


class TraceContext(BaseModel):
    span_uuid: Optional[str] = None
    """The unique identifier for the current span within the trace."""


class FunctionRunPlaygroundResponse(BaseModel):
    result: object
    """The result returned by the executed function.

    Can be any JSON-serializable type.
    """

    trace_context: Optional[TraceContext] = None
    """Represents the tracing context information provided by Lilypad."""
