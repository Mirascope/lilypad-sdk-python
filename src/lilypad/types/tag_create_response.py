# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TagCreateResponse"]


class TagCreateResponse(BaseModel):
    created_at: datetime

    name: str

    organization_uuid: str

    uuid: str

    project_uuid: Optional[str] = None
