# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["SpanUpdateTagsParams"]


class SpanUpdateTagsParams(TypedDict, total=False):
    tags_by_name: Optional[List[str]]

    tags_by_uuid: Optional[List[str]]
