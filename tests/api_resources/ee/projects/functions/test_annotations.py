# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.ee.projects.functions import AnnotationListResponse, AnnotationGetMetricsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Lilypad) -> None:
        annotation = client.ee.projects.functions.annotations.list(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Lilypad) -> None:
        response = client.ee.projects.functions.annotations.with_raw_response.list(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Lilypad) -> None:
        with client.ee.projects.functions.annotations.with_streaming_response.list(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(AnnotationListResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.functions.annotations.with_raw_response.list(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.ee.projects.functions.annotations.with_raw_response.list(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_metrics(self, client: Lilypad) -> None:
        annotation = client.ee.projects.functions.annotations.get_metrics(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationGetMetricsResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_metrics(self, client: Lilypad) -> None:
        response = client.ee.projects.functions.annotations.with_raw_response.get_metrics(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(AnnotationGetMetricsResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_metrics(self, client: Lilypad) -> None:
        with client.ee.projects.functions.annotations.with_streaming_response.get_metrics(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(AnnotationGetMetricsResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_metrics(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.functions.annotations.with_raw_response.get_metrics(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.ee.projects.functions.annotations.with_raw_response.get_metrics(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncAnnotations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLilypad) -> None:
        annotation = await async_client.ee.projects.functions.annotations.list(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.functions.annotations.with_raw_response.list(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.functions.annotations.with_streaming_response.list(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(AnnotationListResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.functions.annotations.with_raw_response.list(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.ee.projects.functions.annotations.with_raw_response.list(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_metrics(self, async_client: AsyncLilypad) -> None:
        annotation = await async_client.ee.projects.functions.annotations.get_metrics(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationGetMetricsResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_metrics(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.functions.annotations.with_raw_response.get_metrics(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(AnnotationGetMetricsResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_metrics(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.functions.annotations.with_streaming_response.get_metrics(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(AnnotationGetMetricsResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_metrics(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.functions.annotations.with_raw_response.get_metrics(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.ee.projects.functions.annotations.with_raw_response.get_metrics(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
