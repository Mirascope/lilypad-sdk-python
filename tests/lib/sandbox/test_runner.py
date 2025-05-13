"""Function-style tests for SandboxRunner."""

from unittest.mock import Mock

import pytest

from lilypad.lib._utils import Closure
from lilypad.lib.sandbox.runner import SandboxRunner, DependencyError


class MockSandboxRunner(SandboxRunner):
    """Mock implementation of SandboxRunner used in tests."""

    def execute_function(self, closure, *args, **kwargs):
        return {"result": "mock_result"}


def test_init():
    """Verify that SandboxRunner initializes with or without an environment."""
    runner = MockSandboxRunner()
    assert runner.environment == {}

    env = {"KEY": "VALUE"}
    runner = MockSandboxRunner(environment=env)
    assert runner.environment == env


@pytest.mark.parametrize(
    "signature, expected",
    [
        ("def test_func():\n    pass", False),
        ("async def test_func():\n    pass", True),
    ],
)
def test_is_async_func(signature, expected):
    """Ensure that _is_async_func detects asynchronous functions correctly."""
    closure = Mock(spec=Closure)
    closure.signature = signature
    assert SandboxRunner._is_async_func(closure) is expected


def test_parse_execution_result_success():
    """Return value is parsed correctly when the subprocess exits successfully."""
    stdout = b'{"result": "success"}'
    stderr = b""
    returncode = 0

    result = SandboxRunner.parse_execution_result(stdout, stderr, returncode)
    assert result == {"result": "success"}


def test_parse_execution_result_dependency_error():
    """DependencyError is raised and populated with details from the JSON payload."""
    stdout = (
        b'{"error_type": "ImportError", '
        b'"error_message": "No module named test", '
        b'"is_dependency_error": true, '
        b'"module_name": "test"}'
    )
    stderr = b""
    returncode = 1

    with pytest.raises(DependencyError) as excinfo:
        SandboxRunner.parse_execution_result(stdout, stderr, returncode)

    err = excinfo.value
    assert err.message == "No module named test"
    assert err.module_name == "test"
    assert err.error_class == "ImportError"


def test_parse_execution_result_runtime_error():
    """RuntimeError is raised and its message contains stdout and stderr."""
    stdout = b"Invalid JSON"
    stderr = b"Error message"
    returncode = 1

    with pytest.raises(RuntimeError) as excinfo:
        SandboxRunner.parse_execution_result(stdout, stderr, returncode)

    msg = str(excinfo.value)
    assert "Process exited with non-zero status" in msg
    assert "Invalid JSON" in msg
    assert "Error message" in msg


def _create_closure(name, code, signature, dependencies):
    """Return a mocked Closure with the specified attributes."""
    closure = Mock(spec=Closure)
    closure.name = name
    closure.code = code
    closure.signature = signature
    closure.dependencies = dependencies
    return closure


def test_generate_script_sync():
    """generate_script embeds a synchronous function, its call, and dependencies."""
    closure = _create_closure(
        "test_func",
        "def test_func(x, y):\n    return x + y",
        "def test_func(x, y):\n    return x + y",
        {"package1": {"version": "1.0.0", "extras": []}},
    )

    script = SandboxRunner.generate_script(closure, 1, 2)

    assert "def test_func(x, y):" in script
    assert "return x + y" in script
    assert "test_func(*(1, 2), **{})" in script
    assert '"package1==1.0.0"' in script


def test_generate_script_async():
    """generate_script embeds an asynchronous function, its awaited call, and dependencies."""
    closure = _create_closure(
        "test_func",
        "async def test_func(x, y):\n    return x + y",
        "async def test_func(x, y):\n    return x + y",
        {"package1": {"version": "1.0.0", "extras": []}},
    )

    script = SandboxRunner.generate_script(closure, 1, 2)

    assert "async def test_func(x, y):" in script
    assert "return x + y" in script
    assert "await test_func(*(1, 2), **{})" in script
    assert '"package1==1.0.0"' in script
    assert "import asyncio" in script


def test_generate_script_with_extras():
    """Dependencies with extras are formatted correctly in the generated script."""
    closure = _create_closure(
        "test_func",
        "def test_func():\n    pass",
        "def test_func():\n    pass",
        {"package1": {"version": "1.0.0", "extras": ["extra1", "extra2"]}},
    )

    script = SandboxRunner.generate_script(closure)

    assert '"package1[extra1,extra2]==1.0.0"' in script


def test_generate_script_with_custom_result():
    """Custom result expressions are inserted into the generated script."""
    closure = _create_closure(
        "test_func",
        "def test_func():\n    return 42",
        "def test_func():\n    return 42",
        {},
    )

    custom_result = {"custom_key": "result * 2"}
    script = SandboxRunner.generate_script(closure, custom_result=custom_result)

    assert '"custom_key": (result * 2)' in script


def test_generate_script_with_actions():
    """Pre-actions and after-actions are included in the generated script."""
    closure = _create_closure(
        "test_func",
        "def test_func():\n    return 42",
        "def test_func():\n    return 42",
        {},
    )

    pre_actions = ["print('Before')"]
    after_actions = ["print('After')"]
    script = SandboxRunner.generate_script(closure, pre_actions=pre_actions, after_actions=after_actions)

    assert "print('Before')" in script
    assert "print('After')" in script
