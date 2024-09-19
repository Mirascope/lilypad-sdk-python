# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallTable"]


class CallTable(BaseModel):
    input: str

    output: str

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    prompt_version_id: Optional[int] = None
