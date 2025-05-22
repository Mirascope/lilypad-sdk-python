# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .scope import Scope

__all__ = ["SpanSearchTracesParams"]


class SpanSearchTracesParams(TypedDict, total=False):
    limit: int

    query_string: Optional[str]

    scope: Optional[Scope]
    """Instrumentation Scope name of the span"""

    time_range_end: Optional[int]

    time_range_start: Optional[int]

    type: Optional[str]
