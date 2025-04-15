# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SpanUpdateParams", "Tag"]


class SpanUpdateParams(TypedDict, total=False):
    tags: Optional[Iterable[Tag]]


class Tag(TypedDict, total=False):
    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    name: Required[str]

    organization_uuid: Required[str]

    uuid: Required[str]

    project_uuid: Optional[str]
