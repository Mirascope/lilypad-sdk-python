# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .projects.functions.function_public import FunctionPublic

__all__ = ["ProjectPublic"]


class ProjectPublic(BaseModel):
    created_at: datetime

    name: str

    uuid: str

    functions: Optional[List[FunctionPublic]] = None
