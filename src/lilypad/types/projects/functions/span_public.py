# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel
from .function_public import FunctionPublic
from ...ee.projects.annotation_public import AnnotationPublic

__all__ = ["SpanPublic", "Tag"]


class Tag(BaseModel):
    created_at: datetime

    name: str

    organization_uuid: str

    uuid: str

    project_uuid: Optional[str] = None


class SpanPublic(BaseModel):
    annotations: List[AnnotationPublic]

    child_spans: List["SpanPublic"]

    created_at: datetime

    function: Optional[FunctionPublic] = None
    """Function public model."""

    project_uuid: str

    scope: Literal["lilypad", "llm"]
    """Instrumentation Scope name of the span"""

    span_id: str

    tags: List[Tag]

    uuid: str

    cost: Optional[float] = None

    data: Optional[object] = None

    display_name: Optional[str] = None

    duration_ms: Optional[float] = None

    function_uuid: Optional[str] = None

    input_tokens: Optional[float] = None

    output_tokens: Optional[float] = None

    parent_span_id: Optional[str] = None

    score: Optional[float] = None

    session_id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function", "trace"]] = None
    """Span type"""


if PYDANTIC_V2:
    SpanPublic.model_rebuild()
    Tag.model_rebuild()
else:
    SpanPublic.update_forward_refs()  # type: ignore
    Tag.update_forward_refs()  # type: ignore
