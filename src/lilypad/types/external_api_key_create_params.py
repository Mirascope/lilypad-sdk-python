# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalAPIKeyCreateParams"]


class ExternalAPIKeyCreateParams(TypedDict, total=False):
    api_key: Required[str]

    service_name: Required[str]
