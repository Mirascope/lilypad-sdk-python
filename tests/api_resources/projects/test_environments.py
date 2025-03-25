# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types.projects import (
    DeploymentPublic,
    EnvironmentRetrieveDeploymentHistoryResponse,
)
from lilypad.types.projects.functions import FunctionPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_deploy(self, client: Lilypad) -> None:
        environment = client.projects.environments.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_deploy_with_all_params(self, client: Lilypad) -> None:
        environment = client.projects.environments.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_deploy(self, client: Lilypad) -> None:
        response = client.projects.environments.with_raw_response.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_deploy(self, client: Lilypad) -> None:
        with client.projects.environments.with_streaming_response.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_deploy(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.environments.with_raw_response.deploy(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.projects.environments.with_raw_response.deploy(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_active_deployment(self, client: Lilypad) -> None:
        environment = client.projects.environments.retrieve_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_active_deployment(self, client: Lilypad) -> None:
        response = client.projects.environments.with_raw_response.retrieve_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_active_deployment(self, client: Lilypad) -> None:
        with client.projects.environments.with_streaming_response.retrieve_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_active_deployment(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.environments.with_raw_response.retrieve_active_deployment(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.projects.environments.with_raw_response.retrieve_active_deployment(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_active_function(self, client: Lilypad) -> None:
        environment = client.projects.environments.retrieve_active_function(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_active_function(self, client: Lilypad) -> None:
        response = client.projects.environments.with_raw_response.retrieve_active_function(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(FunctionPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_active_function(self, client: Lilypad) -> None:
        with client.projects.environments.with_streaming_response.retrieve_active_function(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(FunctionPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_active_function(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.environments.with_raw_response.retrieve_active_function(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.projects.environments.with_raw_response.retrieve_active_function(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_deployment_history(self, client: Lilypad) -> None:
        environment = client.projects.environments.retrieve_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentRetrieveDeploymentHistoryResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_deployment_history(self, client: Lilypad) -> None:
        response = client.projects.environments.with_raw_response.retrieve_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRetrieveDeploymentHistoryResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_deployment_history(self, client: Lilypad) -> None:
        with client.projects.environments.with_streaming_response.retrieve_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRetrieveDeploymentHistoryResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_deployment_history(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            client.projects.environments.with_raw_response.retrieve_deployment_history(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            client.projects.environments.with_raw_response.retrieve_deployment_history(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_deploy(self, async_client: AsyncLilypad) -> None:
        environment = await async_client.projects.environments.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_deploy_with_all_params(self, async_client: AsyncLilypad) -> None:
        environment = await async_client.projects.environments.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_deploy(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.environments.with_raw_response.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_deploy(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.environments.with_streaming_response.deploy(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_deploy(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.deploy(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.deploy(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_active_deployment(self, async_client: AsyncLilypad) -> None:
        environment = await async_client.projects.environments.retrieve_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_active_deployment(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.environments.with_raw_response.retrieve_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(DeploymentPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_active_deployment(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.environments.with_streaming_response.retrieve_active_deployment(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(DeploymentPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_active_deployment(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.retrieve_active_deployment(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.retrieve_active_deployment(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_active_function(self, async_client: AsyncLilypad) -> None:
        environment = await async_client.projects.environments.retrieve_active_function(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_active_function(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.environments.with_raw_response.retrieve_active_function(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(FunctionPublic, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_active_function(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.environments.with_streaming_response.retrieve_active_function(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(FunctionPublic, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_active_function(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.retrieve_active_function(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.retrieve_active_function(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_deployment_history(self, async_client: AsyncLilypad) -> None:
        environment = await async_client.projects.environments.retrieve_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentRetrieveDeploymentHistoryResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_deployment_history(self, async_client: AsyncLilypad) -> None:
        response = await async_client.projects.environments.with_raw_response.retrieve_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRetrieveDeploymentHistoryResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_deployment_history(self, async_client: AsyncLilypad) -> None:
        async with async_client.projects.environments.with_streaming_response.retrieve_deployment_history(
            environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRetrieveDeploymentHistoryResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_deployment_history(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.retrieve_deployment_history(
                environment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_uuid` but received ''"):
            await async_client.projects.environments.with_raw_response.retrieve_deployment_history(
                environment_uuid="",
                project_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
