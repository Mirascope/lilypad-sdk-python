"""Factory helpers for cached Lilypad client instances."""

from __future__ import annotations

import os
import asyncio
import weakref

from cachetools.func import lru_cache

from ..._client import Lilypad, AsyncLilypad


@lru_cache(maxsize=None)
def _sync_singleton(api_key: str) -> Lilypad:  # noqa: D401
    """Return (or create) the process‑wide synchronous client.

    Args:
        api_key: Lilypad API key used for authentication.

    Returns:
        A memoized :class:`lilypad.Lilypad` instance tied to *api_key*.
    """
    return Lilypad(api_key=api_key)


def get_sync_client(api_key: str | None = None) -> Lilypad:  # noqa: D401
    """Obtain a cached synchronous client.

    Args:
        api_key: Overrides the ``LILYPAD_API_KEY`` environment variable when
            provided.  If *None*, the environment variable is used.

    Returns:
        A cached :class:`lilypad.Lilypad`.
    """
    key = api_key or os.getenv("LILYPAD_API_KEY")
    if key is None:
        raise RuntimeError("Lilypad API key not provided and LILYPAD_API_KEY is not set.")
    return _sync_singleton(key)


@lru_cache(maxsize=None)
def _async_singleton(api_key: str, loop_id: int) -> AsyncLilypad:  # noqa: D401
    """Return (or create) an asynchronous client bound to a specific loop.

    Args:
        api_key: Lilypad API key.
        loop_id: ``id(asyncio.get_running_loop())`` identifying the event loop.
    """
    loop = asyncio.get_running_loop()
    client = AsyncLilypad(api_key=api_key)
    # Ensure the client is closed when the loop is closed.
    weakref.finalize(loop, _async_singleton.cache.pop, (api_key, loop_id), None)
    return client


def get_async_client(api_key: str | None = None) -> AsyncLilypad:  # noqa: D401
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

    key = api_key or os.getenv("LILYPAD_API_KEY")
    if key is None:
        raise RuntimeError("Lilypad API key not provided and LILYPAD_API_KEY is not set.")

    return _async_singleton(key, id(loop))


__all__ = ["get_sync_client", "get_async_client"]
