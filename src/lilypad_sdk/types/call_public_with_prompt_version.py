# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallPublicWithPromptVersion", "PromptVersion"]


class PromptVersion(BaseModel):
    id: int

    function_name: str

    prompt_template: str

    previous_version_id: Optional[int] = None

    project_id: Optional[int] = None


class CallPublicWithPromptVersion(BaseModel):
    id: int

    input: str

    output: str

    prompt_version: PromptVersion
    """Prompt Version public model."""

    created_at: Optional[datetime] = None

    prompt_version_id: Optional[int] = None
