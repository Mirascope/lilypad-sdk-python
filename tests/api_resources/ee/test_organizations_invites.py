# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk._utils import parse_datetime
from lilypad_sdk.types.ee import OrganizationInvitePublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizationsInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_organization_invite(self, client: LilypadSDK) -> None:
        organizations_invite = client.ee.organizations_invites.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_organization_invite_with_all_params(self, client: LilypadSDK) -> None:
        organizations_invite = client.ee.organizations_invites.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="token",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resend_email_id="resend_email_id",
        )
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_organization_invite(self, client: LilypadSDK) -> None:
        response = client.ee.organizations_invites.with_raw_response.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = response.parse()
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_organization_invite(self, client: LilypadSDK) -> None:
        with client.ee.organizations_invites.with_streaming_response.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = response.parse()
            assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_organization_invite(self, client: LilypadSDK) -> None:
        organizations_invite = client.ee.organizations_invites.get_organization_invite(
            "invite_token",
        )
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_organization_invite(self, client: LilypadSDK) -> None:
        response = client.ee.organizations_invites.with_raw_response.get_organization_invite(
            "invite_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = response.parse()
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_organization_invite(self, client: LilypadSDK) -> None:
        with client.ee.organizations_invites.with_streaming_response.get_organization_invite(
            "invite_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = response.parse()
            assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_organization_invite(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_token` but received ''"):
            client.ee.organizations_invites.with_raw_response.get_organization_invite(
                "",
            )


class TestAsyncOrganizationsInvites:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        organizations_invite = await async_client.ee.organizations_invites.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_organization_invite_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        organizations_invite = await async_client.ee.organizations_invites.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="token",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resend_email_id="resend_email_id",
        )
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.organizations_invites.with_raw_response.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = await response.parse()
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.organizations_invites.with_streaming_response.create_organization_invite(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = await response.parse()
            assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        organizations_invite = await async_client.ee.organizations_invites.get_organization_invite(
            "invite_token",
        )
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.organizations_invites.with_raw_response.get_organization_invite(
            "invite_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = await response.parse()
        assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.organizations_invites.with_streaming_response.get_organization_invite(
            "invite_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = await response.parse()
            assert_matches_type(OrganizationInvitePublic, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_organization_invite(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_token` but received ''"):
            await async_client.ee.organizations_invites.with_raw_response.get_organization_invite(
                "",
            )
