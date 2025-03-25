# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .deployment_public import DeploymentPublic

__all__ = ["EnvironmentRetrieveDeploymentHistoryResponse"]

EnvironmentRetrieveDeploymentHistoryResponse: TypeAlias = List[DeploymentPublic]
