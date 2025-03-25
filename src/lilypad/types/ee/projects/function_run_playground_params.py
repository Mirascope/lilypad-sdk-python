# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...function_create_param import FunctionCreateParam

__all__ = ["FunctionRunPlaygroundParams"]


class FunctionRunPlaygroundParams(TypedDict, total=False):
    project_uuid: Required[str]

    arg_values: Required[Dict[str, Union[float, bool, str, Iterable[object], object]]]

    model: Required[str]

    provider: Required[Literal["openai", "anthropic", "openrouter", "gemini"]]
    """Provider name enum"""

    function: Optional[FunctionCreateParam]
    """Function create model."""
