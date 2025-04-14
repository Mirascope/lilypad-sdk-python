# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_annotation(self, client: Lilypad) -> None:
        span = client.ee.projects.spans.generate_annotation(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_annotation(self, client: Lilypad) -> None:
        response = client.ee.projects.spans.with_raw_response.generate_annotation(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(object, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_annotation(self, client: Lilypad) -> None:
        with client.ee.projects.spans.with_streaming_response.generate_annotation(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(object, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_generate_annotation(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.spans.with_raw_response.generate_annotation(
                span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            client.ee.projects.spans.with_raw_response.generate_annotation(
                span_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_annotation(self, async_client: AsyncLilypad) -> None:
        span = await async_client.ee.projects.spans.generate_annotation(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_annotation(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.spans.with_raw_response.generate_annotation(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(object, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_annotation(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.spans.with_streaming_response.generate_annotation(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(object, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_generate_annotation(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.spans.with_raw_response.generate_annotation(
                span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_uuid` but received ''"):
            await async_client.ee.projects.spans.with_raw_response.generate_annotation(
                span_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
