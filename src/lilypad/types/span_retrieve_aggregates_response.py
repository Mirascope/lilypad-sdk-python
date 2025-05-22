# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .projects.aggregate_metrics import AggregateMetrics

__all__ = ["SpanRetrieveAggregatesResponse"]

SpanRetrieveAggregatesResponse: TypeAlias = List[AggregateMetrics]
