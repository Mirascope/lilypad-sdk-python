# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProviderCallParamCreateParams"]


class ProviderCallParamCreateParams(TypedDict, total=False):
    call_params: Required[Optional[object]]

    model: Required[str]

    prompt_template: Required[str]

    provider: Required[Literal["openai", "anthropic"]]
    """Provider name enum"""
