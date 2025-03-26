# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import environment_deploy_params
from ...types.projects.deployment_public import DeploymentPublic
from ...types.projects.functions.function_public import FunctionPublic
from ...types.projects.environment_retrieve_deployment_history_response import (
    EnvironmentRetrieveDeploymentHistoryResponse,
)

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def deploy(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        function_uuid: str,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentPublic:
        """
        Deploy a function to an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return self._post(
            f"/projects/{project_uuid}/environments/{environment_uuid}/deploy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "function_uuid": function_uuid,
                        "notes": notes,
                    },
                    environment_deploy_params.EnvironmentDeployParams,
                ),
            ),
            cast_to=DeploymentPublic,
        )

    def retrieve_active_deployment(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentPublic:
        """
        Get active deployment for an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/environments/{environment_uuid}/deployment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentPublic,
        )

    def retrieve_active_function(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionPublic:
        """
        Get the currently active function for an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/environments/{environment_uuid}/function",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionPublic,
        )

    def retrieve_deployment_history(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveDeploymentHistoryResponse:
        """
        Get deployment history for an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/environments/{environment_uuid}/history",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentRetrieveDeploymentHistoryResponse,
        )


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def deploy(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        function_uuid: str,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentPublic:
        """
        Deploy a function to an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return await self._post(
            f"/projects/{project_uuid}/environments/{environment_uuid}/deploy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "function_uuid": function_uuid,
                        "notes": notes,
                    },
                    environment_deploy_params.EnvironmentDeployParams,
                ),
            ),
            cast_to=DeploymentPublic,
        )

    async def retrieve_active_deployment(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentPublic:
        """
        Get active deployment for an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/environments/{environment_uuid}/deployment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentPublic,
        )

    async def retrieve_active_function(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionPublic:
        """
        Get the currently active function for an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/environments/{environment_uuid}/function",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionPublic,
        )

    async def retrieve_deployment_history(
        self,
        environment_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveDeploymentHistoryResponse:
        """
        Get deployment history for an environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not environment_uuid:
            raise ValueError(f"Expected a non-empty value for `environment_uuid` but received {environment_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/environments/{environment_uuid}/history",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentRetrieveDeploymentHistoryResponse,
        )


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.deploy = to_raw_response_wrapper(
            environments.deploy,
        )
        self.retrieve_active_deployment = to_raw_response_wrapper(
            environments.retrieve_active_deployment,
        )
        self.retrieve_active_function = to_raw_response_wrapper(
            environments.retrieve_active_function,
        )
        self.retrieve_deployment_history = to_raw_response_wrapper(
            environments.retrieve_deployment_history,
        )


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.deploy = async_to_raw_response_wrapper(
            environments.deploy,
        )
        self.retrieve_active_deployment = async_to_raw_response_wrapper(
            environments.retrieve_active_deployment,
        )
        self.retrieve_active_function = async_to_raw_response_wrapper(
            environments.retrieve_active_function,
        )
        self.retrieve_deployment_history = async_to_raw_response_wrapper(
            environments.retrieve_deployment_history,
        )


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.deploy = to_streamed_response_wrapper(
            environments.deploy,
        )
        self.retrieve_active_deployment = to_streamed_response_wrapper(
            environments.retrieve_active_deployment,
        )
        self.retrieve_active_function = to_streamed_response_wrapper(
            environments.retrieve_active_function,
        )
        self.retrieve_deployment_history = to_streamed_response_wrapper(
            environments.retrieve_deployment_history,
        )


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.deploy = async_to_streamed_response_wrapper(
            environments.deploy,
        )
        self.retrieve_active_deployment = async_to_streamed_response_wrapper(
            environments.retrieve_active_deployment,
        )
        self.retrieve_active_function = async_to_streamed_response_wrapper(
            environments.retrieve_active_function,
        )
        self.retrieve_deployment_history = async_to_streamed_response_wrapper(
            environments.retrieve_deployment_history,
        )
