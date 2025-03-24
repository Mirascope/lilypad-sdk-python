# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["SettingRetrieveResponse"]


class SettingRetrieveResponse(BaseModel):
    environment: str

    experimental: bool

    github_client_id: str

    google_client_id: str

    remote_api_url: str

    remote_client_url: str
