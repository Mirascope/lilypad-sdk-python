# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types import Organization

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: LilypadSDK) -> None:
        organization = client.organizations.update()
        assert_matches_type(Organization, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: LilypadSDK) -> None:
        organization = client.organizations.update(
            license="license",
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: LilypadSDK) -> None:
        response = client.organizations.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: LilypadSDK) -> None:
        with client.organizations.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypadSDK) -> None:
        organization = await async_client.organizations.update()
        assert_matches_type(Organization, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        organization = await async_client.organizations.update(
            license="license",
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.organizations.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.organizations.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
