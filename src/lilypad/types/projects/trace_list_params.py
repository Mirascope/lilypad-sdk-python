# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TraceListParams"]


class TraceListParams(TypedDict, total=False):
    limit: int

    offset: int

    order: Literal["asc", "desc"]
