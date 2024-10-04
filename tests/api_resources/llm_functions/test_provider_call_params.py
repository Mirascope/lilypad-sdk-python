# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types.llm_functions import CallArgsPublic, ProviderCallParamsTable

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviderCallParams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LilypadSDK) -> None:
        provider_call_param = client.llm_functions.provider_call_params.create(
            llm_function_id=0,
            call_params={},
            model="model",
            prompt_template="prompt_template",
            provider="openai",
        )
        assert_matches_type(ProviderCallParamsTable, provider_call_param, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LilypadSDK) -> None:
        response = client.llm_functions.provider_call_params.with_raw_response.create(
            llm_function_id=0,
            call_params={},
            model="model",
            prompt_template="prompt_template",
            provider="openai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_call_param = response.parse()
        assert_matches_type(ProviderCallParamsTable, provider_call_param, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LilypadSDK) -> None:
        with client.llm_functions.provider_call_params.with_streaming_response.create(
            llm_function_id=0,
            call_params={},
            model="model",
            prompt_template="prompt_template",
            provider="openai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_call_param = response.parse()
            assert_matches_type(ProviderCallParamsTable, provider_call_param, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LilypadSDK) -> None:
        provider_call_param = client.llm_functions.provider_call_params.retrieve(
            "version_hash",
        )
        assert_matches_type(CallArgsPublic, provider_call_param, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LilypadSDK) -> None:
        response = client.llm_functions.provider_call_params.with_raw_response.retrieve(
            "version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_call_param = response.parse()
        assert_matches_type(CallArgsPublic, provider_call_param, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LilypadSDK) -> None:
        with client.llm_functions.provider_call_params.with_streaming_response.retrieve(
            "version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_call_param = response.parse()
            assert_matches_type(CallArgsPublic, provider_call_param, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_hash` but received ''"):
            client.llm_functions.provider_call_params.with_raw_response.retrieve(
                "",
            )


class TestAsyncProviderCallParams:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLilypadSDK) -> None:
        provider_call_param = await async_client.llm_functions.provider_call_params.create(
            llm_function_id=0,
            call_params={},
            model="model",
            prompt_template="prompt_template",
            provider="openai",
        )
        assert_matches_type(ProviderCallParamsTable, provider_call_param, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.llm_functions.provider_call_params.with_raw_response.create(
            llm_function_id=0,
            call_params={},
            model="model",
            prompt_template="prompt_template",
            provider="openai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_call_param = await response.parse()
        assert_matches_type(ProviderCallParamsTable, provider_call_param, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.llm_functions.provider_call_params.with_streaming_response.create(
            llm_function_id=0,
            call_params={},
            model="model",
            prompt_template="prompt_template",
            provider="openai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_call_param = await response.parse()
            assert_matches_type(ProviderCallParamsTable, provider_call_param, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        provider_call_param = await async_client.llm_functions.provider_call_params.retrieve(
            "version_hash",
        )
        assert_matches_type(CallArgsPublic, provider_call_param, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.llm_functions.provider_call_params.with_raw_response.retrieve(
            "version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_call_param = await response.parse()
        assert_matches_type(CallArgsPublic, provider_call_param, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.llm_functions.provider_call_params.with_streaming_response.retrieve(
            "version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_call_param = await response.parse()
            assert_matches_type(CallArgsPublic, provider_call_param, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_hash` but received ''"):
            await async_client.llm_functions.provider_call_params.with_raw_response.retrieve(
                "",
            )
