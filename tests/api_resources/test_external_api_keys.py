# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import (
    ExternalAPIKeyPublic,
    ExternalAPIKeyListResponse,
    ExternalAPIKeyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        external_api_key = client.external_api_keys.create(
            api_key="api_key",
            service_name="service_name",
        )
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.external_api_keys.with_raw_response.create(
            api_key="api_key",
            service_name="service_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = response.parse()
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.external_api_keys.with_streaming_response.create(
            api_key="api_key",
            service_name="service_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = response.parse()
            assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        external_api_key = client.external_api_keys.retrieve(
            "service_name",
        )
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.external_api_keys.with_raw_response.retrieve(
            "service_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = response.parse()
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.external_api_keys.with_streaming_response.retrieve(
            "service_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = response.parse()
            assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            client.external_api_keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Lilypad) -> None:
        external_api_key = client.external_api_keys.list()
        assert_matches_type(ExternalAPIKeyListResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Lilypad) -> None:
        response = client.external_api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = response.parse()
        assert_matches_type(ExternalAPIKeyListResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Lilypad) -> None:
        with client.external_api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = response.parse()
            assert_matches_type(ExternalAPIKeyListResponse, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Lilypad) -> None:
        external_api_key = client.external_api_keys.delete(
            "service_name",
        )
        assert_matches_type(ExternalAPIKeyDeleteResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Lilypad) -> None:
        response = client.external_api_keys.with_raw_response.delete(
            "service_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = response.parse()
        assert_matches_type(ExternalAPIKeyDeleteResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Lilypad) -> None:
        with client.external_api_keys.with_streaming_response.delete(
            "service_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = response.parse()
            assert_matches_type(ExternalAPIKeyDeleteResponse, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            client.external_api_keys.with_raw_response.delete(
                "",
            )


class TestAsyncExternalAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        external_api_key = await async_client.external_api_keys.create(
            api_key="api_key",
            service_name="service_name",
        )
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.external_api_keys.with_raw_response.create(
            api_key="api_key",
            service_name="service_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = await response.parse()
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.external_api_keys.with_streaming_response.create(
            api_key="api_key",
            service_name="service_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = await response.parse()
            assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        external_api_key = await async_client.external_api_keys.retrieve(
            "service_name",
        )
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.external_api_keys.with_raw_response.retrieve(
            "service_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = await response.parse()
        assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.external_api_keys.with_streaming_response.retrieve(
            "service_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = await response.parse()
            assert_matches_type(ExternalAPIKeyPublic, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            await async_client.external_api_keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLilypad) -> None:
        external_api_key = await async_client.external_api_keys.list()
        assert_matches_type(ExternalAPIKeyListResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypad) -> None:
        response = await async_client.external_api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = await response.parse()
        assert_matches_type(ExternalAPIKeyListResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypad) -> None:
        async with async_client.external_api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = await response.parse()
            assert_matches_type(ExternalAPIKeyListResponse, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncLilypad) -> None:
        external_api_key = await async_client.external_api_keys.delete(
            "service_name",
        )
        assert_matches_type(ExternalAPIKeyDeleteResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLilypad) -> None:
        response = await async_client.external_api_keys.with_raw_response.delete(
            "service_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_api_key = await response.parse()
        assert_matches_type(ExternalAPIKeyDeleteResponse, external_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLilypad) -> None:
        async with async_client.external_api_keys.with_streaming_response.delete(
            "service_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_api_key = await response.parse()
            assert_matches_type(ExternalAPIKeyDeleteResponse, external_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            await async_client.external_api_keys.with_raw_response.delete(
                "",
            )
