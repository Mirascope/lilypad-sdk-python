# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .llm_functions.provider_call_params_table import ProviderCallParamsTable

__all__ = ["LlmFunctionBasePublic"]


class LlmFunctionBasePublic(BaseModel):
    id: int

    code: str

    function_name: str

    provider_call_params: Optional[List[ProviderCallParamsTable]] = None

    input_arguments: Optional[str] = None

    version_hash: Optional[str] = None
