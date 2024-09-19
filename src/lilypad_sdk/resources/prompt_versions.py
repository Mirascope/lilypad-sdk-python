# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.prompt_version_public import PromptVersionPublic

__all__ = ["PromptVersionsResource", "AsyncPromptVersionsResource"]


class PromptVersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PromptVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return PromptVersionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        version_hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptVersionPublic:
        """
        Get prompt version id by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_hash:
            raise ValueError(f"Expected a non-empty value for `version_hash` but received {version_hash!r}")
        return self._get(
            f"/prompt-versions/{version_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptVersionPublic,
        )


class AsyncPromptVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return AsyncPromptVersionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        version_hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptVersionPublic:
        """
        Get prompt version id by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_hash:
            raise ValueError(f"Expected a non-empty value for `version_hash` but received {version_hash!r}")
        return await self._get(
            f"/prompt-versions/{version_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptVersionPublic,
        )


class PromptVersionsResourceWithRawResponse:
    def __init__(self, prompt_versions: PromptVersionsResource) -> None:
        self._prompt_versions = prompt_versions

        self.retrieve = to_raw_response_wrapper(
            prompt_versions.retrieve,
        )


class AsyncPromptVersionsResourceWithRawResponse:
    def __init__(self, prompt_versions: AsyncPromptVersionsResource) -> None:
        self._prompt_versions = prompt_versions

        self.retrieve = async_to_raw_response_wrapper(
            prompt_versions.retrieve,
        )


class PromptVersionsResourceWithStreamingResponse:
    def __init__(self, prompt_versions: PromptVersionsResource) -> None:
        self._prompt_versions = prompt_versions

        self.retrieve = to_streamed_response_wrapper(
            prompt_versions.retrieve,
        )


class AsyncPromptVersionsResourceWithStreamingResponse:
    def __init__(self, prompt_versions: AsyncPromptVersionsResource) -> None:
        self._prompt_versions = prompt_versions

        self.retrieve = async_to_streamed_response_wrapper(
            prompt_versions.retrieve,
        )
