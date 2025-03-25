# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .functions.function_public import FunctionPublic

__all__ = ["FunctionListResponse"]

FunctionListResponse: TypeAlias = List[FunctionPublic]
