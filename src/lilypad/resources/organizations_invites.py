# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import organizations_invite_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.organization_invite import OrganizationInvite

__all__ = ["OrganizationsInvitesResource", "AsyncOrganizationsInvitesResource"]


class OrganizationsInvitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsInvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return OrganizationsInvitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        invited_by: str,
        token: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        organization_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        resend_email_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationInvite:
        """
        Create an organization invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organizations-invites",
            body=maybe_transform(
                {
                    "email": email,
                    "invited_by": invited_by,
                    "token": token,
                    "expires_at": expires_at,
                    "organization_uuid": organization_uuid,
                    "resend_email_id": resend_email_id,
                },
                organizations_invite_create_params.OrganizationsInviteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationInvite,
        )

    def retrieve(
        self,
        invite_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationInvite:
        """
        Get an organization invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_token:
            raise ValueError(f"Expected a non-empty value for `invite_token` but received {invite_token!r}")
        return self._get(
            f"/organizations-invites/{invite_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationInvite,
        )


class AsyncOrganizationsInvitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsInvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncOrganizationsInvitesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        invited_by: str,
        token: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        organization_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        resend_email_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationInvite:
        """
        Create an organization invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organizations-invites",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "invited_by": invited_by,
                    "token": token,
                    "expires_at": expires_at,
                    "organization_uuid": organization_uuid,
                    "resend_email_id": resend_email_id,
                },
                organizations_invite_create_params.OrganizationsInviteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationInvite,
        )

    async def retrieve(
        self,
        invite_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationInvite:
        """
        Get an organization invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_token:
            raise ValueError(f"Expected a non-empty value for `invite_token` but received {invite_token!r}")
        return await self._get(
            f"/organizations-invites/{invite_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationInvite,
        )


class OrganizationsInvitesResourceWithRawResponse:
    def __init__(self, organizations_invites: OrganizationsInvitesResource) -> None:
        self._organizations_invites = organizations_invites

        self.create = to_raw_response_wrapper(
            organizations_invites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            organizations_invites.retrieve,
        )


class AsyncOrganizationsInvitesResourceWithRawResponse:
    def __init__(self, organizations_invites: AsyncOrganizationsInvitesResource) -> None:
        self._organizations_invites = organizations_invites

        self.create = async_to_raw_response_wrapper(
            organizations_invites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            organizations_invites.retrieve,
        )


class OrganizationsInvitesResourceWithStreamingResponse:
    def __init__(self, organizations_invites: OrganizationsInvitesResource) -> None:
        self._organizations_invites = organizations_invites

        self.create = to_streamed_response_wrapper(
            organizations_invites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            organizations_invites.retrieve,
        )


class AsyncOrganizationsInvitesResourceWithStreamingResponse:
    def __init__(self, organizations_invites: AsyncOrganizationsInvitesResource) -> None:
        self._organizations_invites = organizations_invites

        self.create = async_to_streamed_response_wrapper(
            organizations_invites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            organizations_invites.retrieve,
        )
