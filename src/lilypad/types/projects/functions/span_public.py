# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel
from .function_public import FunctionPublic
from ...ee.projects.label import Label
from ...ee.projects.evaluation_type import EvaluationType

__all__ = ["SpanPublic", "Annotation"]


class Annotation(BaseModel):
    organization_uuid: str

    assigned_to: Optional[str] = None

    created_at: Optional[datetime] = None

    data: Optional[object] = None

    function_uuid: Optional[str] = None

    label: Optional[Label] = None
    """Label enum"""

    project_uuid: Optional[str] = None

    reasoning: Optional[str] = None

    span_uuid: Optional[str] = None

    type: Optional[EvaluationType] = None
    """Evaluation type enum"""

    uuid: Optional[str] = None


class SpanPublic(BaseModel):
    annotations: List[Annotation]

    child_spans: List["SpanPublic"]

    created_at: datetime

    project_uuid: str

    scope: Literal["lilypad", "llm"]
    """Instrumentation Scope name of the span"""

    span_id: str

    uuid: str

    cost: Optional[float] = None

    data: Optional[object] = None

    display_name: Optional[str] = None

    duration_ms: Optional[float] = None

    function: Optional[FunctionPublic] = None
    """Function public model."""

    function_uuid: Optional[str] = None

    input_tokens: Optional[float] = None

    output_tokens: Optional[float] = None

    parent_span_id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function", "trace"]] = None
    """Span type"""

    version: Optional[int] = None


if PYDANTIC_V2:
    SpanPublic.model_rebuild()
    Annotation.model_rebuild()
else:
    SpanPublic.update_forward_refs()  # type: ignore
    Annotation.update_forward_refs()  # type: ignore
