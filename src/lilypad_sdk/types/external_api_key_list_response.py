# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .external_api_key_public import ExternalAPIKeyPublic

__all__ = ["ExternalAPIKeyListResponse"]

ExternalAPIKeyListResponse: TypeAlias = List[ExternalAPIKeyPublic]
