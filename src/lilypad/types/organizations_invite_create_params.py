# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationsInviteCreateParams"]


class OrganizationsInviteCreateParams(TypedDict, total=False):
    email: Required[str]

    invited_by: Required[str]

    token: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    organization_uuid: Optional[str]

    resend_email_id: Optional[str]
