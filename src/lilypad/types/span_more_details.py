# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "SpanMoreDetails",
    "Message",
    "MessageContent",
    "MessageContent_AudioPart",
    "MessageContent_TextPart",
    "MessageContent_ImagePart",
    "MessageContent_ToolCall",
    "Event",
]


class MessageContent_AudioPart(BaseModel):
    audio: str

    media_type: str

    type: Literal["audio"]


class MessageContent_TextPart(BaseModel):
    text: str

    type: Literal["text"]


class MessageContent_ImagePart(BaseModel):
    detail: Optional[str] = None

    image: str

    media_type: str

    type: Literal["image"]


class MessageContent_ToolCall(BaseModel):
    arguments: object

    name: str

    type: Literal["tool_call"]


MessageContent: TypeAlias = Union[
    MessageContent_AudioPart, MessageContent_TextPart, MessageContent_ImagePart, MessageContent_ToolCall
]


class Message(BaseModel):
    content: List[MessageContent]

    role: str


class Event(BaseModel):
    message: str

    name: str

    timestamp: datetime

    type: str


class SpanMoreDetails(BaseModel):
    data: object

    display_name: str

    messages: List[Message]

    model: str

    provider: str

    uuid: str

    arg_values: Optional[object] = None

    code: Optional[str] = None

    cost: Optional[float] = None

    duration_ms: Optional[float] = None

    events: Optional[List[Event]] = None

    function_uuid: Optional[str] = None

    input_tokens: Optional[float] = None

    output: Optional[str] = None

    output_tokens: Optional[float] = None

    project_uuid: Optional[str] = None

    signature: Optional[str] = None

    status: Optional[str] = None

    template: Optional[str] = None
