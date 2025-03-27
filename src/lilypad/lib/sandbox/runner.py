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
        extra_result: dict[str, str] | None = None,
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
    def _generate_async_run(cls, closure: Closure, *args: Any, **kwargs: Any) -> str:
        return inspect.cleandoc("""
                import asyncio
                    result = asyncio.run({name}(*{args}, **{kwargs}))
                """).format(name=closure.name, args=args, kwargs=kwargs)

    @classmethod
    def _generate_sync_run(cls, closure: Closure, *args: Any, **kwargs: Any) -> str:
        return inspect.cleandoc("""
                    result = {name}(*{args}, **{kwargs})
                """).format(name=closure.name, args=args, kwargs=kwargs)

    @classmethod
    def generate_script(
        cls,
        closure: Closure,
        *args: Any,
        extra_result: dict[str, str] | None = None,
        extra_imports: list[str] | None = None,
        **kwargs: Any,
    ) -> str:
        """
        Generate a script that executes the function in the sandbox.

        If wrap_result is True, the script returns a structured JSON object with additional
        attributes. The additional attributes are specified by the extra_result dictionary,
        where keys are attribute names and values are code snippets that evaluate to the attribute values.
        """
        base_run = (
            cls._generate_async_run(closure, *args, **kwargs)
            if cls._is_async_func(closure)
            else cls._generate_sync_run(closure, *args, **kwargs)
        )
        extra_items = ""
        if extra_result:
            extra_items = ", " + ", ".join(f'"{k}": ({v})' for k, v in extra_result.items())
        result_code = base_run + "\n" + f'result = {{"result": result{extra_items}}}'

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
            extra_imports="\n".join(extra_imports) if extra_imports else "",
        )


SandboxRunnerT = TypeVar("SandboxRunnerT", bound=SandboxRunner)
