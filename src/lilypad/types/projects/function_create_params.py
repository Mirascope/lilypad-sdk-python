# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .functions.common_call_params_param import CommonCallParamsParam

__all__ = ["FunctionCreateParams", "Dependencies"]


class FunctionCreateParams(TypedDict, total=False):
    code: Required[str]

    hash: Required[str]

    name: Required[str]

    signature: Required[str]

    archived: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    arg_types: Dict[str, str]

    call_params: CommonCallParamsParam
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

    custom_id: Optional[str]

    dependencies: Dict[str, Dependencies]

    is_versioned: Optional[bool]

    model: Optional[str]

    body_project_uuid: Annotated[Optional[str], PropertyInfo(alias="project_uuid")]

    prompt_template: Optional[str]

    provider: Optional[str]

    version_num: Optional[int]


class Dependencies(TypedDict, total=False):
    extras: Required[Optional[List[str]]]

    version: Required[str]
