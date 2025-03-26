# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EnvironmentDeployParams"]


class EnvironmentDeployParams(TypedDict, total=False):
    project_uuid: Required[str]

    function_uuid: Required[str]

    notes: Optional[str]
