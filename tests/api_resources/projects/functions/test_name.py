# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.projects.functions import FunctionPublic, NameRetrieveByNameResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_name(self, client: Lilypad) -> None:
        name = client.projects.functions.name.retrieve_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NameRetrieveByNameResponse, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_name(self, client: Lilypad) -> None:
        response = client.projects.functions.name.with_raw_response.retrieve_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(NameRetrieveByNameResponse, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: Lilypad) -> None:
        with client.projects.functions.name.with_streaming_response.retrieve_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(NameRetrieveByNameResponse, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_name(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.name.with_raw_response.retrieve_by_name(
                function_name="function_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.projects.functions.name.with_raw_response.retrieve_by_name(
                function_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_version(self, client: Lilypad) -> None:
        name = client.projects.functions.name.retrieve_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
        )
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_version(self, client: Lilypad) -> None:
        response = client.projects.functions.name.with_raw_response.retrieve_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_version(self, client: Lilypad) -> None:
        with client.projects.functions.name.with_streaming_response.retrieve_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(FunctionPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_version(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.name.with_raw_response.retrieve_by_version(
                version_num=0,
                project_uuid="",
                function_name="function_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.projects.functions.name.with_raw_response.retrieve_by_version(
                version_num=0,
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_name="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_deployed(self, client: Lilypad) -> None:
        name = client.projects.functions.name.retrieve_deployed(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_deployed(self, client: Lilypad) -> None:
        response = client.projects.functions.name.with_raw_response.retrieve_deployed(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_deployed(self, client: Lilypad) -> None:
        with client.projects.functions.name.with_streaming_response.retrieve_deployed(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(FunctionPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_deployed(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.functions.name.with_raw_response.retrieve_deployed(
                function_name="function_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.projects.functions.name.with_raw_response.retrieve_deployed(
                function_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncName:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncLilypad) -> None:
        name = await async_client.projects.functions.name.retrieve_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NameRetrieveByNameResponse, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.name.with_raw_response.retrieve_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(NameRetrieveByNameResponse, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.name.with_streaming_response.retrieve_by_name(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(NameRetrieveByNameResponse, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_name(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.name.with_raw_response.retrieve_by_name(
                function_name="function_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.projects.functions.name.with_raw_response.retrieve_by_name(
                function_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_version(self, async_client: AsyncLilypad) -> None:
        name = await async_client.projects.functions.name.retrieve_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
        )
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_version(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.name.with_raw_response.retrieve_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_version(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.name.with_streaming_response.retrieve_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(FunctionPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_version(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.name.with_raw_response.retrieve_by_version(
                version_num=0,
                project_uuid="",
                function_name="function_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.projects.functions.name.with_raw_response.retrieve_by_version(
                version_num=0,
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_name="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_deployed(self, async_client: AsyncLilypad) -> None:
        name = await async_client.projects.functions.name.retrieve_deployed(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_deployed(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.functions.name.with_raw_response.retrieve_deployed(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(FunctionPublic, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_deployed(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.functions.name.with_streaming_response.retrieve_deployed(
            function_name="function_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(FunctionPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_deployed(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.functions.name.with_raw_response.retrieve_deployed(
                function_name="function_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.projects.functions.name.with_raw_response.retrieve_deployed(
                function_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
