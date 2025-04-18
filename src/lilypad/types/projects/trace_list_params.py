# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TraceListParams"]


class TraceListParams(TypedDict, total=False):
    cursor: Optional[str]
    """last span_id of previous page"""

    limit: int
