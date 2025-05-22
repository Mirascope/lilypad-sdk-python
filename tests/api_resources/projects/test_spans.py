# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import SpanMoreDetails
from lilypad.types.projects import (
    SpanDeleteResponse,
    SpanSearchTracesResponse,
    SpanRetrieveAggregatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Lilypad) -> None:
        span = client.projects.spans.delete(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanDeleteResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.delete(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanDeleteResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.delete(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanDeleteResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.delete(
                span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            client.projects.spans.with_raw_response.delete(
                span_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_aggregates(self, client: Lilypad) -> None:
        span = client.projects.spans.retrieve_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )
        assert_matches_type(SpanRetrieveAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_aggregates(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.retrieve_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanRetrieveAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_aggregates(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.retrieve_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanRetrieveAggregatesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_aggregates(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.retrieve_aggregates(
                project_uuid="",
                time_frame="day",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_id(self, client: Lilypad) -> None:
        span = client.projects.spans.retrieve_by_id(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_id(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.retrieve_by_id(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_id(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.retrieve_by_id(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanMoreDetails, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_id(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.retrieve_by_id(
                span_id="span_id",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.projects.spans.with_raw_response.retrieve_by_id(
                span_id="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_search_traces(self, client: Lilypad) -> None:
        span = client.projects.spans.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_traces_with_all_params(self, client: Lilypad) -> None:
        span = client.projects.spans.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            query_string="query_string",
            scope="lilypad",
            time_range_end=0,
            time_range_start=0,
            type="type",
        )
        assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search_traces(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search_traces(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_search_traces(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.search_traces(
                project_uuid="",
            )


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.delete(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanDeleteResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.delete(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanDeleteResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.delete(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanDeleteResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.delete(
                span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.delete(
                span_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_aggregates(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.retrieve_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )
        assert_matches_type(SpanRetrieveAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_aggregates(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.retrieve_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanRetrieveAggregatesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_aggregates(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.retrieve_aggregates(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time_frame="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanRetrieveAggregatesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_aggregates(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.retrieve_aggregates(
                project_uuid="",
                time_frame="day",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_id(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.retrieve_by_id(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_id(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.retrieve_by_id(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_id(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.retrieve_by_id(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanMoreDetails, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_id(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.retrieve_by_id(
                span_id="span_id",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.projects.spans.with_raw_response.retrieve_by_id(
                span_id="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_traces(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_traces_with_all_params(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            query_string="query_string",
            scope="lilypad",
            time_range_end=0,
            time_range_start=0,
            type="type",
        )
        assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search_traces(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search_traces(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.search_traces(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanSearchTracesResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_search_traces(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.search_traces(
                project_uuid="",
            )
