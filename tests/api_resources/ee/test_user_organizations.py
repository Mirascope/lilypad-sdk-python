# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types.ee import (
    UserOrganizationTable,
    UserOrganizationGetUserOrganizationsResponse,
    UserOrganizationDeleteUserOrganizationResponse,
    UserOrganizationGetUsersByOrganizationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_user_organization(self, client: LilypadSDK) -> None:
        user_organization = client.ee.user_organizations.create_user_organization(
            token="token",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_user_organization(self, client: LilypadSDK) -> None:
        response = client.ee.user_organizations.with_raw_response.create_user_organization(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_user_organization(self, client: LilypadSDK) -> None:
        with client.ee.user_organizations.with_streaming_response.create_user_organization(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_user_organization(self, client: LilypadSDK) -> None:
        user_organization = client.ee.user_organizations.delete_user_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserOrganizationDeleteUserOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_user_organization(self, client: LilypadSDK) -> None:
        response = client.ee.user_organizations.with_raw_response.delete_user_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationDeleteUserOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_user_organization(self, client: LilypadSDK) -> None:
        with client.ee.user_organizations.with_streaming_response.delete_user_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationDeleteUserOrganizationResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_user_organization(self, client: LilypadSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            client.ee.user_organizations.with_raw_response.delete_user_organization(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_user_organizations(self, client: LilypadSDK) -> None:
        user_organization = client.ee.user_organizations.get_user_organizations()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_user_organizations(self, client: LilypadSDK) -> None:
        response = client.ee.user_organizations.with_raw_response.get_user_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_user_organizations(self, client: LilypadSDK) -> None:
        with client.ee.user_organizations.with_streaming_response.get_user_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_users_by_organization(self, client: LilypadSDK) -> None:
        user_organization = client.ee.user_organizations.get_users_by_organization()
        assert_matches_type(UserOrganizationGetUsersByOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_users_by_organization(self, client: LilypadSDK) -> None:
        response = client.ee.user_organizations.with_raw_response.get_users_by_organization()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationGetUsersByOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_users_by_organization(self, client: LilypadSDK) -> None:
        with client.ee.user_organizations.with_streaming_response.get_users_by_organization() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationGetUsersByOrganizationResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_user_organization(self, client: LilypadSDK) -> None:
        user_organization = client.ee.user_organizations.update_user_organization(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_user_organization(self, client: LilypadSDK) -> None:
        response = client.ee.user_organizations.with_raw_response.update_user_organization(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_user_organization(self, client: LilypadSDK) -> None:
        with client.ee.user_organizations.with_streaming_response.update_user_organization(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_user_organization(self, client: LilypadSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            client.ee.user_organizations.with_raw_response.update_user_organization(
                user_organization_uuid="",
                role="owner",
            )


class TestAsyncUserOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        user_organization = await async_client.ee.user_organizations.create_user_organization(
            token="token",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.create_user_organization(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.create_user_organization(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        user_organization = await async_client.ee.user_organizations.delete_user_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserOrganizationDeleteUserOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.delete_user_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationDeleteUserOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.delete_user_organization(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationDeleteUserOrganizationResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            await async_client.ee.user_organizations.with_raw_response.delete_user_organization(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_user_organizations(self, async_client: AsyncLilypadSDK) -> None:
        user_organization = await async_client.ee.user_organizations.get_user_organizations()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_user_organizations(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.get_user_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_user_organizations(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.get_user_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_users_by_organization(self, async_client: AsyncLilypadSDK) -> None:
        user_organization = await async_client.ee.user_organizations.get_users_by_organization()
        assert_matches_type(UserOrganizationGetUsersByOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_users_by_organization(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.get_users_by_organization()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationGetUsersByOrganizationResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_users_by_organization(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.get_users_by_organization() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationGetUsersByOrganizationResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        user_organization = await async_client.ee.user_organizations.update_user_organization(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.update_user_organization(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.update_user_organization(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_user_organization(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            await async_client.ee.user_organizations.with_raw_response.update_user_organization(
                user_organization_uuid="",
                role="owner",
            )
