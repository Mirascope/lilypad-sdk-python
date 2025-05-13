"""Tests for OpenTelemetry utility classes and functions."""

from unittest.mock import Mock, AsyncMock, create_autospec

import httpx
import pytest
from opentelemetry.trace import StatusCode

from lilypad.lib._opentelemetry._utils import (
    ChoiceBuffer,
    ChunkHandler,
    StreamWrapper,
    ToolCallBuffer,
    AsyncStreamWrapper,
    set_server_address_and_port,
)


# Define concrete protocol implementations for mocking
class MockStreamProtocol:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()

    def close(self):
        pass


class MockAsyncStreamProtocol:
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    def __aiter__(self):
        return self

    async def __anext__(self):
        raise NotImplementedError

    async def aclose(self):
        pass


@pytest.fixture
def mock_span():
    return Mock()


@pytest.fixture
def mock_stream():
    # Create a stream mock that implements the iterator protocol
    stream = create_autospec(MockStreamProtocol)

    chunks = ["chunk1", "chunk2"]
    iter_obj = iter(chunks)

    stream.__iter__ = Mock(return_value=iter_obj)
    stream.__next__ = Mock(side_effect=iter_obj.__next__)
    stream.close = Mock()

    return stream


@pytest.fixture
def mock_async_stream():
    stream = create_autospec(MockAsyncStreamProtocol)
    chunks = ["chunk1", "chunk2"]
    index = 0

    # Mock __aiter__ to return self
    stream.__aiter__ = AsyncMock(return_value=stream)

    # Mock __anext__ to return chunks and eventually raise StopAsyncIteration
    async def async_next():
        nonlocal index
        if index >= len(chunks):
            raise StopAsyncIteration
        chunk = chunks[index]
        index += 1
        return chunk

    stream.__anext__ = AsyncMock(side_effect=async_next)
    stream.__aenter__ = AsyncMock(return_value=stream)
    stream.__aexit__ = AsyncMock(return_value=None)
    stream.aclose = AsyncMock()

    return stream


@pytest.fixture
def mock_metadata():
    return Mock()


@pytest.fixture
def mock_chunk_handler():
    handler = Mock()
    handler.extract_metadata = Mock()
    handler.process_chunk = Mock()
    return handler


def test_choice_buffer():
    buffer = ChoiceBuffer(0)
    assert buffer.index == 0
    assert buffer.finish_reason is None
    assert buffer.text_content == []
    assert buffer.tool_calls_buffers == []

    buffer.append_text_content("test")
    assert buffer.text_content == ["test"]


def test_choice_buffer_append_tool_call():
    buffer = ChoiceBuffer(0)

    tool_call = Mock()
    tool_call.index = 0
    tool_call.id = "tool-call-id"
    tool_call.function = Mock()
    tool_call.function.name = "test_function"
    tool_call.function.arguments = {"arg": "value"}

    buffer.append_tool_call(tool_call)

    assert len(buffer.tool_calls_buffers) == 1
    assert buffer.tool_calls_buffers[0].tool_call_id == "tool-call-id"
    assert buffer.tool_calls_buffers[0].function_name == "test_function"
    assert buffer.tool_calls_buffers[0].arguments == [{"arg": "value"}]

    tool_call2 = Mock()
    tool_call2.index = 1
    tool_call2.id = "tool-call-id-2"
    tool_call2.function = Mock()
    tool_call2.function.name = "test_function_2"
    tool_call2.function.arguments = {"arg2": "value2"}

    buffer.append_tool_call(tool_call2)

    assert len(buffer.tool_calls_buffers) == 2
    assert buffer.tool_calls_buffers[1].tool_call_id == "tool-call-id-2"
    assert buffer.tool_calls_buffers[1].function_name == "test_function_2"
    assert buffer.tool_calls_buffers[1].arguments == [{"arg2": "value2"}]


def test_tool_call_buffer():
    buffer = ToolCallBuffer(0, "test-id", "test-function")
    assert buffer.index == 0
    assert buffer.tool_call_id == "test-id"
    assert buffer.function_name == "test-function"
    assert buffer.arguments == []

    buffer.append_arguments({"arg": "value"})
    assert buffer.arguments == [{"arg": "value"}]


