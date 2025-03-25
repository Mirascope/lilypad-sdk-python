# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad._utils import parse_datetime
from lilypad.types.ee.projects import (
    FunctionGetAnnotationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_annotations(self, client: Lilypad) -> None:
        function = client.ee.projects.functions.get_annotations(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionGetAnnotationsResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_annotations(self, client: Lilypad) -> None:
        response = client.ee.projects.functions.with_raw_response.get_annotations(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionGetAnnotationsResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_annotations(self, client: Lilypad) -> None:
        with client.ee.projects.functions.with_streaming_response.get_annotations(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionGetAnnotationsResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_annotations(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.functions.with_raw_response.get_annotations(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.ee.projects.functions.with_raw_response.get_annotations(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_playground(self, client: Lilypad) -> None:
        function = client.ee.projects.functions.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )
        assert_matches_type(str, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_playground_with_all_params(self, client: Lilypad) -> None:
        function = client.ee.projects.functions.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
            function={
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
                "is_versioned": True,
                "model": "model",
                "project_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt_template": "prompt_template",
                "provider": "provider",
                "version_num": 0,
            },
        )
        assert_matches_type(str, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_playground(self, client: Lilypad) -> None:
        response = client.ee.projects.functions.with_raw_response.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(str, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_playground(self, client: Lilypad) -> None:
        with client.ee.projects.functions.with_streaming_response.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(str, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_playground(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.functions.with_raw_response.run_playground(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.ee.projects.functions.with_raw_response.run_playground(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_annotations(self, async_client: AsyncLilypad) -> None:
        function = await async_client.ee.projects.functions.get_annotations(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionGetAnnotationsResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_annotations(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.functions.with_raw_response.get_annotations(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionGetAnnotationsResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_annotations(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.functions.with_streaming_response.get_annotations(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionGetAnnotationsResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_annotations(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.functions.with_raw_response.get_annotations(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.ee.projects.functions.with_raw_response.get_annotations(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_playground(self, async_client: AsyncLilypad) -> None:
        function = await async_client.ee.projects.functions.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )
        assert_matches_type(str, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_playground_with_all_params(self, async_client: AsyncLilypad) -> None:
        function = await async_client.ee.projects.functions.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
            function={
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
                "is_versioned": True,
                "model": "model",
                "project_uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt_template": "prompt_template",
                "provider": "provider",
                "version_num": 0,
            },
        )
        assert_matches_type(str, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_playground(self, async_client: AsyncLilypad) -> None:
        response = await async_client.ee.projects.functions.with_raw_response.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(str, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_playground(self, async_client: AsyncLilypad) -> None:
        async with async_client.ee.projects.functions.with_streaming_response.run_playground(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            arg_values={"foo": 0},
            model="model",
            provider="openai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(str, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_playground(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.functions.with_raw_response.run_playground(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.ee.projects.functions.with_raw_response.run_playground(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                arg_values={"foo": 0},
                model="model",
                provider="openai",
            )
