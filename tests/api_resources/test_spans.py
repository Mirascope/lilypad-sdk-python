# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import SpanMoreDetails, SpanListCommentsResponse
from lilypad._utils import parse_datetime
from lilypad.types.projects.functions import SpanPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        span = client.spans.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.spans.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.spans.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanMoreDetails, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            client.spans.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Lilypad) -> None:
        span = client.spans.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Lilypad) -> None:
        span = client.spans.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tags=[
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "x",
                    "organization_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "project_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Lilypad) -> None:
        response = client.spans.with_raw_response.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Lilypad) -> None:
        with client.spans.with_streaming_response.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanPublic, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            client.spans.with_raw_response.update(
                span_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_comments(self, client: Lilypad) -> None:
        span = client.spans.list_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanListCommentsResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_comments(self, client: Lilypad) -> None:
        response = client.spans.with_raw_response.list_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanListCommentsResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_comments(self, client: Lilypad) -> None:
        with client.spans.with_streaming_response.list_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanListCommentsResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_comments(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            client.spans.with_raw_response.list_comments(
                "",
            )


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        span = await async_client.spans.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.spans.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanMoreDetails, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.spans.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanMoreDetails, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            await async_client.spans.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypad) -> None:
        span = await async_client.spans.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLilypad) -> None:
        span = await async_client.spans.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tags=[
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "x",
                    "organization_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "project_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypad) -> None:
        response = await async_client.spans.with_raw_response.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanPublic, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypad) -> None:
        async with async_client.spans.with_streaming_response.update(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanPublic, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            await async_client.spans.with_raw_response.update(
                span_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_comments(self, async_client: AsyncLilypad) -> None:
        span = await async_client.spans.list_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpanListCommentsResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_comments(self, async_client: AsyncLilypad) -> None:
        response = await async_client.spans.with_raw_response.list_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanListCommentsResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_comments(self, async_client: AsyncLilypad) -> None:
        async with async_client.spans.with_streaming_response.list_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanListCommentsResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_comments(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            await async_client.spans.with_raw_response.list_comments(
                "",
            )
