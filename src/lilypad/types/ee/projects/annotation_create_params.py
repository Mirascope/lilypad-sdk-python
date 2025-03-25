# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .label import Label
from .evaluation_type import EvaluationType

__all__ = ["AnnotationCreateParams", "Body"]


class AnnotationCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    assigned_to: Optional[List[str]]

    data: Optional[object]

    function_uuid: Optional[str]

    label: Optional[Label]
    """Label enum"""

    project_uuid: Optional[str]

    reasoning: Optional[str]

    span_uuid: Optional[str]

    type: Optional[EvaluationType]
    """Evaluation type enum"""
