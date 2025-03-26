# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ...._models import BaseModel

__all__ = ["CommonCallParams"]


class CommonCallParams(BaseModel):
    frequency_penalty: Optional[float] = None

    max_tokens: Optional[int] = None

    presence_penalty: Optional[float] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None
