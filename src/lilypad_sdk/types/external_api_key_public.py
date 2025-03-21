# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ExternalAPIKeyPublic"]


class ExternalAPIKeyPublic(BaseModel):
    masked_api_key: str
    """Partially masked API key"""

    service_name: str
