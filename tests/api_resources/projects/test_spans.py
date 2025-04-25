# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import SpanMoreDetails
from lilypad.types.projects import (
    SpanListResponse,
    SpanDeleteResponse,
    SpanListAggregatesResponse,
)
from lilypad.types.projects.functions import SpanPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        span = client.projects.spans.retrieve(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.retrieve(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.retrieve(
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
    def test_path_params_retrieve(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.retrieve(
                span_id="span_id",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.projects.spans.with_raw_response.retrieve(
                span_id="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Lilypad) -> None:
        span = client.projects.spans.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
        )
        assert_matches_type(SpanListResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Lilypad) -> None:
        span = client.projects.spans.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
            limit=0,
            scope="lilypad",
            time_range_end=0,
            time_range_start=0,
            type="type",
        )
        assert_matches_type(SpanListResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanListResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanListResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.spans.with_raw_response.list(
                project_uuid="",
                query_string="query_string",
            )

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

    @pytest.mark.skip()
    @parametrize
    def test_method_update_tags(self, client: Lilypad) -> None:
        span = client.projects.spans.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_tags_with_all_params(self, client: Lilypad) -> None:
        span = client.projects.spans.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tags_by_name=["string"],
            tags_by_uuid=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_tags(self, client: Lilypad) -> None:
        response = client.projects.spans.with_raw_response.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_tags(self, client: Lilypad) -> None:
        with client.projects.spans.with_streaming_response.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanPublic, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_tags(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            client.projects.spans.with_raw_response.update_tags(
                span_uuid="",
            )


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.retrieve(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.retrieve(
            span_id="span_id",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.retrieve(
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
    async def test_path_params_retrieve(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.retrieve(
                span_id="span_id",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.projects.spans.with_raw_response.retrieve(
                span_id="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
        )
        assert_matches_type(SpanListResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
            limit=0,
            scope="lilypad",
            time_range_end=0,
            time_range_start=0,
            type="type",
        )
        assert_matches_type(SpanListResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanListResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.list(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_string="query_string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanListResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.list(
                project_uuid="",
                query_string="query_string",
            )

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

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_tags(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_tags_with_all_params(self, async_client: AsyncLilypad) -> None:
        span = await async_client.projects.spans.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tags_by_name=["string"],
            tags_by_uuid=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_tags(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.spans.with_raw_response.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_tags(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.spans.with_streaming_response.update_tags(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanPublic, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_tags(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            await async_client.projects.spans.with_raw_response.update_tags(
                span_uuid="",
            )
