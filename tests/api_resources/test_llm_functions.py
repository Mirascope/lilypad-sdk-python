# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types import (
    LlmFunctionTable,
    LlmFunctionBasePublic,
    LlmFunctionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlmFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LilypadSDK) -> None:
        llm_function = client.llm_functions.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
        )
        assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LilypadSDK) -> None:
        llm_function = client.llm_functions.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
            input_arguments="input_arguments",
        )
        assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LilypadSDK) -> None:
        response = client.llm_functions.with_raw_response.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_function = response.parse()
        assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LilypadSDK) -> None:
        with client.llm_functions.with_streaming_response.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_function = response.parse()
            assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LilypadSDK) -> None:
        llm_function = client.llm_functions.retrieve(
            "version_hash",
        )
        assert_matches_type(LlmFunctionBasePublic, llm_function, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LilypadSDK) -> None:
        response = client.llm_functions.with_raw_response.retrieve(
            "version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_function = response.parse()
        assert_matches_type(LlmFunctionBasePublic, llm_function, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LilypadSDK) -> None:
        with client.llm_functions.with_streaming_response.retrieve(
            "version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_function = response.parse()
            assert_matches_type(LlmFunctionBasePublic, llm_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_hash` but received ''"):
            client.llm_functions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LilypadSDK) -> None:
        llm_function = client.llm_functions.list(
            function_name="function_name",
        )
        assert_matches_type(LlmFunctionListResponse, llm_function, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LilypadSDK) -> None:
        response = client.llm_functions.with_raw_response.list(
            function_name="function_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_function = response.parse()
        assert_matches_type(LlmFunctionListResponse, llm_function, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LilypadSDK) -> None:
        with client.llm_functions.with_streaming_response.list(
            function_name="function_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_function = response.parse()
            assert_matches_type(LlmFunctionListResponse, llm_function, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLlmFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLilypadSDK) -> None:
        llm_function = await async_client.llm_functions.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
        )
        assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        llm_function = await async_client.llm_functions.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
            input_arguments="input_arguments",
        )
        assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.llm_functions.with_raw_response.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_function = await response.parse()
        assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.llm_functions.with_streaming_response.create(
            code="code",
            function_name="function_name",
            version_hash="version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_function = await response.parse()
            assert_matches_type(LlmFunctionTable, llm_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        llm_function = await async_client.llm_functions.retrieve(
            "version_hash",
        )
        assert_matches_type(LlmFunctionBasePublic, llm_function, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.llm_functions.with_raw_response.retrieve(
            "version_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_function = await response.parse()
        assert_matches_type(LlmFunctionBasePublic, llm_function, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.llm_functions.with_streaming_response.retrieve(
            "version_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_function = await response.parse()
            assert_matches_type(LlmFunctionBasePublic, llm_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_hash` but received ''"):
            await async_client.llm_functions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLilypadSDK) -> None:
        llm_function = await async_client.llm_functions.list(
            function_name="function_name",
        )
        assert_matches_type(LlmFunctionListResponse, llm_function, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.llm_functions.with_raw_response.list(
            function_name="function_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_function = await response.parse()
        assert_matches_type(LlmFunctionListResponse, llm_function, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.llm_functions.with_streaming_response.list(
            function_name="function_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_function = await response.parse()
            assert_matches_type(LlmFunctionListResponse, llm_function, path=["response"])

        assert cast(Any, response.is_closed) is True
