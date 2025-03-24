# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["EnvironmentPublic"]


class EnvironmentPublic(BaseModel):
    name: str

    organization_uuid: str

    project_uuid: str

    uuid: str

    description: Optional[str] = None

    is_default: Optional[bool] = None
