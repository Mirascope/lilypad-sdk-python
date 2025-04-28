"""Factory helpers for cached Lilypad client instances."""

from __future__ import annotations

import asyncio
import weakref
from typing import Any, TypeVar, ParamSpec
from functools import (
    lru_cache,  # noqa: TID251
)

from .settings import get_settings
from ..._client import Lilypad as _BaseLilypad, AsyncLilypad as _BaseAsyncLilypad
from .call_safely import call_safely
from ..._exceptions import RateLimitError, APIConnectionError, InternalServerError

_P = ParamSpec("_P")
_R = TypeVar("_R")

NETWORK_EXCEPTIONS = (APIConnectionError, InternalServerError, RateLimitError)


def _noop_fallback(*_args: object, **_kwargs: object) -> None:
    """Fallback used by @call_safely – swallow the exception and return None."""
    return None


async def _async_noop_fallback(*_args: object, **_kwargs: object) -> None:
    """Fallback used by @call_safely – swallow the exception and return None."""
    return None


class Lilypad(_BaseLilypad):
    """Fail-soft synchronous Lilypad client."""

    @call_safely(_noop_fallback, catch=NETWORK_EXCEPTIONS)
    def request(self, *args: Any, **kwargs: Any):
        return super().request(*args, **kwargs)


class AsyncLilypad(_BaseAsyncLilypad):
    """Fail-soft asynchronous Lilypad client."""

    @call_safely(_async_noop_fallback, catch=NETWORK_EXCEPTIONS)
    async def request(self, *args: Any, **kwargs: Any):
        return await super().request(*args, **kwargs)


@lru_cache(maxsize=256)
def _sync_singleton(api_key: str, base_url: str | None) -> Lilypad:  # noqa: D401
    """Return (or create) the process‑wide synchronous client.

    Args:
        api_key: Lilypad API key used for authentication.

    Returns:
        A memoized :class:`lilypad.Lilypad` instance tied to *api_key*.
    """
    return Lilypad(api_key=api_key, base_url=base_url)


def get_sync_client(api_key: str | None = None, base_url: str | None = None) -> Lilypad:  # noqa: D401
    """Obtain a cached synchronous client.

    Args:
        api_key: Overrides the ``LILYPAD_API_KEY`` environment variable when
            provided.  If *None*, the environment variable is used.
        base_url: Overrides the ``LILYPAD_BASE_URL`` environment variable when

    Returns:
        A cached :class:`lilypad.Lilypad`.
    """
    key = api_key or get_settings().api_key
    if key is None:
        raise RuntimeError("Lilypad API key not provided and LILYPAD_API_KEY is not set.")
    return _sync_singleton(key, base_url or get_settings().base_url)


@lru_cache(maxsize=256)
def _async_singleton(api_key: str, loop_id_for_cache: int, base_url: str | None = None) -> AsyncLilypad:  # noqa: D401
    """Return (or create) an asynchronous client bound to a specific loop.

    Args:
        api_key: Lilypad API key.
        loop_id_for_cache: ``id(asyncio.get_running_loop())`` identifying the event loop.
    """
    loop = asyncio.get_running_loop()
    client = AsyncLilypad(api_key=api_key, base_url=base_url)
    # Ensure the client is closed when the loop is closed.
    weakref.finalize(loop, _async_singleton.cache_clear)
    return client


def get_async_client(api_key: str | None = None, base_url: str | None = None) -> AsyncLilypad:  # noqa: D401
    """Obtain a cached asynchronous client for the current event loop.

    The cache key is the tuple ``(api_key, id(event_loop))`` so that each
    event loop receives its own client instance.

    Args:
        api_key: Overrides the ``LILYPAD_API_KEY`` environment variable.  If
            *None*, the environment variable value is used.

    Returns:
        A cached :class:`lilypad.AsyncLilypad` for the running event loop.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError as exc:  # pragma: no cover – called outside event loop
        raise RuntimeError("get_async_client() must be called from within an active event loop.") from exc

    key = api_key or get_settings().api_key
    if key is None:
        raise RuntimeError("Lilypad API key not provided and LILYPAD_API_KEY is not set.")

    return _async_singleton(key, id(loop), base_url=base_url or get_settings().base_url)


__all__ = ["get_sync_client", "get_async_client", "NETWORK_EXCEPTIONS"]
