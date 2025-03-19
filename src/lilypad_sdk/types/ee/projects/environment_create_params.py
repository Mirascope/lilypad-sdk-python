# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnvironmentCreateParams"]


class EnvironmentCreateParams(TypedDict, total=False):
    name: Required[str]

    project_uuid_2: Required[Annotated[str, PropertyInfo(alias="project_uuid")]]

    description: Optional[str]

    is_default: bool
