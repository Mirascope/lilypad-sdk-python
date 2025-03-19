# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad_sdk import LilypadSDK, AsyncLilypadSDK
from tests.utils import assert_matches_type
from lilypad_sdk.types.ee.projects import (
    DeploymentPublic,
    GenerationPublic,
    EnvironmentPublic,
    EnvironmentListResponse,
    EnvironmentDeleteResponse,
    EnvironmentGetDeploymentHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            is_default=True,
        )
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid_1` but received ''"):
            client.ee.projects.environments.with_raw_response.create(
                project_uuid_1="",
                name="name",
                project_uuid_2="",
            )

    @parametrize
    def test_method_retrieve(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.retrieve(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.retrieve(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.retrieve(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.retrieve(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.retrieve(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.delete(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.delete(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.delete(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.delete(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.delete(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_deploy_generation(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    def test_method_deploy_generation_with_all_params(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    def test_raw_response_deploy_generation(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    def test_streaming_response_deploy_generation(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deploy_generation(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.deploy_generation(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.deploy_generation(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_active_deployment(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.get_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    def test_raw_response_get_active_deployment(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.get_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    def test_streaming_response_get_active_deployment(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.get_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_active_deployment(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.get_active_deployment(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.get_active_deployment(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_deployment_history(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.get_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentGetDeploymentHistoryResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_get_deployment_history(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.get_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentGetDeploymentHistoryResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_get_deployment_history(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.get_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentGetDeploymentHistoryResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_deployment_history(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.get_deployment_history(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.get_deployment_history(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_environment_generation(self, client: LilypadSDK) -> None:
        environment = client.ee.projects.environments.get_environment_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationPublic, environment, path=["response"])

    @parametrize
    def test_raw_response_get_environment_generation(self, client: LilypadSDK) -> None:
        response = client.ee.projects.environments.with_raw_response.get_environment_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(GenerationPublic, environment, path=["response"])

    @parametrize
    def test_streaming_response_get_environment_generation(self, client: LilypadSDK) -> None:
        with client.ee.projects.environments.with_streaming_response.get_environment_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(GenerationPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_environment_generation(self, client: LilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.get_environment_generation(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.ee.projects.environments.with_raw_response.get_environment_generation(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            is_default=True,
        )
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.create(
            project_uuid_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            project_uuid_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid_1` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.create(
                project_uuid_1="",
                name="name",
                project_uuid_2="",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.retrieve(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.retrieve(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentPublic, environment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.retrieve(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.retrieve(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.retrieve(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.delete(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.delete(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.delete(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.delete(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.delete(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_deploy_generation(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    async def test_method_deploy_generation_with_all_params(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    async def test_raw_response_deploy_generation(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    async def test_streaming_response_deploy_generation(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.deploy_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deploy_generation(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.deploy_generation(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.deploy_generation(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                generation_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_active_deployment(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.get_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    async def test_raw_response_get_active_deployment(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.get_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @parametrize
    async def test_streaming_response_get_active_deployment(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.get_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_active_deployment(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.get_active_deployment(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.get_active_deployment(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_deployment_history(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.get_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentGetDeploymentHistoryResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_get_deployment_history(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.get_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentGetDeploymentHistoryResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_get_deployment_history(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.get_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentGetDeploymentHistoryResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_deployment_history(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.get_deployment_history(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.get_deployment_history(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_environment_generation(self, async_client: AsyncLilypadSDK) -> None:
        environment = await async_client.ee.projects.environments.get_environment_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationPublic, environment, path=["response"])

    @parametrize
    async def test_raw_response_get_environment_generation(self, async_client: AsyncLilypadSDK) -> None:
        response = await async_client.ee.projects.environments.with_raw_response.get_environment_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(GenerationPublic, environment, path=["response"])

    @parametrize
    async def test_streaming_response_get_environment_generation(self, async_client: AsyncLilypadSDK) -> None:
        async with async_client.ee.projects.environments.with_streaming_response.get_environment_generation(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(GenerationPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_environment_generation(self, async_client: AsyncLilypadSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.get_environment_generation(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.ee.projects.environments.with_raw_response.get_environment_generation(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
