# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.ee import OrganizationGetLicenseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_license(self, client: Lilypad) -> None:
        organization = client.ee.organizations.get_license()
        assert_matches_type(OrganizationGetLicenseResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_license(self, client: Lilypad) -> None:
        response = client.ee.organizations.with_raw_response.get_license()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationGetLicenseResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_license(self, client: Lilypad) -> None:
        with client.ee.organizations.with_streaming_response.get_license() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationGetLicenseResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_license(self, async_client: AsyncLilypad) -> None:
        organization = await async_client.ee.organizations.get_license()
        assert_matches_type(OrganizationGetLicenseResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_license(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.organizations.with_raw_response.get_license()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationGetLicenseResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_license(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.organizations.with_streaming_response.get_license() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationGetLicenseResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
