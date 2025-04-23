# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import user_consent_create_params, user_consent_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_consent_create_response import UserConsentCreateResponse
from ..types.user_consent_update_response import UserConsentUpdateResponse

__all__ = ["UserConsentsResource", "AsyncUserConsentsResource"]


class UserConsentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserConsentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UserConsentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserConsentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return UserConsentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        privacy_policy_version: str,
        tos_version: str,
        privacy_policy_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tos_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserConsentCreateResponse:
        """
        Store user consent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user-consents",
            body=maybe_transform(
                {
                    "privacy_policy_version": privacy_policy_version,
                    "tos_version": tos_version,
                    "privacy_policy_accepted_at": privacy_policy_accepted_at,
                    "tos_accepted_at": tos_accepted_at,
                    "user_uuid": user_uuid,
                },
                user_consent_create_params.UserConsentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserConsentCreateResponse,
        )

    def update(
        self,
        user_consent_uuid: str,
        *,
        privacy_policy_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        privacy_policy_version: Optional[str] | NotGiven = NOT_GIVEN,
        tos_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tos_version: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserConsentUpdateResponse:
        """
        Update user consent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_consent_uuid:
            raise ValueError(f"Expected a non-empty value for `user_consent_uuid` but received {user_consent_uuid!r}")
        return self._patch(
            f"/user-consents/{user_consent_uuid}",
            body=maybe_transform(
                {
                    "privacy_policy_accepted_at": privacy_policy_accepted_at,
                    "privacy_policy_version": privacy_policy_version,
                    "tos_accepted_at": tos_accepted_at,
                    "tos_version": tos_version,
                },
                user_consent_update_params.UserConsentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserConsentUpdateResponse,
        )


class AsyncUserConsentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserConsentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserConsentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserConsentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncUserConsentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        privacy_policy_version: str,
        tos_version: str,
        privacy_policy_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tos_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        user_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserConsentCreateResponse:
        """
        Store user consent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user-consents",
            body=await async_maybe_transform(
                {
                    "privacy_policy_version": privacy_policy_version,
                    "tos_version": tos_version,
                    "privacy_policy_accepted_at": privacy_policy_accepted_at,
                    "tos_accepted_at": tos_accepted_at,
                    "user_uuid": user_uuid,
                },
                user_consent_create_params.UserConsentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserConsentCreateResponse,
        )

    async def update(
        self,
        user_consent_uuid: str,
        *,
        privacy_policy_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        privacy_policy_version: Optional[str] | NotGiven = NOT_GIVEN,
        tos_accepted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tos_version: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserConsentUpdateResponse:
        """
        Update user consent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_consent_uuid:
            raise ValueError(f"Expected a non-empty value for `user_consent_uuid` but received {user_consent_uuid!r}")
        return await self._patch(
            f"/user-consents/{user_consent_uuid}",
            body=await async_maybe_transform(
                {
                    "privacy_policy_accepted_at": privacy_policy_accepted_at,
                    "privacy_policy_version": privacy_policy_version,
                    "tos_accepted_at": tos_accepted_at,
                    "tos_version": tos_version,
                },
                user_consent_update_params.UserConsentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserConsentUpdateResponse,
        )


class UserConsentsResourceWithRawResponse:
    def __init__(self, user_consents: UserConsentsResource) -> None:
        self._user_consents = user_consents

        self.create = to_raw_response_wrapper(
            user_consents.create,
        )
        self.update = to_raw_response_wrapper(
            user_consents.update,
        )


class AsyncUserConsentsResourceWithRawResponse:
    def __init__(self, user_consents: AsyncUserConsentsResource) -> None:
        self._user_consents = user_consents

        self.create = async_to_raw_response_wrapper(
            user_consents.create,
        )
        self.update = async_to_raw_response_wrapper(
            user_consents.update,
        )


class UserConsentsResourceWithStreamingResponse:
    def __init__(self, user_consents: UserConsentsResource) -> None:
        self._user_consents = user_consents

        self.create = to_streamed_response_wrapper(
            user_consents.create,
        )
        self.update = to_streamed_response_wrapper(
            user_consents.update,
        )


class AsyncUserConsentsResourceWithStreamingResponse:
    def __init__(self, user_consents: AsyncUserConsentsResource) -> None:
        self._user_consents = user_consents

        self.create = async_to_streamed_response_wrapper(
            user_consents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            user_consents.update,
        )
