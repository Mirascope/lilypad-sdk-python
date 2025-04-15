# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnnotationCreateParams", "Body"]


class AnnotationCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    assigned_to: Optional[List[str]]

    assignee_email: Optional[str]

    function_uuid: Optional[str]

    project_uuid: Optional[str]

    span_uuid: Optional[str]
