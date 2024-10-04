# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types import TraceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LilypadSDK) -> None:
        trace = client.traces.create()
        assert_matches_type(object, trace, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LilypadSDK) -> None:
        response = client.traces.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(object, trace, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LilypadSDK) -> None:
        with client.traces.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(object, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LilypadSDK) -> None:
        trace = client.traces.list()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LilypadSDK) -> None:
        response = client.traces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LilypadSDK) -> None:
        with client.traces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceListResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTraces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLilypadSDK) -> None:
        trace = await async_client.traces.create()
        assert_matches_type(object, trace, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.traces.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(object, trace, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.traces.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(object, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLilypadSDK) -> None:
        trace = await async_client.traces.list()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.traces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.traces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceListResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True
