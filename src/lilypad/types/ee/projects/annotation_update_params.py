# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .label import Label
from .evaluation_type import EvaluationType

__all__ = ["AnnotationUpdateParams"]


class AnnotationUpdateParams(TypedDict, total=False):
    project_uuid: Required[str]

    assigned_to: Optional[str]

    data: Optional[object]

    label: Optional[Label]
    """Label enum"""

    reasoning: Optional[str]

    type: Optional[EvaluationType]
    """Evaluation type enum"""
