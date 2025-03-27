"""Subprocess sandbox runner."""

import os
import json
import tempfile
import subprocess
from typing import Any, cast
from pathlib import Path

from . import SandboxRunner
from .runner import Result
from .._utils import Closure


class SubprocessSandboxRunner(SandboxRunner):
    """Runs code in a subprocess."""

    def __init__(self, environment: dict[str, str] | None = None) -> None:
        super().__init__(environment)
        if "PATH" not in self.environment:
            # Set uv path to the default value if not provided
            self.environment["PATH"] = os.environ["PATH"]

    def execute_function(
        self,
        closure: Closure,
        *args: Any,
        extra_result: dict[str, str] | None = None,
        extra_imports: list[str] | None = None,
        **kwargs: Any,
    ) -> Result:
        """Execute the function in the sandbox."""
        script = self.generate_script(closure, extra_result, *args, **kwargs)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp_file:
            tmp_file.write(script)
            tmp_path = Path(tmp_file.name)
        try:
            result = subprocess.run(
                ["uv", "run", "--no-project", str(tmp_path)],
                check=True,
                capture_output=True,
                text=True,
                env=self.environment,
            )
            return cast(Result, json.loads(result.stdout.strip()))
        except subprocess.CalledProcessError as e:
            error_message = f"Process exited with non-zero status.\nStdout: {e.stdout}\nStderr: {e.stderr}"
            raise RuntimeError(error_message)
        finally:
            tmp_path.unlink()
