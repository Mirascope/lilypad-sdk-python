"""Run context utilities: Run dataclass, RUN_CONTEXT variable and run() context-manager."""

from __future__ import annotations

import uuid
from typing import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass

_UNSET = object()


@dataclass(slots=True)
class Run:
    """Lightweight container for a run identifier."""

    id: str | None = None

    @staticmethod
    def generate_id() -> str:
        """Return a new 32-char hexadecimal RunID."""
        return uuid.uuid4().hex


RUN_CONTEXT: ContextVar[Run | None] = ContextVar("RUN_CONTEXT", default=None)


@contextmanager
def run(id: str | None = _UNSET) -> Iterator[Run]:
    """Create a Run context."""

    if id is _UNSET:
        run_id = Run.generate_id()
    else:
        run_id = id
    run_obj = Run(run_id)
    token = RUN_CONTEXT.set(run_obj)
    try:
        yield run_obj
    finally:
        RUN_CONTEXT.reset(token)
