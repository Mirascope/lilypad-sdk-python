import logging
from unittest.mock import MagicMock, patch

from opentelemetry.trace import INVALID_SPAN_ID, INVALID_TRACE_ID

from lilypad.lib._configure import (
    CryptoIdGenerator,
    configure,
    lilypad_config,
    _JSONSpanExporter,
)


def test_crypto_id_generator():
    generator = CryptoIdGenerator()

    span_id = generator.generate_span_id()
    assert span_id != INVALID_SPAN_ID
    assert isinstance(span_id, int)

    trace_id = generator.generate_trace_id()
    assert trace_id != INVALID_TRACE_ID
    assert isinstance(trace_id, int)

    span_id2 = generator.generate_span_id()
    trace_id2 = generator.generate_trace_id()
    assert span_id != span_id2
    assert trace_id != trace_id2


@patch("lilypad.lib._configure._JSONSpanExporter._send_once")
def test_json_span_exporter_export(mock_send_once):
    exporter = _JSONSpanExporter()

    mock_span1 = MagicMock()
    mock_span1.name = "span1"
    mock_span1.context.span_id = 12345
    mock_span1.context.trace_id = 67890
    mock_span1.start_time = 1000000000
    mock_span1.end_time = 1000000100
    status_code_mock = MagicMock()
    status_code_mock.name = "UNSET"
    mock_span1.status.status_code = status_code_mock
    mock_span1.attributes = {"key1": "value1"}
    mock_span1.events = []
    mock_span1.links = []
    mock_span1.parent = None
    mock_span1.resource.to_json.return_value = "{}"
    mock_span1.instrumentation_scope = MagicMock()
    mock_span1.instrumentation_scope.name = "test_scope"
    mock_span1.instrumentation_scope.version = "1.0"
    mock_span1.instrumentation_scope.schema_url = ""
    mock_span1.instrumentation_scope.attributes = None

    mock_span2 = MagicMock()
    mock_span2.name = "span2"
    mock_span2.context.span_id = 54321
    mock_span2.context.trace_id = 9876
    mock_span2.start_time = 1000000200
    mock_span2.end_time = 1000000300
    status_code_mock2 = MagicMock()
    status_code_mock2.name = "ERROR"
    mock_span2.status.status_code = status_code_mock2
    mock_span2.attributes = {"key2": "value2"}
    mock_span2.events = []
    mock_span2.links = []
    mock_span2.parent = None
    mock_span2.resource.to_json.return_value = "{}"
    mock_span2.instrumentation_scope = MagicMock()
    mock_span2.instrumentation_scope.name = "test_scope"
    mock_span2.instrumentation_scope.version = "1.0"
    mock_span2.instrumentation_scope.schema_url = ""
    mock_span2.instrumentation_scope.attributes = None

    with patch.object(exporter, "_span_to_dict") as mock_span_to_dict:
        mock_span_to_dict.side_effect = lambda span: {
            "name": span.name,
            "span_id": span.context.span_id,
            "trace_id": span.context.trace_id,
            "attributes": span.attributes,
        }

        mock_send_once.return_value = []

        result = exporter.export([mock_span1, mock_span2])

        assert mock_span_to_dict.call_count == 2

        mock_send_once.assert_called_once()
        payload = mock_send_once.call_args[0][0]
        assert len(payload) == 2
        assert payload[0]["name"] == "span1"
        assert payload[0]["span_id"] == 12345
        assert payload[0]["trace_id"] == 67890
        assert payload[0]["attributes"]["key1"] == "value1"
        assert payload[1]["name"] == "span2"

        assert result.name == "SUCCESS"


@patch("lilypad.lib._configure._JSONSpanExporter._send_once")
def test_json_span_exporter_force_flush(mock_send_once):
    exporter = _JSONSpanExporter()

    result = exporter.force_flush()

    assert result is True


@patch("threading.Thread")
def test_json_span_exporter_shutdown(mock_thread):
    exporter = _JSONSpanExporter()
    exporter._worker = MagicMock()
    exporter._worker.is_alive.return_value = True

    exporter.shutdown()

    assert exporter._stop.is_set() is True

    exporter._worker.join.assert_called_once()


@patch("lilypad.lib._configure._current_settings")
def test_lilypad_config(mock_current_settings):
    original_settings = MagicMock()
    mock_token = MagicMock()
    mock_current_settings.get.return_value = original_settings
    mock_current_settings.set.return_value = mock_token

    temp_settings = MagicMock()
    temp_settings.api_key = "temp_key"
    temp_settings.project_id = "temp_project"

    original_settings.model_copy.return_value = temp_settings

    with lilypad_config(api_key="temp_key", project_id="temp_project"):
        mock_current_settings.set.assert_called_once()
        assert mock_current_settings.set.call_args[0][0].api_key == "temp_key"
        assert mock_current_settings.set.call_args[0][0].project_id == "temp_project"

    mock_current_settings.reset.assert_called_once_with(mock_token)
