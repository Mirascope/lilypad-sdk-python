# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .user_role import UserRole

__all__ = ["UserOrganizationUpdateUserOrganizationParams"]


class UserOrganizationUpdateUserOrganizationParams(TypedDict, total=False):
    role: Required[UserRole]
    """User role enum."""
