# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import WebhookHandleStripeEventResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_handle_stripe_event(self, client: Lilypad) -> None:
        webhook = client.webhooks.handle_stripe_event()
        assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_handle_stripe_event_with_all_params(self, client: Lilypad) -> None:
        webhook = client.webhooks.handle_stripe_event(
            stripe_signature="Stripe-Signature",
        )
        assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_handle_stripe_event(self, client: Lilypad) -> None:
        response = client.webhooks.with_raw_response.handle_stripe_event()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_handle_stripe_event(self, client: Lilypad) -> None:
        with client.webhooks.with_streaming_response.handle_stripe_event() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_handle_stripe_event(self, async_client: AsyncLilypad) -> None:
        webhook = await async_client.webhooks.handle_stripe_event()
        assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_handle_stripe_event_with_all_params(self, async_client: AsyncLilypad) -> None:
        webhook = await async_client.webhooks.handle_stripe_event(
            stripe_signature="Stripe-Signature",
        )
        assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_handle_stripe_event(self, async_client: AsyncLilypad) -> None:
        response = await async_client.webhooks.with_raw_response.handle_stripe_event()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_handle_stripe_event(self, async_client: AsyncLilypad) -> None:
        async with async_client.webhooks.with_streaming_response.handle_stripe_event() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookHandleStripeEventResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
