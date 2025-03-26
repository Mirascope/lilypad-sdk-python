# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .project_public import ProjectPublic
from .auth.user_public import UserPublic
from .environment_public import EnvironmentPublic

__all__ = ["APIKeyListResponse", "APIKeyListResponseItem"]


class APIKeyListResponseItem(BaseModel):
    environment: EnvironmentPublic
    """Environment public model."""

    key_hash: str

    name: str

    project: ProjectPublic
    """Project Public Model."""

    project_uuid: str

    user: UserPublic
    """User public model"""

    uuid: str

    environment_uuid: Optional[str] = None

    expires_at: Optional[datetime] = None


APIKeyListResponse: TypeAlias = List[APIKeyListResponseItem]
