# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import OrganizationInvite
from lilypad._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizationsInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        organizations_invite = client.organizations_invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Lilypad) -> None:
        organizations_invite = client.organizations_invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="token",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resend_email_id="resend_email_id",
        )
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.organizations_invites.with_raw_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = response.parse()
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.organizations_invites.with_streaming_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = response.parse()
            assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        organizations_invite = client.organizations_invites.retrieve(
            "invite_token",
        )
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.organizations_invites.with_raw_response.retrieve(
            "invite_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = response.parse()
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.organizations_invites.with_streaming_response.retrieve(
            "invite_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = response.parse()
            assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_token` but received ''"):
            client.organizations_invites.with_raw_response.retrieve(
                "",
            )


class TestAsyncOrganizationsInvites:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        organizations_invite = await async_client.organizations_invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypad) -> None:
        organizations_invite = await async_client.organizations_invites.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="token",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resend_email_id="resend_email_id",
        )
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.organizations_invites.with_raw_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = await response.parse()
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.organizations_invites.with_streaming_response.create(
            email="x",
            invited_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = await response.parse()
            assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        organizations_invite = await async_client.organizations_invites.retrieve(
            "invite_token",
        )
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.organizations_invites.with_raw_response.retrieve(
            "invite_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizations_invite = await response.parse()
        assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.organizations_invites.with_streaming_response.retrieve(
            "invite_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizations_invite = await response.parse()
            assert_matches_type(OrganizationInvite, organizations_invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_token` but received ''"):
            await async_client.organizations_invites.with_raw_response.retrieve(
                "",
            )
