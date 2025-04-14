# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    span_uuid: Required[str]

    text: Required[str]

    parent_comment_uuid: Optional[str]
