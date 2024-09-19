# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PromptVersionCreateParams"]


class PromptVersionCreateParams(TypedDict, total=False):
    function_name: Required[str]

    prompt_template: Required[str]

    lexical_closure: Optional[str]

    previous_version_id: Optional[int]

    version_hash: Optional[str]
