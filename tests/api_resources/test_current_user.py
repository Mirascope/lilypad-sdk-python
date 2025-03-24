# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.auth import UserPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrentUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        current_user = client.current_user.retrieve()
        assert_matches_type(UserPublic, current_user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.current_user.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = response.parse()
        assert_matches_type(UserPublic, current_user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.current_user.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = response.parse()
            assert_matches_type(UserPublic, current_user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrentUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        current_user = await async_client.current_user.retrieve()
        assert_matches_type(UserPublic, current_user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.current_user.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = await response.parse()
        assert_matches_type(UserPublic, current_user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.current_user.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = await response.parse()
            assert_matches_type(UserPublic, current_user, path=["response"])

        assert cast(Any, response.is_closed) is True
