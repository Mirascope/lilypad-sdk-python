# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallCreateParams"]


class CallCreateParams(TypedDict, total=False):
    input: Required[str]

    output: Required[str]

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    prompt_version_id: int
