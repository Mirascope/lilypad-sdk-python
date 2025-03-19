# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk._utils import parse_datetime
from lilypad_sdk.types.ee.projects import GenerationPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_managed_generation(self, client: LilypadSDK) -> None:
        project = client.ee.projects.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )
        assert_matches_type(GenerationPublic, project, path=["response"])

    @parametrize
    def test_method_create_managed_generation_with_all_params(self, client: LilypadSDK) -> None:
        project = client.ee.projects.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
            archived=parse_datetime("2019-12-27T18:11:19.117Z"),
            arg_types={"foo": "string"},
            call_params={
                "frequency_penalty": 0,
                "max_tokens": 0,
                "presence_penalty": 0,
                "seed": 0,
                "stop": "string",
                "temperature": 0,
                "top_p": 0,
            },
            custom_id="custom_id",
            dependencies={
                "foo": {
                    "extras": ["string"],
                    "version": "version",
                }
            },
            is_default=True,
            is_managed=True,
            model="model",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt_template="prompt_template",
            provider="provider",
            version_num=0,
        )
        assert_matches_type(GenerationPublic, project, path=["response"])

    @parametrize
    def test_raw_response_create_managed_generation(self, client: LilypadSDK) -> None:
        response = client.ee.projects.with_raw_response.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(GenerationPublic, project, path=["response"])

    @parametrize
    def test_streaming_response_create_managed_generation(self, client: LilypadSDK) -> None:
        with client.ee.projects.with_streaming_response.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(GenerationPublic, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_managed_generation(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid_1` but received ''"):
            client.ee.projects.with_raw_response.create_managed_generation(
                project_uuid_1="",
                code="code",
                hash="hash",
                name="x",
                signature="signature",
                project_uuid_2="",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_managed_generation(self, async_client: AsyncLilypadSDK) -> None:
        project = await async_client.ee.projects.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )
        assert_matches_type(GenerationPublic, project, path=["response"])

    @parametrize
    async def test_method_create_managed_generation_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        project = await async_client.ee.projects.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
            archived=parse_datetime("2019-12-27T18:11:19.117Z"),
            arg_types={"foo": "string"},
            call_params={
                "frequency_penalty": 0,
                "max_tokens": 0,
                "presence_penalty": 0,
                "seed": 0,
                "stop": "string",
                "temperature": 0,
                "top_p": 0,
            },
            custom_id="custom_id",
            dependencies={
                "foo": {
                    "extras": ["string"],
                    "version": "version",
                }
            },
            is_default=True,
            is_managed=True,
            model="model",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt_template="prompt_template",
            provider="provider",
            version_num=0,
        )
        assert_matches_type(GenerationPublic, project, path=["response"])

    @parametrize
    async def test_raw_response_create_managed_generation(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.with_raw_response.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(GenerationPublic, project, path=["response"])

    @parametrize
    async def test_streaming_response_create_managed_generation(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.with_streaming_response.create_managed_generation(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(GenerationPublic, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_managed_generation(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid_1` but received ''"):
            await async_client.ee.projects.with_raw_response.create_managed_generation(
                project_uuid_1="",
                code="code",
                hash="hash",
                name="x",
                signature="signature",
                project_uuid_2="",
            )
