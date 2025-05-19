# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .time_frame import TimeFrame

__all__ = ["SpanRetrieveAggregatesParams"]


class SpanRetrieveAggregatesParams(TypedDict, total=False):
    time_frame: Required[TimeFrame]
    """Timeframe for aggregation"""
