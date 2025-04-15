# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad._utils import parse_datetime
from lilypad.types.projects import (
    FunctionListResponse,
    FunctionArchiveResponse,
    FunctionArchiveByNameResponse,
)
from lilypad.types.projects.functions import FunctionPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        function = client.projects.functions.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Lilypad) -> None:
        function = client.projects.functions.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            is_versioned=True,
            model="model",
            body_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt_template="prompt_template",
            provider="provider",
            version_num=0,
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_project_uuid` but received ''"):
            client.projects.functions.with_raw_response.create(
                path_project_uuid="",
                code="code",
                hash="hash",
                name="x",
                signature="signature",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        function = client.projects.functions.retrieve(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.retrieve(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.retrieve(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.with_raw_response.retrieve(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.projects.functions.with_raw_response.retrieve(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Lilypad) -> None:
        function = client.projects.functions.update(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.update(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.update(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.with_raw_response.update(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.projects.functions.with_raw_response.update(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Lilypad) -> None:
        function = client.projects.functions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionListResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_archive(self, client: Lilypad) -> None:
        function = client.projects.functions.archive(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionArchiveResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_archive(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.archive(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionArchiveResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_archive(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.archive(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionArchiveResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_archive(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.with_raw_response.archive(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.projects.functions.with_raw_response.archive(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_archive_by_name(self, client: Lilypad) -> None:
        function = client.projects.functions.archive_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionArchiveByNameResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_archive_by_name(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.archive_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionArchiveByNameResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_archive_by_name(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.archive_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionArchiveByNameResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_archive_by_name(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.with_raw_response.archive_by_name(
                function_name="function_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.projects.functions.with_raw_response.archive_by_name(
                function_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_hash(self, client: Lilypad) -> None:
        function = client.projects.functions.retrieve_by_hash(
            function_hash="function_hash",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_hash(self, client: Lilypad) -> None:
        response = client.projects.functions.with_raw_response.retrieve_by_hash(
            function_hash="function_hash",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_hash(self, client: Lilypad) -> None:
        with client.projects.functions.with_streaming_response.retrieve_by_hash(
            function_hash="function_hash",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_hash(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.with_raw_response.retrieve_by_hash(
                function_hash="function_hash",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_hash` but received ''"):
            client.projects.functions.with_raw_response.retrieve_by_hash(
                function_hash="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            is_versioned=True,
            model="model",
            body_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt_template="prompt_template",
            provider="provider",
            version_num=0,
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.create(
            path_project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            hash="hash",
            name="x",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.create(
                path_project_uuid="",
                code="code",
                hash="hash",
                name="x",
                signature="signature",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.retrieve(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.retrieve(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.retrieve(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.retrieve(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.retrieve(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.update(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.update(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.update(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.update(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.update(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionListResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_archive(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.archive(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionArchiveResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.archive(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionArchiveResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.archive(
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionArchiveResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.archive(
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.archive(
                function_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_archive_by_name(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.archive_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionArchiveByNameResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_archive_by_name(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.archive_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionArchiveByNameResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_archive_by_name(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.archive_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionArchiveByNameResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_archive_by_name(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.archive_by_name(
                function_name="function_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.projects.functions.with_raw_response.archive_by_name(
                function_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_hash(self, async_client: AsyncLilypad) -> None:
        function = await async_client.projects.functions.retrieve_by_hash(
            function_hash="function_hash",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_hash(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.with_raw_response.retrieve_by_hash(
            function_hash="function_hash",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionPublic, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_hash(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.with_streaming_response.retrieve_by_hash(
            function_hash="function_hash",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionPublic, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_hash(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.with_raw_response.retrieve_by_hash(
                function_hash="function_hash",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_hash` but received ''"):
            await async_client.projects.functions.with_raw_response.retrieve_by_hash(
                function_hash="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
