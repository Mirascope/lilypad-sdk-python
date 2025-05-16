# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel

__all__ = ["SpanListPaginatedResponse"]


class SpanListPaginatedResponse(BaseModel):
    items: List["SpanPublic"]
    """Current slice of items"""

    limit: int
    """Requested page size (limit)"""

    offset: int
    """Requested offset"""

    total: int
    """Total number of items"""


from .span_public import SpanPublic

if PYDANTIC_V2:
    SpanListPaginatedResponse.model_rebuild()
else:
    SpanListPaginatedResponse.update_forward_refs()  # type: ignore
