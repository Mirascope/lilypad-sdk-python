# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..ee.user_role import UserRole
from ..organization_public import OrganizationPublic

__all__ = ["UserPublic", "UserOrganization"]


class UserOrganization(BaseModel):
    organization: OrganizationPublic
    """Organization public model"""

    organization_uuid: str

    role: UserRole
    """User role enum."""

    user_uuid: str

    uuid: str


class UserPublic(BaseModel):
    email: str

    first_name: str

    uuid: str

    access_token: Optional[str] = None

    active_organization_uuid: Optional[str] = None

    keys: Optional[Dict[str, str]] = None

    last_name: Optional[str] = None

    scopes: Optional[List[str]] = None

    user_organizations: Optional[List[UserOrganization]] = None
