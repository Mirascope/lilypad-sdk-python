# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserConsentUpdateResponse"]


class UserConsentUpdateResponse(BaseModel):
    privacy_policy_accepted_at: datetime

    tos_accepted_at: datetime

    uuid: str

    privacy_policy_version: Optional[str] = None
    """Last updated date of the privacy policy accepted"""

    tos_version: Optional[str] = None
    """Last updated date of the terms of service accepted"""
