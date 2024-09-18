# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .call_public_with_prompt_version import CallPublicWithPromptVersion

__all__ = ["CallListResponse"]

CallListResponse: TypeAlias = List[CallPublicWithPromptVersion]
