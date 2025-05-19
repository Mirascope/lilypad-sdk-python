# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .ee.user_public import UserPublic

__all__ = ["OrganizationInvitePublic"]


class OrganizationInvitePublic(BaseModel):
    email: str

    invited_by: str

    organization_uuid: str

    resend_email_id: str

    user: UserPublic
    """User public model"""

    uuid: str

    expires_at: Optional[datetime] = None

    invite_link: Optional[str] = None
