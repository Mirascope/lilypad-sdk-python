# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.auth import UserPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitHub:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_handle_callback(self, client: Lilypad) -> None:
        github = client.auth.github.handle_callback(
            code="code",
        )
        assert_matches_type(UserPublic, github, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_handle_callback(self, client: Lilypad) -> None:
        response = client.auth.github.with_raw_response.handle_callback(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(UserPublic, github, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_handle_callback(self, client: Lilypad) -> None:
        with client.auth.github.with_streaming_response.handle_callback(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(UserPublic, github, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGitHub:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_handle_callback(self, async_client: AsyncLilypad) -> None:
        github = await async_client.auth.github.handle_callback(
            code="code",
        )
        assert_matches_type(UserPublic, github, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_handle_callback(self, async_client: AsyncLilypad) -> None:
        response = await async_client.auth.github.with_raw_response.handle_callback(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(UserPublic, github, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_handle_callback(self, async_client: AsyncLilypad) -> None:
        async with async_client.auth.github.with_streaming_response.handle_callback(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(UserPublic, github, path=["response"])

        assert cast(Any, response.is_closed) is True
