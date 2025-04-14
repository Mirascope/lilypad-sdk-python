# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SpanAssignAnnotationParams"]


class SpanAssignAnnotationParams(TypedDict, total=False):
    project_uuid: Required[str]

    assignee_email: Required[str]
