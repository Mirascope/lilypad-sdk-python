# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserOrganizationCreateParams"]


class UserOrganizationCreateParams(TypedDict, total=False):
    token: Required[str]
