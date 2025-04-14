# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...projects.functions.common_call_params_param import CommonCallParamsParam

__all__ = ["FunctionRunPlaygroundParams"]


class FunctionRunPlaygroundParams(TypedDict, total=False):
    project_uuid: Required[str]

    arg_types: Required[Optional[Dict[str, str]]]

    arg_values: Required[Dict[str, Union[float, bool, str, Iterable[object], object]]]

    call_params: Required[Optional[CommonCallParamsParam]]
    """Common parameters shared across LLM providers.

    Note: Each provider may handle these parameters differently or not support them
    at all. Please check provider-specific documentation for parameter support and
    behavior.

    Attributes: temperature: Controls randomness in the output (0.0 to 1.0).
    max_tokens: Maximum number of tokens to generate. top_p: Nucleus sampling
    parameter (0.0 to 1.0). frequency_penalty: Penalizes frequent tokens (-2.0 to
    2.0). presence_penalty: Penalizes tokens based on presence (-2.0 to 2.0). seed:
    Random seed for reproducibility. stop: Stop sequence(s) to end generation.
    """

    model: Required[str]

    prompt_template: Required[str]

    provider: Required[Literal["openai", "anthropic", "openrouter", "gemini"]]
    """Provider name enum"""
