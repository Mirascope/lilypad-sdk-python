# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookHandleResponse"]


class WebhookHandleResponse(BaseModel):
    status: Literal["success", "error", "ignored"]

    event: Optional[str] = None

    message: Optional[str] = None
