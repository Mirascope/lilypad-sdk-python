# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SpanListParams"]


class SpanListParams(TypedDict, total=False):
    limit: int

    query_string: Optional[str]

    scope: Optional[Literal["lilypad", "llm"]]
    """Instrumentation Scope name of the span"""

    time_range_end: Optional[int]

    time_range_start: Optional[int]

    type: Optional[str]
