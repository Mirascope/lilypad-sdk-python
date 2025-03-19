# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk._utils import parse_datetime
from lilypad_sdk.types.organizations import OrganizationInvite

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LilypadSDK) -> None:
        invite = client.organizations.invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LilypadSDK) -> None:
        invite = client.organizations.invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="token",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resend_email_id="resend_email_id",
        )
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LilypadSDK) -> None:
        response = client.organizations.invites.with_raw_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LilypadSDK) -> None:
        with client.organizations.invites.with_streaming_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(OrganizationInvite, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LilypadSDK) -> None:
        invite = client.organizations.invites.retrieve(
            "invite_token",
        )
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LilypadSDK) -> None:
        response = client.organizations.invites.with_raw_response.retrieve(
            "invite_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LilypadSDK) -> None:
        with client.organizations.invites.with_streaming_response.retrieve(
            "invite_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(OrganizationInvite, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_token` but received ''"):
            client.organizations.invites.with_raw_response.retrieve(
                "",
            )


class TestAsyncInvites:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLilypadSDK) -> None:
        invite = await async_client.organizations.invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        invite = await async_client.organizations.invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="token",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resend_email_id="resend_email_id",
        )
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.organizations.invites.with_raw_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.organizations.invites.with_streaming_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(OrganizationInvite, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        invite = await async_client.organizations.invites.retrieve(
            "invite_token",
        )
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.organizations.invites.with_raw_response.retrieve(
            "invite_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(OrganizationInvite, invite, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.organizations.invites.with_streaming_response.retrieve(
            "invite_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(OrganizationInvite, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_token` but received ''"):
            await async_client.organizations.invites.with_raw_response.retrieve(
                "",
            )
