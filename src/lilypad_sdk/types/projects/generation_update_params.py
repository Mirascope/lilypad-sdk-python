# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GenerationUpdateParams"]


class GenerationUpdateParams(TypedDict, total=False):
    project_uuid: Required[str]

    is_default: Optional[bool]
