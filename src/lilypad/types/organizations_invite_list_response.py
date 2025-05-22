# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .organization_invite_public import OrganizationInvitePublic

__all__ = ["OrganizationsInviteListResponse"]

OrganizationsInviteListResponse: TypeAlias = List[OrganizationInvitePublic]
