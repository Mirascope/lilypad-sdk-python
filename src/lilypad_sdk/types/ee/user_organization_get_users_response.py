# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..auth.user_public import UserPublic

__all__ = ["UserOrganizationGetUsersResponse"]

UserOrganizationGetUsersResponse: TypeAlias = List[UserPublic]
