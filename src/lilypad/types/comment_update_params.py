# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CommentUpdateParams"]


class CommentUpdateParams(TypedDict, total=False):
    is_edited: Optional[bool]

    text: Optional[str]
