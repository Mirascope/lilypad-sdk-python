"""Utilities for caching Function metadata fetched from the Lilypad API."""

from __future__ import annotations

import asyncio
from functools import lru_cache  # noqa: TID251

from lilypad.lib._utils.client import get_sync_client, get_async_client
from lilypad.types.projects.functions import FunctionPublic

_HASH_SYNC_MAX = 2_048
_hash_async_lock = asyncio.Lock()
_hash_async_cache: dict[tuple[str, str], FunctionPublic] = {}


@lru_cache(maxsize=_HASH_SYNC_MAX)
def get_function_by_hash_sync(project_uuid: str, function_hash: str) -> FunctionPublic:
    """Synchronous, cached `retrieve_by_hash`."""
    client = get_sync_client()
    return client.projects.functions.retrieve_by_hash(
        project_uuid=project_uuid,
        function_hash=function_hash,
    )


async def get_function_by_hash_async(project_uuid: str, function_hash: str) -> FunctionPublic:
    """Asynchronous, cached `retrieve_by_hash`."""
    key = (project_uuid, function_hash)
    if key in _hash_async_cache:
        return _hash_async_cache[key]

    async with _hash_async_lock:
        if key in _hash_async_cache:  # lost race
            return _hash_async_cache[key]

        client = get_async_client()
        fn = await client.projects.functions.retrieve_by_hash(
            project_uuid=project_uuid,
            function_hash=function_hash,
        )
        _hash_async_cache[key] = fn
        return fn


_VERSION_SYNC_MAX = 2_048
_version_async_lock = asyncio.Lock()
_version_async_cache: dict[tuple[str, str, int], FunctionPublic] = {}


@lru_cache(maxsize=_VERSION_SYNC_MAX)
def get_function_by_version_sync(
    project_uuid: str,
    function_name: str,
    version_num: int,
) -> FunctionPublic:
    """Synchronous, cached `retrieve_by_version`."""
    client = get_sync_client()
    return client.projects.functions.name.retrieve_by_version(
        project_uuid=project_uuid,
        function_name=function_name,
        version_num=version_num,
    )


async def get_function_by_version_async(
    project_uuid: str,
    function_name: str,
    version_num: int,
) -> FunctionPublic:
    """Asynchronous, cached `retrieve_by_version`."""
    key = (project_uuid, function_name, version_num)
    if key in _version_async_cache:
        return _version_async_cache[key]

    async with _version_async_lock:
        if key in _version_async_cache:
            return _version_async_cache[key]

        client = get_async_client()
        fn = await client.projects.functions.name.retrieve_by_version(
            project_uuid=project_uuid,
            function_name=function_name,
            version_num=version_num,
        )
        _version_async_cache[key] = fn
        return fn


__all__ = [
    "get_function_by_hash_sync",
    "get_function_by_hash_async",
    "get_function_by_version_sync",
    "get_function_by_version_async",
]
