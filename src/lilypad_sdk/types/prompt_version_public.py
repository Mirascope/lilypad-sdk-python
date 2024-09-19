# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PromptVersionPublic"]


class PromptVersionPublic(BaseModel):
    id: int

    function_name: str

    prompt_template: str

    input_arguments: Optional[str] = None

    lexical_closure: Optional[str] = None

    previous_version_id: Optional[int] = None

    version_hash: Optional[str] = None
