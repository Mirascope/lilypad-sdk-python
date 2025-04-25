# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpanListParams"]


class SpanListParams(TypedDict, total=False):
    query_string: Required[str]
    """Search query string"""

    limit: int
    """Maximum number of results to return"""

    scope: Optional[Literal["lilypad", "llm"]]
    """Instrumentation Scope name of the span"""

    time_range_end: Optional[int]
    """End time range in milliseconds"""

    time_range_start: Optional[int]
    """Start time range in milliseconds"""

    type: Optional[str]
    """Type of spans to search for"""
