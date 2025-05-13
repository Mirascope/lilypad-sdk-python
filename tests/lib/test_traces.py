import inspect
from typing import Any, Callable, Coroutine
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from lilypad.lib.spans import Span
from lilypad.lib.traces import (
    Trace,
    Annotation,
    AsyncTrace,
    trace,
    clear_registry,
    enable_recording,
    disable_recording,
    get_decorated_functions,
)


def test_annotation_model():
    # Test creating an annotation
    annotation = Annotation(
        type="manual",  # EvaluationType: 'manual', 'verified', or 'edited'
        data={"content": "Test annotation"},
        label="pass",
        reasoning="This is a test annotation",
    )

    # Verify fields
    assert annotation.type == "manual"
    assert annotation.data == {"content": "Test annotation"}
    assert annotation.label == "pass"
    assert annotation.reasoning == "This is a test annotation"

    # Test model validation
    annotation_dict = annotation.model_dump()
    assert annotation_dict["type"] == "manual"
    assert annotation_dict["data"] == {"content": "Test annotation"}
    assert annotation_dict["label"] == "pass"
    assert annotation_dict["reasoning"] == "This is a test annotation"


# Test Trace class
@patch("lilypad.lib.traces.get_sync_client")
@patch("lilypad.lib.traces.get_settings")
def test_trace_get_span_uuid(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    # Create a trace
    trace = Trace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    span_uuid = trace._get_span_uuid(mock_client)

    mock_client.projects.functions.spans.list.assert_called_once_with(
        project_uuid="test-project", function_uuid="func-uuid"
    )
    assert span_uuid == "test-uuid"


@patch("lilypad.lib.traces.get_sync_client")
@patch("lilypad.lib.traces.get_settings")
def test_trace_annotate(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_settings.return_value.api_key = "test-api-key"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    trace = Trace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    annotation1 = Annotation(type="manual", data={"content": "Annotation 1"}, label="pass", reasoning="Reasoning 1")
    annotation2 = Annotation(type="manual", data={"content": "Annotation 2"}, label="fail", reasoning="Reasoning 2")

    trace.annotate(annotation1, annotation2)

    mock_client.ee.projects.annotations.create.assert_called_once()
    call_args = mock_client.ee.projects.annotations.create.call_args[1]
    assert call_args["project_uuid"] == "test-project"
    assert len(call_args["body"]) == 2
    assert call_args["body"][0]["type"] == "manual"
    assert call_args["body"][0]["data"]["content"] == "Annotation 1"
    assert call_args["body"][0]["label"] == "pass"
    assert call_args["body"][0]["reasoning"] == "Reasoning 1"
    assert call_args["body"][1]["data"]["content"] == "Annotation 2"
    assert call_args["body"][1]["label"] == "fail"
    assert call_args["body"][1]["reasoning"] == "Reasoning 2"


@patch("lilypad.lib.traces.get_sync_client")
@patch("lilypad.lib.traces.get_settings")
def test_trace_assign(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_settings.return_value.api_key = "test-api-key"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    # Create a trace
    trace = Trace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    trace.assign("user1@example.com", "user2@example.com")

    mock_client.ee.projects.annotations.create.assert_called_once()
    call_args = mock_client.ee.projects.annotations.create.call_args[1]
    assert call_args["project_uuid"] == "test-project"
    assert len(call_args["body"]) == 1
    assert call_args["body"][0]["assignee_email"] == ["user1@example.com", "user2@example.com"]
    assert call_args["body"][0]["function_uuid"] == "func-uuid"
    assert call_args["body"][0]["project_uuid"] == "test-project"
    assert call_args["body"][0]["span_uuid"] == "test-uuid"


@patch("lilypad.lib.traces.get_sync_client")
@patch("lilypad.lib.traces.get_settings")
def test_trace_tag(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_settings.return_value.api_key = "test-api-key"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    trace = Trace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    trace.tag("tag1", "tag2")

    mock_client.projects.spans.update_tags.assert_called_once_with(span_uuid="test-uuid", tags_by_name=["tag1", "tag2"])


@pytest.mark.asyncio
@patch("lilypad.lib.traces.get_async_client")
@patch("lilypad.lib.traces.get_settings")
async def test_async_trace_get_span_uuid(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    trace = AsyncTrace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    span_uuid = await trace._get_span_uuid(mock_client)

    mock_client.projects.functions.spans.list.assert_called_once_with(
        project_uuid="test-project", function_uuid="func-uuid"
    )
    assert span_uuid == "test-uuid"


@pytest.mark.asyncio
@patch("lilypad.lib.traces.get_async_client")
@patch("lilypad.lib.traces.get_settings")
async def test_async_trace_annotate(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_settings.return_value.api_key = "test-api-key"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    trace = AsyncTrace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    annotation1 = Annotation(type="manual", data={"content": "Annotation 1"}, label="pass", reasoning="Reasoning 1")
    annotation2 = Annotation(type="manual", data={"content": "Annotation 2"}, label="fail", reasoning="Reasoning 2")

    await trace.annotate(annotation1, annotation2)

    mock_client.ee.projects.annotations.create.assert_called_once()
    call_args = mock_client.ee.projects.annotations.create.call_args[1]
    assert call_args["project_uuid"] == "test-project"
    assert len(call_args["body"]) == 2
    assert call_args["body"][0]["type"] == "manual"
    assert call_args["body"][0]["data"]["content"] == "Annotation 1"
    assert call_args["body"][0]["label"] == "pass"
    assert call_args["body"][0]["reasoning"] == "Reasoning 1"
    assert call_args["body"][1]["data"]["content"] == "Annotation 2"
    assert call_args["body"][1]["label"] == "fail"
    assert call_args["body"][1]["reasoning"] == "Reasoning 2"


@pytest.mark.asyncio
@patch("lilypad.lib.traces.get_async_client")
@patch("lilypad.lib.traces.get_settings")
async def test_async_trace_assign(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_settings.return_value.api_key = "test-api-key"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    trace = AsyncTrace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    await trace.assign("user1@example.com", "user2@example.com")

    mock_client.ee.projects.annotations.create.assert_called_once()
    call_args = mock_client.ee.projects.annotations.create.call_args[1]
    assert call_args["project_uuid"] == "test-project"
    assert len(call_args["body"]) == 1
    assert call_args["body"][0]["assignee_email"] == ["user1@example.com", "user2@example.com"]
    assert call_args["body"][0]["function_uuid"] == "func-uuid"
    assert call_args["body"][0]["project_uuid"] == "test-project"
    assert call_args["body"][0]["span_uuid"] == "test-uuid"


@pytest.mark.asyncio
@patch("lilypad.lib.traces.get_async_client")
@patch("lilypad.lib.traces.get_settings")
async def test_async_trace_tag(mock_get_settings, mock_get_client):
    mock_settings = MagicMock()
    mock_settings.return_value.project_id = "test-project"
    mock_settings.return_value.api_key = "test-api-key"
    mock_get_settings.return_value = mock_settings.return_value

    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client
    mock_client.projects.functions.spans.list.return_value = [{"span_id": "12345", "uuid": "test-uuid"}]

    trace = AsyncTrace(response="test_response", span_id=12345, function_uuid="func-uuid")
    trace.formated_span_id = "12345"

    await trace.tag("tag1", "tag2")

    mock_client.projects.spans.update_tags.assert_called_once_with(span_uuid="test-uuid", tags_by_name=["tag1", "tag2"])


def test_registry_functions():
    clear_registry()

    enable_recording()
    assert enable_recording() is None
    assert disable_recording() is None

    functions = get_decorated_functions()
    assert isinstance(functions, dict)
    assert len(functions) == 0

    functions = get_decorated_functions("test_decorator")
    assert isinstance(functions, dict)
    assert "test_decorator" in functions
    assert isinstance(functions["test_decorator"], list)
    assert len(functions["test_decorator"]) == 0


def test_trace_decorator_sync():
    @trace()
    def test_function(x, y):
        return x + y

    result = test_function(1, 2)

    assert result == 3

    functions = get_decorated_functions("trace")
    assert len(functions) > 0


@pytest.mark.asyncio
async def test_trace_decorator_async():
    @trace()
    async def test_async_function(x, y):
        return x + y

    result = await test_async_function(1, 2)

    assert result == 3

    functions = get_decorated_functions("trace")
    assert len(functions) > 0


def test_trace_decorator_with_context():
    @trace()
    def test_function_with_context(trace_ctx, x, y):
        assert isinstance(trace_ctx, Span)
        return x + y

    result = test_function_with_context(1, 2)

    assert result == 3


@pytest.mark.asyncio
async def test_trace_decorator_async_with_context():
    @trace()
    async def test_async_function_with_context(trace_ctx, x, y):
        assert isinstance(trace_ctx, Span)
        return x + y

    result = await test_async_function_with_context(1, 2)

    assert result == 3
