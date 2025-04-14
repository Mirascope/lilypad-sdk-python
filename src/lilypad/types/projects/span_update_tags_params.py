# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SpanUpdateTagsParams"]


class SpanUpdateTagsParams(TypedDict, total=False):
    project_uuid: Required[str]

    body: Required[List[str]]
