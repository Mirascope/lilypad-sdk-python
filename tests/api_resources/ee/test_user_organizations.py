# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.ee import (
    UserOrganizationTable,
    UserOrganizationDeleteResponse,
    UserOrganizationGetUsersResponse,
    UserOrganizationGetUserOrganizationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        user_organization = client.ee.user_organizations.create(
            token="token",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.ee.user_organizations.with_raw_response.create(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.ee.user_organizations.with_streaming_response.create(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Lilypad) -> None:
        user_organization = client.ee.user_organizations.update(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Lilypad) -> None:
        response = client.ee.user_organizations.with_raw_response.update(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Lilypad) -> None:
        with client.ee.user_organizations.with_streaming_response.update(
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
    def test_path_params_update(self, client: Lilypad) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            client.ee.user_organizations.with_raw_response.update(
                user_organization_uuid="",
                role="owner",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Lilypad) -> None:
        user_organization = client.ee.user_organizations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserOrganizationDeleteResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Lilypad) -> None:
        response = client.ee.user_organizations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationDeleteResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Lilypad) -> None:
        with client.ee.user_organizations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationDeleteResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Lilypad) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            client.ee.user_organizations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_user_organizations(self, client: Lilypad) -> None:
        user_organization = client.ee.user_organizations.get_user_organizations()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_user_organizations(self, client: Lilypad) -> None:
        response = client.ee.user_organizations.with_raw_response.get_user_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_user_organizations(self, client: Lilypad) -> None:
        with client.ee.user_organizations.with_streaming_response.get_user_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_users(self, client: Lilypad) -> None:
        user_organization = client.ee.user_organizations.get_users()
        assert_matches_type(UserOrganizationGetUsersResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_users(self, client: Lilypad) -> None:
        response = client.ee.user_organizations.with_raw_response.get_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = response.parse()
        assert_matches_type(UserOrganizationGetUsersResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_users(self, client: Lilypad) -> None:
        with client.ee.user_organizations.with_streaming_response.get_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = response.parse()
            assert_matches_type(UserOrganizationGetUsersResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        user_organization = await async_client.ee.user_organizations.create(
            token="token",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.create(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.create(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypad) -> None:
        user_organization = await async_client.ee.user_organizations.update(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.update(
            user_organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationTable, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.update(
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
    async def test_path_params_update(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            await async_client.ee.user_organizations.with_raw_response.update(
                user_organization_uuid="",
                role="owner",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncLilypad) -> None:
        user_organization = await async_client.ee.user_organizations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserOrganizationDeleteResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationDeleteResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationDeleteResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `user_organization_uuid` but received ''"
        ):
            await async_client.ee.user_organizations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_user_organizations(self, async_client: AsyncLilypad) -> None:
        user_organization = await async_client.ee.user_organizations.get_user_organizations()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_user_organizations(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.get_user_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_user_organizations(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.get_user_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationGetUserOrganizationsResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_users(self, async_client: AsyncLilypad) -> None:
        user_organization = await async_client.ee.user_organizations.get_users()
        assert_matches_type(UserOrganizationGetUsersResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_users(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.user_organizations.with_raw_response.get_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_organization = await response.parse()
        assert_matches_type(UserOrganizationGetUsersResponse, user_organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_users(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.user_organizations.with_streaming_response.get_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_organization = await response.parse()
            assert_matches_type(UserOrganizationGetUsersResponse, user_organization, path=["response"])

        assert cast(Any, response.is_closed) is True
