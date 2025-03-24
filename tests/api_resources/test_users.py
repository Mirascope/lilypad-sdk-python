# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.auth import UserPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_active_organization(self, client: Lilypad) -> None:
        user = client.users.update_active_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_active_organization(self, client: Lilypad) -> None:
        response = client.users.with_raw_response.update_active_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_active_organization(self, client: Lilypad) -> None:
        with client.users.with_streaming_response.update_active_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserPublic, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_active_organization(self, client: Lilypad) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `active_organization_uuid` but received ''"
        ):
            client.users.with_raw_response.update_active_organization(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_keys(self, client: Lilypad) -> None:
        user = client.users.update_keys(
            body={},
        )
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_keys(self, client: Lilypad) -> None:
        response = client.users.with_raw_response.update_keys(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_keys(self, client: Lilypad) -> None:
        with client.users.with_streaming_response.update_keys(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserPublic, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_active_organization(self, async_client: AsyncLilypad) -> None:
        user = await async_client.users.update_active_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_active_organization(self, async_client: AsyncLilypad) -> None:
        response = await async_client.users.with_raw_response.update_active_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_active_organization(self, async_client: AsyncLilypad) -> None:
        async with async_client.users.with_streaming_response.update_active_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserPublic, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_active_organization(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `active_organization_uuid` but received ''"
        ):
            await async_client.users.with_raw_response.update_active_organization(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_keys(self, async_client: AsyncLilypad) -> None:
        user = await async_client.users.update_keys(
            body={},
        )
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_keys(self, async_client: AsyncLilypad) -> None:
        response = await async_client.users.with_raw_response.update_keys(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_keys(self, async_client: AsyncLilypad) -> None:
        async with async_client.users.with_streaming_response.update_keys(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserPublic, user, path=["response"])

        assert cast(Any, response.is_closed) is True
