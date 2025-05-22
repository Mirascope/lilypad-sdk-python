# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..scope import Scope
from ...._compat import PYDANTIC_V2
from ...._models import BaseModel
from ...tag_public import TagPublic
from .function_public import FunctionPublic
from ...ee.projects.annotation_public import AnnotationPublic

__all__ = ["SpanPublic"]


class SpanPublic(BaseModel):
    annotations: List[AnnotationPublic]

    child_spans: List["SpanPublic"]

    created_at: datetime

    function: Optional[FunctionPublic] = None
    """Function public model."""

    project_uuid: str

    scope: Scope
    """Instrumentation Scope name of the span"""

    span_id: str

    tags: List[TagPublic]

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

    type: Optional[Literal["function", "trace", "mirascope.v1"]] = None
    """Span type"""


if PYDANTIC_V2:
    SpanPublic.model_rebuild()
else:
    SpanPublic.update_forward_refs()  # type: ignore
