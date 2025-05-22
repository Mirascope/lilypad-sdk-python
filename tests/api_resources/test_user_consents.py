# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import UserConsentPublic
from lilypad._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserConsents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        user_consent = client.user_consents.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Lilypad) -> None:
        user_consent = client.user_consents.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
            privacy_policy_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            tos_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.user_consents.with_raw_response.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_consent = response.parse()
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.user_consents.with_streaming_response.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_consent = response.parse()
            assert_matches_type(UserConsentPublic, user_consent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Lilypad) -> None:
        user_consent = client.user_consents.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Lilypad) -> None:
        user_consent = client.user_consents.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            privacy_policy_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            privacy_policy_version="privacy_policy_version",
            tos_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            tos_version="tos_version",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Lilypad) -> None:
        response = client.user_consents.with_raw_response.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_consent = response.parse()
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Lilypad) -> None:
        with client.user_consents.with_streaming_response.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_consent = response.parse()
            assert_matches_type(UserConsentPublic, user_consent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_consent_uuid` but received ''"):
            client.user_consents.with_raw_response.update(
                user_consent_uuid="",
            )


class TestAsyncUserConsents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        user_consent = await async_client.user_consents.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypad) -> None:
        user_consent = await async_client.user_consents.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
            privacy_policy_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            tos_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.user_consents.with_raw_response.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_consent = await response.parse()
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.user_consents.with_streaming_response.create(
            privacy_policy_version="privacy_policy_version",
            tos_version="tos_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_consent = await response.parse()
            assert_matches_type(UserConsentPublic, user_consent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypad) -> None:
        user_consent = await async_client.user_consents.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLilypad) -> None:
        user_consent = await async_client.user_consents.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            privacy_policy_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            privacy_policy_version="privacy_policy_version",
            tos_accepted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            tos_version="tos_version",
        )
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypad) -> None:
        response = await async_client.user_consents.with_raw_response.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_consent = await response.parse()
        assert_matches_type(UserConsentPublic, user_consent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypad) -> None:
        async with async_client.user_consents.with_streaming_response.update(
            user_consent_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_consent = await response.parse()
            assert_matches_type(UserConsentPublic, user_consent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_consent_uuid` but received ''"):
            await async_client.user_consents.with_raw_response.update(
                user_consent_uuid="",
            )
