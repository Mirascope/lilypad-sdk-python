# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.ee.projects import (
    AnnotationPublic,
    AnnotationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        annotation = client.ee.projects.annotations.create(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{}],
        )
        assert_matches_type(AnnotationCreateResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.ee.projects.annotations.with_raw_response.create(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(AnnotationCreateResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.ee.projects.annotations.with_streaming_response.create(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(AnnotationCreateResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.annotations.with_raw_response.create(
                project_uuid="",
                body=[{}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Lilypad) -> None:
        annotation = client.ee.projects.annotations.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationPublic, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Lilypad) -> None:
        annotation = client.ee.projects.annotations.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assigned_to="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
            label="pass",
            reasoning="reasoning",
            type="manual",
        )
        assert_matches_type(AnnotationPublic, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Lilypad) -> None:
        response = client.ee.projects.annotations.with_raw_response.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(AnnotationPublic, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Lilypad) -> None:
        with client.ee.projects.annotations.with_streaming_response.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(AnnotationPublic, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.annotations.with_raw_response.update(
                annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `annotation_uuid` but received ''"):
            client.ee.projects.annotations.with_raw_response.update(
                annotation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncAnnotations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        annotation = await async_client.ee.projects.annotations.create(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{}],
        )
        assert_matches_type(AnnotationCreateResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.annotations.with_raw_response.create(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(AnnotationCreateResponse, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.annotations.with_streaming_response.create(
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(AnnotationCreateResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.annotations.with_raw_response.create(
                project_uuid="",
                body=[{}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypad) -> None:
        annotation = await async_client.ee.projects.annotations.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationPublic, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLilypad) -> None:
        annotation = await async_client.ee.projects.annotations.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assigned_to="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
            label="pass",
            reasoning="reasoning",
            type="manual",
        )
        assert_matches_type(AnnotationPublic, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.annotations.with_raw_response.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(AnnotationPublic, annotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.annotations.with_streaming_response.update(
            annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(AnnotationPublic, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.annotations.with_raw_response.update(
                annotation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `annotation_uuid` but received ''"):
            await async_client.ee.projects.annotations.with_raw_response.update(
                annotation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
