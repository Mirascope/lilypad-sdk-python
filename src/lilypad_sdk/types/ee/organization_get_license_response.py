# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OrganizationGetLicenseResponse"]


class OrganizationGetLicenseResponse(BaseModel):
    customer: str

    expires_at: datetime

    is_expired: bool
    """Check if the license has expired"""

    license_id: str

    organization_uuid: str

    tier: Literal[0, 1, 2, 3]
    """License tier enum."""
