# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .llm_function_table import LlmFunctionTable

__all__ = ["LlmFunctionListResponse"]

LlmFunctionListResponse: TypeAlias = List[LlmFunctionTable]
