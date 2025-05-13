import pytest
from httpx import HTTPError, RequestError, TimeoutException

from lilypad.lib.exceptions import (
    LicenseError,
    LilypadTimeout,
    LilypadException,
    LilypadHTTPError,
    LilypadValueError,
    RemoteFunctionError,
    LilypadNotFoundError,
    LilypadRateLimitError,
    LilypadRequestException,
    LilypadFileNotFoundError,
    LilypadAPIConnectionError,
    LilypadPaymentRequiredError,
)


def test_lilypad_exception():
    exc = LilypadException("Test message")
    assert str(exc) == "Test message"
    assert isinstance(exc, Exception)


def test_license_error():
    exc = LicenseError("License expired")
    assert str(exc) == "License expired"
    assert isinstance(exc, LilypadException)


def test_remote_function_error():
    exc = RemoteFunctionError("Function call failed")
    assert str(exc) == "Function call failed"
    assert isinstance(exc, LilypadException)


def test_lilypad_not_found_error():
    exc = LilypadNotFoundError("Resource not found")
    assert str(exc) == "Resource not found"
    assert isinstance(exc, LilypadException)
    assert exc.status_code == 404


def test_lilypad_rate_limit_error():
    exc = LilypadRateLimitError("Rate limit exceeded")
    assert str(exc) == "Rate limit exceeded"
    assert isinstance(exc, LilypadException)
    assert exc.status_code == 429


def test_lilypad_api_connection_error():
    exc = LilypadAPIConnectionError("Connection failed")
    assert str(exc) == "Connection failed"
    assert isinstance(exc, LilypadException)


def test_lilypad_value_error():
    exc = LilypadValueError("Invalid value")
    assert str(exc) == "Invalid value"
    assert isinstance(exc, LilypadException)


def test_lilypad_file_not_found_error():
    exc = LilypadFileNotFoundError("File not found")
    assert str(exc) == "File not found"
    assert isinstance(exc, LilypadException)


def test_lilypad_http_error():
    exc = LilypadHTTPError("HTTP error")
    assert str(exc) == "HTTP error"
    assert isinstance(exc, LilypadException)
    assert isinstance(exc, HTTPError)


def test_lilypad_request_exception():
    exc = LilypadRequestException("Request failed")
    assert str(exc) == "Request failed"
    assert isinstance(exc, LilypadException)
    assert isinstance(exc, RequestError)


def test_lilypad_timeout():
    exc = LilypadTimeout("Request timed out")
    assert str(exc) == "Request timed out"
    assert isinstance(exc, LilypadException)
    assert isinstance(exc, TimeoutException)


def test_lilypad_payment_required_error():
    exc = LilypadPaymentRequiredError("Payment required")
    assert str(exc) == "Payment required"
    assert isinstance(exc, LilypadException)
    assert exc.status_code == 402