def test_stream_wrapper(mock_span, mock_stream, mock_metadata, mock_chunk_handler):
    wrapper = StreamWrapper(mock_span, mock_stream, mock_metadata, mock_chunk_handler)
    wrapper.setup()

    assert wrapper._span_started
    wrapper.cleanup()
    assert not wrapper._span_started
    mock_span.end.assert_called_once()


def test_stream_wrapper_iterator(mock_span, mock_stream, mock_metadata, mock_chunk_handler):
    wrapper = StreamWrapper(mock_span, mock_stream, mock_metadata, mock_chunk_handler)
    chunks = list(wrapper)

    assert chunks == ["chunk1", "chunk2"]
    assert mock_chunk_handler.process_chunk.call_count == 2


def test_stream_error_handling(mock_span, mock_stream, mock_metadata, mock_chunk_handler):
    error = Exception("Test error")
    stream = create_autospec(MockStreamProtocol)
    stream.__next__.side_effect = error

    wrapper = StreamWrapper(mock_span, stream, mock_metadata, mock_chunk_handler)

    with pytest.raises(Exception):  # noqa: B017
        list(wrapper)

    mock_span.set_status.assert_called_once()
    mock_span.end.assert_called_once()


@pytest.mark.asyncio
async def test_async_stream_wrapper(mock_span, mock_async_stream, mock_metadata, mock_chunk_handler):
    wrapper = AsyncStreamWrapper(mock_span, mock_async_stream, mock_metadata, mock_chunk_handler)

    chunks = []
    async with wrapper as w:
        assert w._span_started
        async for chunk in w:
            chunks.append(chunk)

    assert not wrapper._span_started
    assert chunks == ["chunk1", "chunk2"]
    assert mock_chunk_handler.process_chunk.call_count == 2
    mock_span.end.assert_called_once()


@pytest.mark.asyncio
async def test_async_stream_error_handling(mock_span, mock_async_stream, mock_metadata, mock_chunk_handler):
    """Test that errors during iteration are handled correctly"""
    error = Exception("Test error")
    stream = create_autospec(MockAsyncStreamProtocol)

    # Setup async mock behavior
    stream.__anext__ = AsyncMock(side_effect=error)
    stream.__aiter__ = AsyncMock(return_value=stream)
    stream.__aenter__ = AsyncMock(return_value=stream)
    stream.__aexit__ = AsyncMock(return_value=None)

    wrapper = AsyncStreamWrapper(mock_span, stream, mock_metadata, mock_chunk_handler)

    with pytest.raises(Exception) as exc_info:
        async with wrapper as w:
            await anext(w)

    # Verify the error handling
    assert exc_info.value is error
    assert mock_span.set_status.called
    status_call = mock_span.set_status.call_args[0][0]
    assert status_call.status_code == StatusCode.ERROR
    assert status_call.description == str(error)
    mock_span.end.assert_called_once()


@pytest.mark.asyncio
async def test_async_stream_normal_case(mock_span, mock_async_stream, mock_metadata, mock_chunk_handler):
    """Test normal async stream operation"""
    stream = create_autospec(MockAsyncStreamProtocol)

    stream.__aenter__ = AsyncMock(return_value=stream)
    stream.__aexit__ = AsyncMock()
    stream.__aiter__ = AsyncMock(return_value=stream)
    stream.__anext__ = AsyncMock(side_effect=StopAsyncIteration)
    stream.aclose = AsyncMock()

    wrapper = AsyncStreamWrapper(mock_span, stream, mock_metadata, mock_chunk_handler)

    async with wrapper as w:
        async for _ in w:
            pass  # Normal operation, no items

    # Verify normal cleanup
    mock_span.end.assert_called_once()


