# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LlmFunctionCreateParams"]


class LlmFunctionCreateParams(TypedDict, total=False):
    code: Required[str]

    function_name: Required[str]

    version_hash: Required[str]

    input_arguments: Optional[str]
