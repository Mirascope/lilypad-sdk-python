# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel
from .common_call_params import CommonCallParams

__all__ = ["FunctionPublic", "Dependencies"]


class Dependencies(BaseModel):
    extras: Optional[List[str]] = None

    version: str


class FunctionPublic(BaseModel):
    code: str

    hash: str

    name: str

    signature: str

    uuid: str

    archived: Optional[datetime] = None

    arg_types: Optional[Dict[str, str]] = None

    call_params: Optional[CommonCallParams] = None
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

    custom_id: Optional[str] = None

    dependencies: Optional[Dict[str, Dependencies]] = None

    is_versioned: Optional[bool] = None

    model: Optional[str] = None

    project_uuid: Optional[str] = None

    prompt_template: Optional[str] = None

    provider: Optional[str] = None

    version_num: Optional[int] = None
