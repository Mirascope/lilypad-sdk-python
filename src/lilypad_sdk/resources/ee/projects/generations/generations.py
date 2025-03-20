# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from .name import (
    NameResource,
    AsyncNameResource,
    NameResourceWithRawResponse,
    AsyncNameResourceWithRawResponse,
    NameResourceWithStreamingResponse,
    AsyncNameResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ee.projects import generation_run_version_params
from .....types.ee.generation_create_param import GenerationCreateParam
from .....types.ee.projects.generation_get_annotations_response import GenerationGetAnnotationsResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def name(self) -> NameResource:
        return NameResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)

    def get_annotations(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationGetAnnotationsResponse:
        """
        Get annotations by generations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return self._get(
            f"/ee/projects/{project_uuid}/generations/{generation_uuid}/annotations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationGetAnnotationsResponse,
        )

    def run_version(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        arg_values: Dict[str, Union[float, bool, str, Iterable[object], object]],
        model: str,
        provider: Literal["openai", "anthropic", "openrouter", "gemini"],
        generation: Optional[GenerationCreateParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Run version.

        Args:
          provider: Provider name enum

          generation: Generation create model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return self._post(
            f"/ee/projects/{project_uuid}/generations/{generation_uuid}/run",
            body=maybe_transform(
                {
                    "arg_values": arg_values,
                    "model": model,
                    "provider": provider,
                    "generation": generation,
                },
                generation_run_version_params.GenerationRunVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def name(self) -> AsyncNameResource:
        return AsyncNameResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def get_annotations(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationGetAnnotationsResponse:
        """
        Get annotations by generations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return await self._get(
            f"/ee/projects/{project_uuid}/generations/{generation_uuid}/annotations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationGetAnnotationsResponse,
        )

    async def run_version(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        arg_values: Dict[str, Union[float, bool, str, Iterable[object], object]],
        model: str,
        provider: Literal["openai", "anthropic", "openrouter", "gemini"],
        generation: Optional[GenerationCreateParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Run version.

        Args:
          provider: Provider name enum

          generation: Generation create model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return await self._post(
            f"/ee/projects/{project_uuid}/generations/{generation_uuid}/run",
            body=await async_maybe_transform(
                {
                    "arg_values": arg_values,
                    "model": model,
                    "provider": provider,
                    "generation": generation,
                },
                generation_run_version_params.GenerationRunVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.get_annotations = to_raw_response_wrapper(
            generations.get_annotations,
        )
        self.run_version = to_raw_response_wrapper(
            generations.run_version,
        )

    @cached_property
    def name(self) -> NameResourceWithRawResponse:
        return NameResourceWithRawResponse(self._generations.name)


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.get_annotations = async_to_raw_response_wrapper(
            generations.get_annotations,
        )
        self.run_version = async_to_raw_response_wrapper(
            generations.run_version,
        )

    @cached_property
    def name(self) -> AsyncNameResourceWithRawResponse:
        return AsyncNameResourceWithRawResponse(self._generations.name)


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.get_annotations = to_streamed_response_wrapper(
            generations.get_annotations,
        )
        self.run_version = to_streamed_response_wrapper(
            generations.run_version,
        )

    @cached_property
    def name(self) -> NameResourceWithStreamingResponse:
        return NameResourceWithStreamingResponse(self._generations.name)


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.get_annotations = async_to_streamed_response_wrapper(
            generations.get_annotations,
        )
        self.run_version = async_to_streamed_response_wrapper(
            generations.run_version,
        )

    @cached_property
    def name(self) -> AsyncNameResourceWithStreamingResponse:
        return AsyncNameResourceWithStreamingResponse(self._generations.name)
