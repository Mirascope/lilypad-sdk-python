# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ee.projects.generation_public import GenerationPublic
from .....types.ee.projects.generations.name_get_by_name_response import NameGetByNameResponse

__all__ = ["NameResource", "AsyncNameResource"]


class NameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return NameResourceWithStreamingResponse(self)

    def get_by_name(
        self,
        generation_name: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameGetByNameResponse:
        """
        Get generation by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return self._get(
            f"/ee/projects/{project_uuid}/generations/name/{generation_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameGetByNameResponse,
        )

    def get_by_version(
        self,
        version_num: int,
        *,
        project_uuid: str,
        generation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Get generation by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return self._get(
            f"/ee/projects/{project_uuid}/generations/name/{generation_name}/version/{version_num}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    def get_deployed_by_name(
        self,
        generation_name: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Get the deployed generation by generation name and environment name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return self._get(
            f"/ee/projects/{project_uuid}/generations/name/{generation_name}/environments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )


class AsyncNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncNameResourceWithStreamingResponse(self)

    async def get_by_name(
        self,
        generation_name: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameGetByNameResponse:
        """
        Get generation by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return await self._get(
            f"/ee/projects/{project_uuid}/generations/name/{generation_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameGetByNameResponse,
        )

    async def get_by_version(
        self,
        version_num: int,
        *,
        project_uuid: str,
        generation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Get generation by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return await self._get(
            f"/ee/projects/{project_uuid}/generations/name/{generation_name}/version/{version_num}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    async def get_deployed_by_name(
        self,
        generation_name: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Get the deployed generation by generation name and environment name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return await self._get(
            f"/ee/projects/{project_uuid}/generations/name/{generation_name}/environments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )


class NameResourceWithRawResponse:
    def __init__(self, name: NameResource) -> None:
        self._name = name

        self.get_by_name = to_raw_response_wrapper(
            name.get_by_name,
        )
        self.get_by_version = to_raw_response_wrapper(
            name.get_by_version,
        )
        self.get_deployed_by_name = to_raw_response_wrapper(
            name.get_deployed_by_name,
        )


class AsyncNameResourceWithRawResponse:
    def __init__(self, name: AsyncNameResource) -> None:
        self._name = name

        self.get_by_name = async_to_raw_response_wrapper(
            name.get_by_name,
        )
        self.get_by_version = async_to_raw_response_wrapper(
            name.get_by_version,
        )
        self.get_deployed_by_name = async_to_raw_response_wrapper(
            name.get_deployed_by_name,
        )


class NameResourceWithStreamingResponse:
    def __init__(self, name: NameResource) -> None:
        self._name = name

        self.get_by_name = to_streamed_response_wrapper(
            name.get_by_name,
        )
        self.get_by_version = to_streamed_response_wrapper(
            name.get_by_version,
        )
        self.get_deployed_by_name = to_streamed_response_wrapper(
            name.get_deployed_by_name,
        )


class AsyncNameResourceWithStreamingResponse:
    def __init__(self, name: AsyncNameResource) -> None:
        self._name = name

        self.get_by_name = async_to_streamed_response_wrapper(
            name.get_by_name,
        )
        self.get_by_version = async_to_streamed_response_wrapper(
            name.get_by_version,
        )
        self.get_deployed_by_name = async_to_streamed_response_wrapper(
            name.get_deployed_by_name,
        )
