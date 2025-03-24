# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .user_role import UserRole

__all__ = ["UserOrganizationTable"]


class UserOrganizationTable(BaseModel):
    organization_uuid: str

    role: UserRole
    """User role enum."""

    user_uuid: str

    created_at: Optional[datetime] = None

    uuid: Optional[str] = None
