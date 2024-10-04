# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LlmFunctionTable"]


class LlmFunctionTable(BaseModel):
    code: str

    function_name: str

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    input_arguments: Optional[str] = None

    version_hash: Optional[str] = None
