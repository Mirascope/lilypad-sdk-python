"""This module contains the SandboxRunner abstract base class."""

import inspect
from abc import ABC, abstractmethod
from typing import Any, TypeVar, Optional
from typing_extensions import TypedDict

from .._utils import Closure


class Result(TypedDict, total=False):
    """Result of executing a function in a sandbox."""

    result: Any


class SandboxRunner(ABC):
    """Abstract base class for executing code in a sandbox.

    Subclasses must implement the execute_function method.
    """

    def __init__(self, environment: dict[str, str] | None = None) -> None:
        self.environment: dict[str, str] = environment or {}

    @abstractmethod
    def execute_function(
        self,
        closure: Closure,
        *args: Any,
        custom_result: dict[str, str] | None = None,
        extra_imports: list[str] | None = None,
        **kwargs: Any,
    ) -> Result:
        """Execute the function in the sandbox."""
        ...

    @classmethod
    def _is_async_func(cls, closure: Closure) -> bool:
        lines = closure.signature.splitlines()
        return any(line.strip() for line in lines if line.strip().startswith("async def "))

    @classmethod
    def generate_script(
        cls,
        closure: Closure,
        *args: Any,
        custom_result: dict[str, str] | None = None,
        pre_actions: list[str] | None = None,
        extra_imports: list[str] | None = None,
        **kwargs: Any,
    ) -> str:
        """
        Generate a script that executes the function in the sandbox.

        If wrap_result is True, the script returns a structured JSON object with additional
        attributes. The result is wrapped in a dictionary with the key "result".
        """

        if custom_result:
            result_content = "{" + ", ".join(f'"{k}": ({v})' for k, v in custom_result.items()) + "}"
        else:
            result_content = '{"result": result}'

        base_run = "{name}(*{args}, **{kwargs})".format(name=closure.name, args=args, kwargs=kwargs)

        is_async = cls._is_async_func(closure)
        if is_async:
            extra_imports = extra_imports or []
            extra_imports.append("import asyncio")
            result_code = inspect.cleandoc("""
            async def main():
                    result = await {base_run}
                    return {result_content}
                result = asyncio.run(main())
            """).format(base_run=base_run, result_content=result_content)
        else:
            result_code = inspect.cleandoc("""
            def main():
                    result = {base_run}
                    return {result_content}
                result = main()
            """).format(base_run=base_run, result_content=result_content)

        return inspect.cleandoc("""
            # /// script
            # dependencies = [
            #   {dependencies}
            # ]
            # ///
            
            {code}


            if __name__ == "__main__":
                import json
                {extra_imports}
                {pre_actions}
                {result}
                print(json.dumps(result))
            """).format(
            dependencies=",\n#   ".join(
                [
                    f'"{key}[{",".join(extras)}]=={value["version"]}"'
                    if (extras := value["extras"])
                    else f'"{key}=={value["version"]}"'
                    for key, value in closure.dependencies.items()
                ]
            ),
            code=closure.code,
            result=result_code,
            pre_actions="\n    ".join(pre_actions) if pre_actions else "",
            extra_imports="\n    ".join(extra_imports) if extra_imports else "",
        )


SandboxRunnerT = TypeVar("SandboxRunnerT", bound=SandboxRunner)
