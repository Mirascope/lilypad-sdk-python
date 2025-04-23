"""Factory helpers for cached Lilypad client instances."""

from __future__ import annotations

import asyncio
import logging
import weakref
from typing import Any, TypeVar, Callable, ParamSpec
from functools import (
    wraps,
    lru_cache,  # noqa: TID251
)

import httpx

from .settings import get_settings
from ..._client import Lilypad as _BaseLilypad, AsyncLilypad as _BaseAsyncLilypad
from ..exceptions import LilypadException
from .fn_is_async import fn_is_async
from ..._exceptions import LilypadError

_P = ParamSpec("_P")
_R = TypeVar("_R")


def safe_lilypad_call(*, logger_name: str = "lilypad") -> Callable[[Callable[_P, _R]], Callable[_P, _R | None]]:
    """Return a decorator that suppresses httpx transport errors."""

    logger = logging.getLogger(logger_name)

    def decorator(fn: Callable[_P, _R]) -> Callable[_P, _R | None]:
        if fn_is_async(fn):

            @wraps(fn)
            async def inner(*args: _P.args, **kwargs: _P.kwargs) -> _R | None:  # type: ignore[override]
                try:
                    return await fn(*args, **kwargs)
                except (httpx.RequestError, httpx.HTTPStatusError, LilypadException, LilypadError) as exc:
                    logger.warning("Lilypad call failed – graceful degradation (%s)", exc)
                    return None

            return inner

        @wraps(fn)
        def inner(*args: _P.args, **kwargs: _P.kwargs) -> _R | None:  # type: ignore[override]
            try:
                return fn(*args, **kwargs)
            except (httpx.RequestError, httpx.HTTPStatusError, LilypadException, LilypadError) as exc:
                logger.warning("Lilypad call failed – graceful degradation (%s)", exc)
                return None

        return inner

    return decorator


class Lilypad(_BaseLilypad):
    """Fail-soft synchronous Lilypad client."""

    @safe_lilypad_call()
    def _request(self, *args: Any, **kwargs: Any):
        return super()._request(*args, **kwargs)


class AsyncLilypad(_BaseAsyncLilypad):
    """Fail-soft asynchronous Lilypad client."""

    @safe_lilypad_call()
    async def _request(self, *args: Any, **kwargs: Any):
        return await super()._request(*args, **kwargs)


@lru_cache(maxsize=256)
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
    key = api_key or get_settings().api_key
    if key is None:
        raise RuntimeError("Lilypad API key not provided and LILYPAD_API_KEY is not set.")
    return _sync_singleton(key)


@lru_cache(maxsize=256)
def _async_singleton(api_key: str, loop_id_for_cache: int) -> AsyncLilypad:  # noqa: D401
    """Return (or create) an asynchronous client bound to a specific loop.

    Args:
        api_key: Lilypad API key.
        loop_id_for_cache: ``id(asyncio.get_running_loop())`` identifying the event loop.
    """
    loop = asyncio.get_running_loop()
    client = AsyncLilypad(api_key=api_key)
    # Ensure the client is closed when the loop is closed.
    weakref.finalize(loop, _async_singleton.cache_clear)
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

    key = api_key or get_settings().api_key
    if key is None:
        raise RuntimeError("Lilypad API key not provided and LILYPAD_API_KEY is not set.")

    return _async_singleton(key, id(loop))


__all__ = ["get_sync_client", "get_async_client"]
