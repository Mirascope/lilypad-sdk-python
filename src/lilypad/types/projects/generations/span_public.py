# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel
from ...ee.projects.label import Label
from ...ee.projects.evaluation_type import EvaluationType
from ...ee.projects.common_call_params import CommonCallParams

__all__ = ["SpanPublic", "Annotation", "Function", "FunctionDependencies"]


class Annotation(BaseModel):
    organization_uuid: str

    assigned_to: Optional[str] = None

    created_at: Optional[datetime] = None

    data: Optional[object] = None

    function_uuid: Optional[str] = None

    label: Optional[Label] = None
    """Label enum"""

    project_uuid: Optional[str] = None

    reasoning: Optional[str] = None

    span_uuid: Optional[str] = None

    type: Optional[EvaluationType] = None
    """Evaluation type enum"""

    uuid: Optional[str] = None


class FunctionDependencies(BaseModel):
    extras: Optional[List[str]] = None

    version: str


class Function(BaseModel):
    code: str

    hash: str

    name: str

    signature: str

    uuid: str

    archived: Optional[datetime] = None

    arg_types: Optional[Dict[str, str]] = None

    call_params: Optional[CommonCallParams] = None
    """Common parameters shared across LLM providers.

    Note: Each provider may handle these parameters differently or not support them
    at all. Please check provider-specific documentation for parameter support and
    behavior.

    Attributes: temperature: Controls randomness in the output (0.0 to 1.0).
    max_tokens: Maximum number of tokens to generate. top_p: Nucleus sampling
    parameter (0.0 to 1.0). frequency_penalty: Penalizes frequent tokens (-2.0 to
    2.0). presence_penalty: Penalizes tokens based on presence (-2.0 to 2.0). seed:
    Random seed for reproducibility. stop: Stop sequence(s) to end generation.
    """

    custom_id: Optional[str] = None

    dependencies: Optional[Dict[str, FunctionDependencies]] = None

    is_versioned: Optional[bool] = None

    model: Optional[str] = None

    project_uuid: Optional[str] = None

    prompt_template: Optional[str] = None

    provider: Optional[str] = None

    version_num: Optional[int] = None


class SpanPublic(BaseModel):
    annotations: List[Annotation]

    child_spans: List["SpanPublic"]

    created_at: datetime

    project_uuid: str

    scope: Literal["lilypad", "llm"]
    """Instrumentation Scope name of the span"""

    span_id: str

    uuid: str

    cost: Optional[float] = None

    data: Optional[object] = None

    display_name: Optional[str] = None

    duration_ms: Optional[float] = None

    function: Optional[Function] = None
    """Function public model."""

    function_uuid: Optional[str] = None

    input_tokens: Optional[float] = None

    output_tokens: Optional[float] = None

    parent_span_id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function", "trace"]] = None
    """Span type"""

    version: Optional[int] = None


if PYDANTIC_V2:
    SpanPublic.model_rebuild()
    Annotation.model_rebuild()
    Function.model_rebuild()
    FunctionDependencies.model_rebuild()
else:
    SpanPublic.update_forward_refs()  # type: ignore
    Annotation.update_forward_refs()  # type: ignore
    Function.update_forward_refs()  # type: ignore
    FunctionDependencies.update_forward_refs()  # type: ignore
