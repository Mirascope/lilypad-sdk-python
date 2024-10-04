# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .llm_function_table import LlmFunctionTable

__all__ = ["SpanPublic"]


class SpanPublic(BaseModel):
    id: str

    child_spans: List[SpanPublic]

    data: str

    llm_function: LlmFunctionTable
    """LLM function table"""

    scope: Literal["lilypad", "llm"]
    """Instrumentation Scope name of the span"""

    created_at: Optional[datetime] = None

    display_name: Optional[str] = None

    llm_function_id: Optional[int] = None

    parent_span_id: Optional[str] = None


if PYDANTIC_V2:
    SpanPublic.model_rebuild()
else:
    SpanPublic.update_forward_refs()  # type: ignore
