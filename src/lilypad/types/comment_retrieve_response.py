# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CommentRetrieveResponse"]


class CommentRetrieveResponse(BaseModel):
    created_at: datetime

    span_uuid: str

    text: str

    user_uuid: str

    uuid: str

    child_comments: Optional[List[object]] = None

    is_edited: Optional[bool] = None

    parent_comment_uuid: Optional[str] = None

    updated_at: Optional[datetime] = None
