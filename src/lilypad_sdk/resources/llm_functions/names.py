# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.llm_functions.name_list_response import NameListResponse

__all__ = ["NamesResource", "AsyncNamesResource"]


class NamesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return NamesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameListResponse:
        """Get llm function names by hash."""
        return self._get(
            "/llm-functions/names",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameListResponse,
        )


class AsyncNamesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return AsyncNamesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameListResponse:
        """Get llm function names by hash."""
        return await self._get(
            "/llm-functions/names",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameListResponse,
        )


class NamesResourceWithRawResponse:
    def __init__(self, names: NamesResource) -> None:
        self._names = names

        self.list = to_raw_response_wrapper(
            names.list,
        )


class AsyncNamesResourceWithRawResponse:
    def __init__(self, names: AsyncNamesResource) -> None:
        self._names = names

        self.list = async_to_raw_response_wrapper(
            names.list,
        )


class NamesResourceWithStreamingResponse:
    def __init__(self, names: NamesResource) -> None:
        self._names = names

        self.list = to_streamed_response_wrapper(
            names.list,
        )


class AsyncNamesResourceWithStreamingResponse:
    def __init__(self, names: AsyncNamesResource) -> None:
        self._names = names

        self.list = async_to_streamed_response_wrapper(
            names.list,
        )
