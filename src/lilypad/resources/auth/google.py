# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import google_callback_params
from ..._base_client import make_request_options
from ...types.ee.user_public import UserPublic

__all__ = ["GoogleResource", "AsyncGoogleResource"]


class GoogleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoogleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GoogleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoogleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return GoogleResourceWithStreamingResponse(self)

    def callback(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPublic:
        """
        Callback for Google OAuth.

        Saves the user and organization or retrieves the user after authenticating with
        Google.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/auth/google/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"code": code}, google_callback_params.GoogleCallbackParams),
            ),
            cast_to=UserPublic,
        )


class AsyncGoogleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoogleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGoogleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoogleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncGoogleResourceWithStreamingResponse(self)

    async def callback(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPublic:
        """
        Callback for Google OAuth.

        Saves the user and organization or retrieves the user after authenticating with
        Google.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/auth/google/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"code": code}, google_callback_params.GoogleCallbackParams),
            ),
            cast_to=UserPublic,
        )


class GoogleResourceWithRawResponse:
    def __init__(self, google: GoogleResource) -> None:
        self._google = google

        self.callback = to_raw_response_wrapper(
            google.callback,
        )


class AsyncGoogleResourceWithRawResponse:
    def __init__(self, google: AsyncGoogleResource) -> None:
        self._google = google

        self.callback = async_to_raw_response_wrapper(
            google.callback,
        )


class GoogleResourceWithStreamingResponse:
    def __init__(self, google: GoogleResource) -> None:
        self._google = google

        self.callback = to_streamed_response_wrapper(
            google.callback,
        )


class AsyncGoogleResourceWithStreamingResponse:
    def __init__(self, google: AsyncGoogleResource) -> None:
        self._google = google

        self.callback = async_to_streamed_response_wrapper(
            google.callback,
        )
