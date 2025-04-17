# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .label import Label
from ...._models import BaseModel
from .evaluation_type import EvaluationType
from ...span_more_details import SpanMoreDetails

__all__ = ["AnnotationPublic"]


class AnnotationPublic(BaseModel):
    created_at: datetime

    project_uuid: str

    span: SpanMoreDetails
    """Span more details model."""

    span_uuid: str

    uuid: str

    assigned_to: Optional[str] = None

    data: Optional[object] = None

    function_uuid: Optional[str] = None

    label: Optional[Label] = None
    """Label enum"""

    reasoning: Optional[str] = None

    type: Optional[EvaluationType] = None
    """Evaluation type enum"""
