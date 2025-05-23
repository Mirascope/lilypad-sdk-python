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
from ..types.ee.user_public import UserPublic

__all__ = ["CurrentUserResource", "AsyncCurrentUserResource"]


class CurrentUserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrentUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CurrentUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrentUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return CurrentUserResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPublic:
        """Get user."""
        return self._get(
            "/current-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPublic,
        )


class AsyncCurrentUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrentUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrentUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrentUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncCurrentUserResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPublic:
        """Get user."""
        return await self._get(
            "/current-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPublic,
        )


class CurrentUserResourceWithRawResponse:
    def __init__(self, current_user: CurrentUserResource) -> None:
        self._current_user = current_user

        self.retrieve = to_raw_response_wrapper(
            current_user.retrieve,
        )


class AsyncCurrentUserResourceWithRawResponse:
    def __init__(self, current_user: AsyncCurrentUserResource) -> None:
        self._current_user = current_user

        self.retrieve = async_to_raw_response_wrapper(
            current_user.retrieve,
        )


class CurrentUserResourceWithStreamingResponse:
    def __init__(self, current_user: CurrentUserResource) -> None:
        self._current_user = current_user

        self.retrieve = to_streamed_response_wrapper(
            current_user.retrieve,
        )


class AsyncCurrentUserResourceWithStreamingResponse:
    def __init__(self, current_user: AsyncCurrentUserResource) -> None:
        self._current_user = current_user

        self.retrieve = async_to_streamed_response_wrapper(
            current_user.retrieve,
        )
