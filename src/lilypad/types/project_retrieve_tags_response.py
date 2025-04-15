# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ProjectRetrieveTagsResponse", "ProjectRetrieveTagsResponseItem"]


class ProjectRetrieveTagsResponseItem(BaseModel):
    created_at: datetime

    name: str

    organization_uuid: str

    uuid: str

    project_uuid: Optional[str] = None


ProjectRetrieveTagsResponse: TypeAlias = List[ProjectRetrieveTagsResponseItem]
