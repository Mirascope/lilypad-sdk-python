# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import external_api_key_create_params
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
from ..types.external_api_key_public import ExternalAPIKeyPublic
from ..types.external_api_key_list_response import ExternalAPIKeyListResponse
from ..types.external_api_key_delete_response import ExternalAPIKeyDeleteResponse

__all__ = ["ExternalAPIKeysResource", "AsyncExternalAPIKeysResource"]


class ExternalAPIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExternalAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return ExternalAPIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_key: str,
        service_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyPublic:
        """
        Store an external API key for a given service.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external-api-keys",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "service_name": service_name,
                },
                external_api_key_create_params.ExternalAPIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyPublic,
        )

    def retrieve(
        self,
        service_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyPublic:
        """
        Retrieve an external API key for a given service.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        return self._get(
            f"/external-api-keys/{service_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyPublic,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyListResponse:
        """List all external API keys for the user with masked values."""
        return self._get(
            "/external-api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyListResponse,
        )

    def delete(
        self,
        service_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyDeleteResponse:
        """
        Delete an external API key for a given service.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        return self._delete(
            f"/external-api-keys/{service_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyDeleteResponse,
        )


class AsyncExternalAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncExternalAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_key: str,
        service_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyPublic:
        """
        Store an external API key for a given service.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external-api-keys",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "service_name": service_name,
                },
                external_api_key_create_params.ExternalAPIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyPublic,
        )

    async def retrieve(
        self,
        service_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyPublic:
        """
        Retrieve an external API key for a given service.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        return await self._get(
            f"/external-api-keys/{service_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyPublic,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyListResponse:
        """List all external API keys for the user with masked values."""
        return await self._get(
            "/external-api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyListResponse,
        )

    async def delete(
        self,
        service_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAPIKeyDeleteResponse:
        """
        Delete an external API key for a given service.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        return await self._delete(
            f"/external-api-keys/{service_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAPIKeyDeleteResponse,
        )


class ExternalAPIKeysResourceWithRawResponse:
    def __init__(self, external_api_keys: ExternalAPIKeysResource) -> None:
        self._external_api_keys = external_api_keys

        self.create = to_raw_response_wrapper(
            external_api_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            external_api_keys.retrieve,
        )
        self.list = to_raw_response_wrapper(
            external_api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            external_api_keys.delete,
        )


class AsyncExternalAPIKeysResourceWithRawResponse:
    def __init__(self, external_api_keys: AsyncExternalAPIKeysResource) -> None:
        self._external_api_keys = external_api_keys

        self.create = async_to_raw_response_wrapper(
            external_api_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            external_api_keys.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            external_api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            external_api_keys.delete,
        )


class ExternalAPIKeysResourceWithStreamingResponse:
    def __init__(self, external_api_keys: ExternalAPIKeysResource) -> None:
        self._external_api_keys = external_api_keys

        self.create = to_streamed_response_wrapper(
            external_api_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_api_keys.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            external_api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            external_api_keys.delete,
        )


class AsyncExternalAPIKeysResourceWithStreamingResponse:
    def __init__(self, external_api_keys: AsyncExternalAPIKeysResource) -> None:
        self._external_api_keys = external_api_keys

        self.create = async_to_streamed_response_wrapper(
            external_api_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_api_keys.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            external_api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            external_api_keys.delete,
        )
