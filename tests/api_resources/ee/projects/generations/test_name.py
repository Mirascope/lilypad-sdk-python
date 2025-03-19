# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types.ee.projects import GenerationPublic
from lilypad_sdk.types.ee.projects.generations import NameGetByNameResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_by_name(self, client: LilypadSDK) -> None:
        name = client.ee.projects.generations.name.get_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NameGetByNameResponse, name, path=["response"])

    @parametrize
    def test_raw_response_get_by_name(self, client: LilypadSDK) -> None:
        response = client.ee.projects.generations.name.with_raw_response.get_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(NameGetByNameResponse, name, path=["response"])

    @parametrize
    def test_streaming_response_get_by_name(self, client: LilypadSDK) -> None:
        with client.ee.projects.generations.name.with_streaming_response.get_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(NameGetByNameResponse, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_name(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.generations.name.with_raw_response.get_by_name(
                generation_name="generation_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_name` but received ''"):
            client.ee.projects.generations.name.with_raw_response.get_by_name(
                generation_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_by_version(self, client: LilypadSDK) -> None:
        name = client.ee.projects.generations.name.get_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_name="generation_name",
        )
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    def test_raw_response_get_by_version(self, client: LilypadSDK) -> None:
        response = client.ee.projects.generations.name.with_raw_response.get_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_name="generation_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    def test_streaming_response_get_by_version(self, client: LilypadSDK) -> None:
        with client.ee.projects.generations.name.with_streaming_response.get_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_name="generation_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(GenerationPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_version(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.generations.name.with_raw_response.get_by_version(
                version_num=0,
                project_uuid="",
                generation_name="generation_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_name` but received ''"):
            client.ee.projects.generations.name.with_raw_response.get_by_version(
                version_num=0,
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                generation_name="",
            )

    @parametrize
    def test_method_get_deployed_by_name(self, client: LilypadSDK) -> None:
        name = client.ee.projects.generations.name.get_deployed_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    def test_raw_response_get_deployed_by_name(self, client: LilypadSDK) -> None:
        response = client.ee.projects.generations.name.with_raw_response.get_deployed_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    def test_streaming_response_get_deployed_by_name(self, client: LilypadSDK) -> None:
        with client.ee.projects.generations.name.with_streaming_response.get_deployed_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(GenerationPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_deployed_by_name(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.generations.name.with_raw_response.get_deployed_by_name(
                generation_name="generation_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_name` but received ''"):
            client.ee.projects.generations.name.with_raw_response.get_deployed_by_name(
                generation_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncName:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncLilypadSDK) -> None:
        name = await async_client.ee.projects.generations.name.get_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NameGetByNameResponse, name, path=["response"])

    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.generations.name.with_raw_response.get_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(NameGetByNameResponse, name, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.generations.name.with_streaming_response.get_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(NameGetByNameResponse, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.generations.name.with_raw_response.get_by_name(
                generation_name="generation_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_name` but received ''"):
            await async_client.ee.projects.generations.name.with_raw_response.get_by_name(
                generation_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_by_version(self, async_client: AsyncLilypadSDK) -> None:
        name = await async_client.ee.projects.generations.name.get_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_name="generation_name",
        )
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    async def test_raw_response_get_by_version(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.generations.name.with_raw_response.get_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_name="generation_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_version(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.generations.name.with_streaming_response.get_by_version(
            version_num=0,
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_name="generation_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(GenerationPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_version(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.generations.name.with_raw_response.get_by_version(
                version_num=0,
                project_uuid="",
                generation_name="generation_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_name` but received ''"):
            await async_client.ee.projects.generations.name.with_raw_response.get_by_version(
                version_num=0,
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                generation_name="",
            )

    @parametrize
    async def test_method_get_deployed_by_name(self, async_client: AsyncLilypadSDK) -> None:
        name = await async_client.ee.projects.generations.name.get_deployed_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    async def test_raw_response_get_deployed_by_name(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.generations.name.with_raw_response.get_deployed_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(GenerationPublic, name, path=["response"])

    @parametrize
    async def test_streaming_response_get_deployed_by_name(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.generations.name.with_streaming_response.get_deployed_by_name(
            generation_name="generation_name",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(GenerationPublic, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_deployed_by_name(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.generations.name.with_raw_response.get_deployed_by_name(
                generation_name="generation_name",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_name` but received ''"):
            await async_client.ee.projects.generations.name.with_raw_response.get_deployed_by_name(
                generation_name="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
