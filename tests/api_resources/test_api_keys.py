# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import APIKeyListResponse, APIKeyDeleteResponse
from lilypad._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        api_key = client.api_keys.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Lilypad) -> None:
        api_key = client.api_keys.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            key_hash="key_hash",
        )
        assert_matches_type(str, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.api_keys.with_raw_response.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(str, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.api_keys.with_streaming_response.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(str, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Lilypad) -> None:
        api_key = client.api_keys.list()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Lilypad) -> None:
        response = client.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Lilypad) -> None:
        with client.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Lilypad) -> None:
        api_key = client.api_keys.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Lilypad) -> None:
        response = client.api_keys.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Lilypad) -> None:
        with client.api_keys.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.api_keys.with_raw_response.delete(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        api_key = await async_client.api_keys.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypad) -> None:
        api_key = await async_client.api_keys.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            key_hash="key_hash",
        )
        assert_matches_type(str, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.api_keys.with_raw_response.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(str, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.api_keys.with_streaming_response.create(
            name="x",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(str, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLilypad) -> None:
        api_key = await async_client.api_keys.list()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypad) -> None:
        response = await async_client.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypad) -> None:
        async with async_client.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncLilypad) -> None:
        api_key = await async_client.api_keys.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLilypad) -> None:
        response = await async_client.api_keys.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLilypad) -> None:
        async with async_client.api_keys.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.api_keys.with_raw_response.delete(
                "",
            )
