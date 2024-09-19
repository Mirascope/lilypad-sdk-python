# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .prompt_version_public import PromptVersionPublic

__all__ = ["CallPublicWithPromptVersion"]


class CallPublicWithPromptVersion(BaseModel):
    id: int

    input: str

    output: str

    prompt_version: PromptVersionPublic
    """Prompt Version public model."""

    created_at: Optional[datetime] = None

    prompt_version_id: Optional[int] = None
