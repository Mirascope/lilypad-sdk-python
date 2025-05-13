"""Function-style tests for DockerSandboxRunner."""

import io
import tarfile
from unittest.mock import Mock, MagicMock, patch

import pytest

from lilypad.lib._utils import Closure
from lilypad.lib.sandbox.docker import _DEFAULT_IMAGE, DockerSandboxRunner


def test_init():
    """DockerSandboxRunner initializes with correct defaults and overrides."""
    runner = DockerSandboxRunner()
    assert runner.image == _DEFAULT_IMAGE
    assert runner.environment == {}

    runner = DockerSandboxRunner(image="custom-image")
    assert runner.image == "custom-image"
    assert runner.environment == {}

    env = {"KEY": "VALUE"}
    runner = DockerSandboxRunner(environment=env)
    assert runner.image == _DEFAULT_IMAGE
    assert runner.environment == env

    runner = DockerSandboxRunner(image="custom-image", environment=env)
    assert runner.image == "custom-image"
    assert runner.environment == env


def test_create_tar_stream():
    """_create_tar_stream returns an in-memory tar archive with provided files."""
    files = {
        "file1.txt": "content1",
        "file2.py": "content2",
    }

    stream = DockerSandboxRunner._create_tar_stream(files)
    assert isinstance(stream, io.BytesIO)

    with tarfile.open(fileobj=stream, mode="r") as tar:
        file_names = [member.name for member in tar.getmembers()]
        assert "file1.txt" in file_names
        assert "file2.py" in file_names

        file1 = tar.extractfile("file1.txt")
        assert file1.read().decode("utf-8") == "content1"

        file2 = tar.extractfile("file2.py")
        assert file2.read().decode("utf-8") == "content2"


@patch("docker.from_env")
@patch("lilypad.lib.sandbox.docker.DockerSandboxRunner._create_tar_stream")
@patch("lilypad.lib.sandbox.docker.SandboxRunner.generate_script")
@patch("lilypad.lib.sandbox.docker.SandboxRunner.parse_execution_result")
def test_execute_function(mock_parse, mock_generate, mock_create_tar, mock_docker):
    """execute_function runs inside a container and returns parsed results."""
    mock_generate.return_value = "test script"

    mock_tar_stream = MagicMock()
    mock_create_tar.return_value = mock_tar_stream

    mock_container = MagicMock()
    mock_container.exec_run.return_value = (
        0,
        (b'{"result": "success"}', b""),
    )

    mock_client = MagicMock()
    mock_client.containers.run.return_value = mock_container
    mock_docker.return_value = mock_client

    mock_parse.return_value = {"result": "success"}

    runner = DockerSandboxRunner(image="test-image", environment={"ENV": "TEST"})
    closure = Mock(spec=Closure)

    result = runner.execute_function(
        closure,
        custom_result={"custom": "result"},
        pre_actions=["pre"],
        after_actions=["after"],
        extra_imports=["import os"],
        args=(1, 2),
        kwarg1="value1",
    )

    mock_docker.assert_called_once()
    mock_client.containers.run.assert_called_once_with(
        "test-image",
        "tail -f /dev/null",
        remove=True,
        detach=True,
        security_opt=["no-new-privileges"],
        cap_drop=["ALL"],
        environment={"ENV": "TEST"},
    )

    mock_create_tar.assert_called_once_with({"main.py": "test script"})
    mock_container.put_archive.assert_called_once_with("/", mock_tar_stream)
    mock_container.exec_run.assert_called_once_with(cmd=["uv", "run", "/main.py"], demux=True)
    mock_parse.assert_called_once_with(b'{"result": "success"}', b"", 0)

    assert result == {"result": "success"}


@patch("docker.from_env")
@patch("lilypad.lib.sandbox.docker.DockerSandboxRunner._create_tar_stream")
@patch("lilypad.lib.sandbox.docker.SandboxRunner.generate_script")
def test_execute_function_cleanup(mock_generate, mock_create_tar, mock_docker):
    """Container is stopped even when execute_function raises an exception."""
    mock_generate.return_value = "test script"

    mock_tar_stream = MagicMock()
    mock_create_tar.return_value = mock_tar_stream

    mock_container = MagicMock()
    mock_container.exec_run.side_effect = Exception("Test exception")

    mock_client = MagicMock()
    mock_client.containers.run.return_value = mock_container
    mock_docker.return_value = mock_client

    runner = DockerSandboxRunner()
    closure = Mock(spec=Closure)

    with pytest.raises(Exception, match="Test exception"):
        runner.execute_function(closure)

    mock_container.stop.assert_called_once()


@patch("docker.from_env")
@patch("lilypad.lib.sandbox.docker.DockerSandboxRunner._create_tar_stream")
@patch("lilypad.lib.sandbox.docker.SandboxRunner.generate_script")
def test_execute_function_stop_exception(mock_generate, mock_create_tar, mock_docker):
    """Exceptions during container.stop are suppressed in favor of the original."""
    mock_generate.return_value = "test script"

    mock_tar_stream = MagicMock()
    mock_create_tar.return_value = mock_tar_stream

    mock_container = MagicMock()
    mock_container.exec_run.side_effect = Exception("Test exception")
    mock_container.stop.side_effect = Exception("Stop exception")

    mock_client = MagicMock()
    mock_client.containers.run.return_value = mock_container
    mock_docker.return_value = mock_client

    runner = DockerSandboxRunner()
    closure = Mock(spec=Closure)

    with pytest.raises(Exception, match="Test exception"):
        runner.execute_function(closure)

    mock_container.stop.assert_called_once()
