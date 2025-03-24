# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .ee.projects.generation_public import GenerationPublic

__all__ = ["ProjectPublic"]


class ProjectPublic(BaseModel):
    created_at: datetime

    name: str

    uuid: str

    generations: Optional[List[GenerationPublic]] = None
