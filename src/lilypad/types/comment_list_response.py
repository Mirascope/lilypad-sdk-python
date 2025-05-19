# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .comment_public import CommentPublic

__all__ = ["CommentListResponse"]

CommentListResponse: TypeAlias = List[CommentPublic]
