# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["AnnotationGetMetricsResponse"]


class AnnotationGetMetricsResponse(BaseModel):
    function_uuid: str

    success_count: int

    total_count: int
