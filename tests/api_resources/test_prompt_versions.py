# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types import PromptVersionPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LilypadSDK) -> None:
        prompt_version = client.prompt_versions.retrieve(
            "version_hash",
        )
        assert_matches_type(PromptVersionPublic, prompt_version, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LilypadSDK) -> None:
        response = client.prompt_versions.with_raw_response.retrieve(
            "version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_version = response.parse()
        assert_matches_type(PromptVersionPublic, prompt_version, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LilypadSDK) -> None:
        with client.prompt_versions.with_streaming_response.retrieve(
            "version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_version = response.parse()
            assert_matches_type(PromptVersionPublic, prompt_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_hash` but received ''"):
            client.prompt_versions.with_raw_response.retrieve(
                "",
            )


class TestAsyncPromptVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        prompt_version = await async_client.prompt_versions.retrieve(
            "version_hash",
        )
        assert_matches_type(PromptVersionPublic, prompt_version, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.prompt_versions.with_raw_response.retrieve(
            "version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_version = await response.parse()
        assert_matches_type(PromptVersionPublic, prompt_version, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.prompt_versions.with_streaming_response.retrieve(
            "version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_version = await response.parse()
            assert_matches_type(PromptVersionPublic, prompt_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_hash` but received ''"):
            await async_client.prompt_versions.with_raw_response.retrieve(
                "",
            )
