# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CallArgsPublic"]


class CallArgsPublic(BaseModel):
    call_params: Optional[object] = None

    model: str

    prompt_template: str

    provider: Literal["openai", "anthropic"]
    """Provider name enum"""
