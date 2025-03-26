# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..environment_public import EnvironmentPublic
from .functions.function_public import FunctionPublic

__all__ = ["DeploymentPublic"]


class DeploymentPublic(BaseModel):
    environment_uuid: str

    function_uuid: str

    organization_uuid: str

    uuid: str

    activated_at: Optional[datetime] = None
    """Timestamp when the deployment was activated."""

    environment: Optional[EnvironmentPublic] = None
    """Environment public model."""

    function: Optional[FunctionPublic] = None
    """Function public model."""

    is_active: Optional[bool] = None

    notes: Optional[str] = None

    project_uuid: Optional[str] = None

    version_num: Optional[int] = None
