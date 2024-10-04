# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.llm_functions import provider_call_param_create_params
from ...types.llm_functions.call_args_public import CallArgsPublic
from ...types.llm_functions.provider_call_params_table import ProviderCallParamsTable

__all__ = ["ProviderCallParamsResource", "AsyncProviderCallParamsResource"]


class ProviderCallParamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProviderCallParamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProviderCallParamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderCallParamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return ProviderCallParamsResourceWithStreamingResponse(self)

    def create(
        self,
        llm_function_id: int,
        *,
        call_params: Optional[object],
        model: str,
        prompt_template: str,
        provider: Literal["openai", "anthropic"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderCallParamsTable:
        """
        Creates a provider call params.

        Args:
          provider: Provider name enum

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/llm-functions/{llm_function_id}/provider-call-params",
            body=maybe_transform(
                {
                    "call_params": call_params,
                    "model": model,
                    "prompt_template": prompt_template,
                    "provider": provider,
                },
                provider_call_param_create_params.ProviderCallParamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderCallParamsTable,
        )

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
    ) -> CallArgsPublic:
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
            f"/llm-functions/{version_hash}/provider-call-params",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallArgsPublic,
        )


class AsyncProviderCallParamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProviderCallParamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderCallParamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderCallParamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return AsyncProviderCallParamsResourceWithStreamingResponse(self)

    async def create(
        self,
        llm_function_id: int,
        *,
        call_params: Optional[object],
        model: str,
        prompt_template: str,
        provider: Literal["openai", "anthropic"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderCallParamsTable:
        """
        Creates a provider call params.

        Args:
          provider: Provider name enum

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/llm-functions/{llm_function_id}/provider-call-params",
            body=await async_maybe_transform(
                {
                    "call_params": call_params,
                    "model": model,
                    "prompt_template": prompt_template,
                    "provider": provider,
                },
                provider_call_param_create_params.ProviderCallParamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderCallParamsTable,
        )

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
    ) -> CallArgsPublic:
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
            f"/llm-functions/{version_hash}/provider-call-params",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallArgsPublic,
        )


class ProviderCallParamsResourceWithRawResponse:
    def __init__(self, provider_call_params: ProviderCallParamsResource) -> None:
        self._provider_call_params = provider_call_params

        self.create = to_raw_response_wrapper(
            provider_call_params.create,
        )
        self.retrieve = to_raw_response_wrapper(
            provider_call_params.retrieve,
        )


class AsyncProviderCallParamsResourceWithRawResponse:
    def __init__(self, provider_call_params: AsyncProviderCallParamsResource) -> None:
        self._provider_call_params = provider_call_params

        self.create = async_to_raw_response_wrapper(
            provider_call_params.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            provider_call_params.retrieve,
        )


class ProviderCallParamsResourceWithStreamingResponse:
    def __init__(self, provider_call_params: ProviderCallParamsResource) -> None:
        self._provider_call_params = provider_call_params

        self.create = to_streamed_response_wrapper(
            provider_call_params.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            provider_call_params.retrieve,
        )


class AsyncProviderCallParamsResourceWithStreamingResponse:
    def __init__(self, provider_call_params: AsyncProviderCallParamsResource) -> None:
        self._provider_call_params = provider_call_params

        self.create = async_to_streamed_response_wrapper(
            provider_call_params.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            provider_call_params.retrieve,
        )
