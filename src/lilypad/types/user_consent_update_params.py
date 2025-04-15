# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserConsentUpdateParams"]


class UserConsentUpdateParams(TypedDict, total=False):
    privacy_policy_accepted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    privacy_policy_version: Optional[str]

    tos_accepted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    tos_version: Optional[str]
