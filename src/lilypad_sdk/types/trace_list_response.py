# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from .span_public import SpanPublic

__all__ = ["TraceListResponse"]

TraceListResponse: TypeAlias = List[SpanPublic]
