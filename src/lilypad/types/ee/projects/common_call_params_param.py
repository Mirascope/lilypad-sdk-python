# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypedDict

__all__ = ["CommonCallParamsParam"]


class CommonCallParamsParam(TypedDict, total=False):
    frequency_penalty: Optional[float]

    max_tokens: Optional[int]

    presence_penalty: Optional[float]

    seed: Optional[int]

    stop: Union[str, List[str], None]

    temperature: Optional[float]

    top_p: Optional[float]