class ConcreteChunkHandler:
    """A concrete implementation of the ChunkHandler protocol for testing."""

    def __init__(self):
        self.metadata_calls = []
        self.process_calls = []

    def extract_metadata(self, chunk, metadata):
        """Extract metadata from chunk and update StreamMetadata."""
        self.metadata_calls.append((chunk, metadata))
        metadata.test_field = f"metadata-{chunk}"

    def process_chunk(self, chunk, buffers):
        """Process chunk and update choice buffers."""
        self.process_calls.append((chunk, buffers))
        if not buffers:
            buffers.append(ChoiceBuffer(0))
        buffers[0].append_text_content(f"processed-{chunk}")


def test_chunk_handler():
    """Test the ChunkHandler protocol with a concrete implementation."""
    handler = ConcreteChunkHandler()

    metadata = Mock()
    handler.extract_metadata("test-chunk", metadata)
    assert handler.metadata_calls == [("test-chunk", metadata)]
    assert metadata.test_field == "metadata-test-chunk"

    buffers = []
    handler.process_chunk("test-chunk", buffers)
    assert len(buffers) == 1
    assert buffers[0].text_content == ["processed-test-chunk"]

    existing_buffer = ChoiceBuffer(1)
    buffers = [existing_buffer]
    handler.process_chunk("another-chunk", buffers)
    assert len(buffers) == 1
    assert buffers[0].text_content == ["processed-another-chunk"]

    assert len(handler.process_calls) == 2
    assert handler.process_calls[0][0] == "test-chunk"
    assert handler.process_calls[1][0] == "another-chunk"


def test_chunk_handler_with_stream_wrapper():
    """Test using a ChunkHandler with StreamWrapper."""
    handler = ConcreteChunkHandler()

    stream = create_autospec(MockStreamProtocol)
    chunks = ["chunk1", "chunk2"]
    iter_obj = iter(chunks)
    stream.__iter__ = Mock(return_value=iter_obj)
    stream.__next__ = Mock(side_effect=iter_obj.__next__)

    span = Mock()
    metadata = Mock()

    wrapper = StreamWrapper(span, stream, metadata, handler)

    result = list(wrapper)

    assert result == chunks
    assert len(handler.metadata_calls) == 2
    assert handler.metadata_calls[0][0] == "chunk1"
    assert handler.metadata_calls[1][0] == "chunk2"
    assert len(handler.process_calls) == 2
    assert handler.process_calls[0][0] == "chunk1"
    assert handler.process_calls[1][0] == "chunk2"

    assert metadata.test_field == "metadata-chunk2"  # Last value

    buffers = wrapper.choice_buffers
    assert len(buffers) == 1
    assert buffers[0].text_content == ["processed-chunk1", "processed-chunk2"]


def test_set_server_address_and_port():
    """Test setting server address and port from different URL types."""
    client1 = Mock()
    client1._client = Mock()
    client1._client.base_url = httpx.URL("https://api.example.com")

    attributes1 = {}
    set_server_address_and_port(client1, attributes1)
    assert attributes1["server.address"] == "api.example.com"
    assert "server.port" not in attributes1  # Default HTTPS port should be omitted

    client2 = Mock()
    client2._client = Mock()
    client2._client.base_url = httpx.URL("https://api.example.com:8443")

    attributes2 = {}
    set_server_address_and_port(client2, attributes2)
    assert attributes2["server.address"] == "api.example.com"
    assert attributes2["server.port"] == 8443

    client3 = Mock()
    client3._client = Mock()
    client3._client.base_url = "https://api.example.org"

    attributes3 = {}
    set_server_address_and_port(client3, attributes3)
    assert attributes3["server.address"] == "api.example.org"
    assert "server.port" not in attributes3

    client4 = Mock()
    client4._client = Mock()
    client4._client.base_url = "https://api.example.org:9000"

    attributes4 = {}
    set_server_address_and_port(client4, attributes4)
    assert attributes4["server.address"] == "api.example.org"
    assert attributes4["server.port"] == 9000

    client5 = Mock()
    client5._client = Mock()
    client5._client.base_url = None

    attributes5 = {}
    set_server_address_and_port(client5, attributes5)
    assert not attributes5  # Should be empty

    client6 = Mock()
    client6._client = None

    attributes6 = {}
    set_server_address_and_port(client6, attributes6)
    assert not attributes6
