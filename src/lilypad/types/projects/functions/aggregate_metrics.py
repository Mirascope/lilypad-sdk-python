# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AggregateMetrics"]


class AggregateMetrics(BaseModel):
    average_duration_ms: float

    end_date: Optional[datetime] = None

    function_uuid: Optional[str] = None

    span_count: int

    start_date: Optional[datetime] = None

    total_cost: float

    total_input_tokens: float

    total_output_tokens: float
