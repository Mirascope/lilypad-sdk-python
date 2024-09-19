# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types import CallListResponse, CallCreateResponse
from lilypad_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LilypadSDK) -> None:
        call = client.calls.create(
            input="input",
            output="output",
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LilypadSDK) -> None:
        call = client.calls.create(
            input="input",
            output="output",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            prompt_version_id=0,
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LilypadSDK) -> None:
        response = client.calls.with_raw_response.create(
            input="input",
            output="output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LilypadSDK) -> None:
        with client.calls.with_streaming_response.create(
            input="input",
            output="output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallCreateResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LilypadSDK) -> None:
        call = client.calls.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LilypadSDK) -> None:
        response = client.calls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LilypadSDK) -> None:
        with client.calls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLilypadSDK) -> None:
        call = await async_client.calls.create(
            input="input",
            output="output",
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        call = await async_client.calls.create(
            input="input",
            output="output",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            prompt_version_id=0,
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.calls.with_raw_response.create(
            input="input",
            output="output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.calls.with_streaming_response.create(
            input="input",
            output="output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallCreateResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLilypadSDK) -> None:
        call = await async_client.calls.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.calls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.calls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True
