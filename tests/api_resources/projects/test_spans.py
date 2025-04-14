# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.projects import SpanListAggregatesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_aggregates(self, client: Lilypad) -> None:
        span = client.projects.spans.list_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )
        assert_matches_type(SpanListAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_aggregates(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.list_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanListAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_aggregates(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.list_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanListAggregatesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_aggregates(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.list_aggregates(
                project_uuid="",
                time_frame="day",
            )


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_aggregates(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.list_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )
        assert_matches_type(SpanListAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_aggregates(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.list_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanListAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_aggregates(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.list_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanListAggregatesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_aggregates(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.list_aggregates(
                project_uuid="",
                time_frame="day",
            )
