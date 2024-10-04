# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProviderCallParamsTable"]


class ProviderCallParamsTable(BaseModel):
    llm_function_id: Optional[int] = None

    model: str

    prompt_template: str

    provider: Literal["openai", "anthropic"]
    """Provider name enum"""

    id: Optional[int] = None

    call_params: Optional[str] = None
