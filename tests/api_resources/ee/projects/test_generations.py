# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk._utils import parse_datetime
from lilypad_sdk.types.ee.projects import (
    GenerationGetAnnotationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_annotations(self, client: LilypadSDK) -> None:
        generation = client.ee.projects.generations.get_annotations(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationGetAnnotationsResponse, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_annotations(self, client: LilypadSDK) -> None:
        response = client.ee.projects.generations.with_raw_response.get_annotations(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationGetAnnotationsResponse, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_annotations(self, client: LilypadSDK) -> None:
        with client.ee.projects.generations.with_streaming_response.get_annotations(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationGetAnnotationsResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_annotations(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.generations.with_raw_response.get_annotations(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            client.ee.projects.generations.with_raw_response.get_annotations(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_playground(self, client: LilypadSDK) -> None:
        generation = client.ee.projects.generations.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )
        assert_matches_type(str, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_playground_with_all_params(self, client: LilypadSDK) -> None:
        generation = client.ee.projects.generations.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
            generation={
                "code": "code",
                "hash": "hash",
                "name": "x",
                "signature": "signature",
                "archived": parse_datetime("2019-12-27T18:11:19.117Z"),
                "arg_types": {"foo": "string"},
                "call_params": {
                    "frequency_penalty": 0,
                    "max_tokens": 0,
                    "presence_penalty": 0,
                    "seed": 0,
                    "stop": "string",
                    "temperature": 0,
                    "top_p": 0,
                },
                "custom_id": "custom_id",
                "dependencies": {
                    "foo": {
                        "extras": ["string"],
                        "version": "version",
                    }
                },
                "is_default": True,
                "is_managed": True,
                "model": "model",
                "project_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt_template": "prompt_template",
                "provider": "provider",
                "version_num": 0,
            },
        )
        assert_matches_type(str, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_playground(self, client: LilypadSDK) -> None:
        response = client.ee.projects.generations.with_raw_response.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(str, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_playground(self, client: LilypadSDK) -> None:
        with client.ee.projects.generations.with_streaming_response.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(str, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_playground(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.generations.with_raw_response.run_playground(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            client.ee.projects.generations.with_raw_response.run_playground(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_annotations(self, async_client: AsyncLilypadSDK) -> None:
        generation = await async_client.ee.projects.generations.get_annotations(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationGetAnnotationsResponse, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_annotations(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.generations.with_raw_response.get_annotations(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationGetAnnotationsResponse, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_annotations(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.generations.with_streaming_response.get_annotations(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationGetAnnotationsResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_annotations(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.generations.with_raw_response.get_annotations(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            await async_client.ee.projects.generations.with_raw_response.get_annotations(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_playground(self, async_client: AsyncLilypadSDK) -> None:
        generation = await async_client.ee.projects.generations.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )
        assert_matches_type(str, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_playground_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        generation = await async_client.ee.projects.generations.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
            generation={
                "code": "code",
                "hash": "hash",
                "name": "x",
                "signature": "signature",
                "archived": parse_datetime("2019-12-27T18:11:19.117Z"),
                "arg_types": {"foo": "string"},
                "call_params": {
                    "frequency_penalty": 0,
                    "max_tokens": 0,
                    "presence_penalty": 0,
                    "seed": 0,
                    "stop": "string",
                    "temperature": 0,
                    "top_p": 0,
                },
                "custom_id": "custom_id",
                "dependencies": {
                    "foo": {
                        "extras": ["string"],
                        "version": "version",
                    }
                },
                "is_default": True,
                "is_managed": True,
                "model": "model",
                "project_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt_template": "prompt_template",
                "provider": "provider",
                "version_num": 0,
            },
        )
        assert_matches_type(str, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_playground(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.generations.with_raw_response.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(str, generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_playground(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.generations.with_streaming_response.run_playground(
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(str, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_playground(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.generations.with_raw_response.run_playground(
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_uuid` but received ''"):
            await async_client.ee.projects.generations.with_raw_response.run_playground(
                generation_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )
