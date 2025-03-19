# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types.projects.generations import (
    SpanListResponse,
    SpanGetAggregatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: LilypadSDK) -> None:
        span = client.projects.generations.spans.list(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanListResponse, span, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LilypadSDK) -> None:
        response = client.projects.generations.spans.with_raw_response.list(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanListResponse, span, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LilypadSDK) -> None:
        with client.projects.generations.spans.with_streaming_response.list(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanListResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.generations.spans.with_raw_response.list(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            client.projects.generations.spans.with_raw_response.list(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_aggregates(self, client: LilypadSDK) -> None:
        span = client.projects.generations.spans.get_aggregates(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )
        assert_matches_type(SpanGetAggregatesResponse, span, path=["response"])

    @parametrize
    def test_raw_response_get_aggregates(self, client: LilypadSDK) -> None:
        response = client.projects.generations.spans.with_raw_response.get_aggregates(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanGetAggregatesResponse, span, path=["response"])

    @parametrize
    def test_streaming_response_get_aggregates(self, client: LilypadSDK) -> None:
        with client.projects.generations.spans.with_streaming_response.get_aggregates(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanGetAggregatesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_aggregates(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.generations.spans.with_raw_response.get_aggregates(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                time_frame="day",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            client.projects.generations.spans.with_raw_response.get_aggregates(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                time_frame="day",
            )


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLilypadSDK) -> None:
        span = await async_client.projects.generations.spans.list(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanListResponse, span, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.projects.generations.spans.with_raw_response.list(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanListResponse, span, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.projects.generations.spans.with_streaming_response.list(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanListResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.generations.spans.with_raw_response.list(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            await async_client.projects.generations.spans.with_raw_response.list(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_aggregates(self, async_client: AsyncLilypadSDK) -> None:
        span = await async_client.projects.generations.spans.get_aggregates(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )
        assert_matches_type(SpanGetAggregatesResponse, span, path=["response"])

    @parametrize
    async def test_raw_response_get_aggregates(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.projects.generations.spans.with_raw_response.get_aggregates(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanGetAggregatesResponse, span, path=["response"])

    @parametrize
    async def test_streaming_response_get_aggregates(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.projects.generations.spans.with_streaming_response.get_aggregates(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanGetAggregatesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_aggregates(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.generations.spans.with_raw_response.get_aggregates(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                time_frame="day",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            await async_client.projects.generations.spans.with_raw_response.get_aggregates(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                time_frame="day",
            )
