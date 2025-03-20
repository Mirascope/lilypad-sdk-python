# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .spans import (
    SpansResource,
    AsyncSpansResource,
    SpansResourceWithRawResponse,
    AsyncSpansResourceWithRawResponse,
    SpansResourceWithStreamingResponse,
    AsyncSpansResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ....types.ee import project_create_managed_generation_params
from .annotations import (
    AnnotationsResource,
    AsyncAnnotationsResource,
    AnnotationsResourceWithRawResponse,
    AsyncAnnotationsResourceWithRawResponse,
    AnnotationsResourceWithStreamingResponse,
    AsyncAnnotationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .environments import (
    EnvironmentsResource,
    AsyncEnvironmentsResource,
    EnvironmentsResourceWithRawResponse,
    AsyncEnvironmentsResourceWithRawResponse,
    EnvironmentsResourceWithStreamingResponse,
    AsyncEnvironmentsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .generations.generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)
from ....types.ee.projects.generation_public import GenerationPublic
from ....types.ee.projects.common_call_params_param import CommonCallParamsParam

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def annotations(self) -> AnnotationsResource:
        return AnnotationsResource(self._client)

    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def spans(self) -> SpansResource:
        return SpansResource(self._client)

    @cached_property
    def environments(self) -> EnvironmentsResource:
        return EnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def create_managed_generation(
        self,
        path_project_uuid: str,
        *,
        code: str,
        hash: str,
        name: str,
        signature: str,
        archived: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        arg_types: Dict[str, str] | NotGiven = NOT_GIVEN,
        call_params: CommonCallParamsParam | NotGiven = NOT_GIVEN,
        custom_id: Optional[str] | NotGiven = NOT_GIVEN,
        dependencies: Dict[str, project_create_managed_generation_params.Dependencies] | NotGiven = NOT_GIVEN,
        is_default: Optional[bool] | NotGiven = NOT_GIVEN,
        is_managed: Optional[bool] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        body_project_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_template: Optional[str] | NotGiven = NOT_GIVEN,
        provider: Optional[str] | NotGiven = NOT_GIVEN,
        version_num: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Create a managed generation.

        Args:
          call_params: Common parameters shared across LLM providers.

              Note: Each provider may handle these parameters differently or not support them
              at all. Please check provider-specific documentation for parameter support and
              behavior.

              Attributes: temperature: Controls randomness in the output (0.0 to 1.0).
              max_tokens: Maximum number of tokens to generate. top_p: Nucleus sampling
              parameter (0.0 to 1.0). frequency_penalty: Penalizes frequent tokens (-2.0 to
              2.0). presence_penalty: Penalizes tokens based on presence (-2.0 to 2.0). seed:
              Random seed for reproducibility. stop: Stop sequence(s) to end generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_project_uuid:
            raise ValueError(f"Expected a non-empty value for `path_project_uuid` but received {path_project_uuid!r}")
        return self._post(
            f"/ee/projects/{path_project_uuid}/managed-generations",
            body=maybe_transform(
                {
                    "code": code,
                    "hash": hash,
                    "name": name,
                    "signature": signature,
                    "archived": archived,
                    "arg_types": arg_types,
                    "call_params": call_params,
                    "custom_id": custom_id,
                    "dependencies": dependencies,
                    "is_default": is_default,
                    "is_managed": is_managed,
                    "model": model,
                    "body_project_uuid": body_project_uuid,
                    "prompt_template": prompt_template,
                    "provider": provider,
                    "version_num": version_num,
                },
                project_create_managed_generation_params.ProjectCreateManagedGenerationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def annotations(self) -> AsyncAnnotationsResource:
        return AsyncAnnotationsResource(self._client)

    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def spans(self) -> AsyncSpansResource:
        return AsyncSpansResource(self._client)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResource:
        return AsyncEnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create_managed_generation(
        self,
        path_project_uuid: str,
        *,
        code: str,
        hash: str,
        name: str,
        signature: str,
        archived: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        arg_types: Dict[str, str] | NotGiven = NOT_GIVEN,
        call_params: CommonCallParamsParam | NotGiven = NOT_GIVEN,
        custom_id: Optional[str] | NotGiven = NOT_GIVEN,
        dependencies: Dict[str, project_create_managed_generation_params.Dependencies] | NotGiven = NOT_GIVEN,
        is_default: Optional[bool] | NotGiven = NOT_GIVEN,
        is_managed: Optional[bool] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        body_project_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_template: Optional[str] | NotGiven = NOT_GIVEN,
        provider: Optional[str] | NotGiven = NOT_GIVEN,
        version_num: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Create a managed generation.

        Args:
          call_params: Common parameters shared across LLM providers.

              Note: Each provider may handle these parameters differently or not support them
              at all. Please check provider-specific documentation for parameter support and
              behavior.

              Attributes: temperature: Controls randomness in the output (0.0 to 1.0).
              max_tokens: Maximum number of tokens to generate. top_p: Nucleus sampling
              parameter (0.0 to 1.0). frequency_penalty: Penalizes frequent tokens (-2.0 to
              2.0). presence_penalty: Penalizes tokens based on presence (-2.0 to 2.0). seed:
              Random seed for reproducibility. stop: Stop sequence(s) to end generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_project_uuid:
            raise ValueError(f"Expected a non-empty value for `path_project_uuid` but received {path_project_uuid!r}")
        return await self._post(
            f"/ee/projects/{path_project_uuid}/managed-generations",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "hash": hash,
                    "name": name,
                    "signature": signature,
                    "archived": archived,
                    "arg_types": arg_types,
                    "call_params": call_params,
                    "custom_id": custom_id,
                    "dependencies": dependencies,
                    "is_default": is_default,
                    "is_managed": is_managed,
                    "model": model,
                    "body_project_uuid": body_project_uuid,
                    "prompt_template": prompt_template,
                    "provider": provider,
                    "version_num": version_num,
                },
                project_create_managed_generation_params.ProjectCreateManagedGenerationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create_managed_generation = to_raw_response_wrapper(
            projects.create_managed_generation,
        )

    @cached_property
    def annotations(self) -> AnnotationsResourceWithRawResponse:
        return AnnotationsResourceWithRawResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._projects.generations)

    @cached_property
    def spans(self) -> SpansResourceWithRawResponse:
        return SpansResourceWithRawResponse(self._projects.spans)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithRawResponse:
        return EnvironmentsResourceWithRawResponse(self._projects.environments)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create_managed_generation = async_to_raw_response_wrapper(
            projects.create_managed_generation,
        )

    @cached_property
    def annotations(self) -> AsyncAnnotationsResourceWithRawResponse:
        return AsyncAnnotationsResourceWithRawResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._projects.generations)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithRawResponse:
        return AsyncSpansResourceWithRawResponse(self._projects.spans)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithRawResponse:
        return AsyncEnvironmentsResourceWithRawResponse(self._projects.environments)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create_managed_generation = to_streamed_response_wrapper(
            projects.create_managed_generation,
        )

    @cached_property
    def annotations(self) -> AnnotationsResourceWithStreamingResponse:
        return AnnotationsResourceWithStreamingResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._projects.generations)

    @cached_property
    def spans(self) -> SpansResourceWithStreamingResponse:
        return SpansResourceWithStreamingResponse(self._projects.spans)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithStreamingResponse:
        return EnvironmentsResourceWithStreamingResponse(self._projects.environments)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create_managed_generation = async_to_streamed_response_wrapper(
            projects.create_managed_generation,
        )

    @cached_property
    def annotations(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        return AsyncAnnotationsResourceWithStreamingResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._projects.generations)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithStreamingResponse:
        return AsyncSpansResourceWithStreamingResponse(self._projects.spans)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        return AsyncEnvironmentsResourceWithStreamingResponse(self._projects.environments)
