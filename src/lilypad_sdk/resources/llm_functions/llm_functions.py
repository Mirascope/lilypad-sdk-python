# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .names import (
    NamesResource,
    AsyncNamesResource,
    NamesResourceWithRawResponse,
    AsyncNamesResourceWithRawResponse,
    NamesResourceWithStreamingResponse,
    AsyncNamesResourceWithStreamingResponse,
)
from ...types import llm_function_list_params, llm_function_create_params
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
from .provider_call_params import (
    ProviderCallParamsResource,
    AsyncProviderCallParamsResource,
    ProviderCallParamsResourceWithRawResponse,
    AsyncProviderCallParamsResourceWithRawResponse,
    ProviderCallParamsResourceWithStreamingResponse,
    AsyncProviderCallParamsResourceWithStreamingResponse,
)
from ...types.llm_function_base_public import LlmFunctionBasePublic
from ...types.llm_function_list_response import LlmFunctionListResponse

__all__ = ["LlmFunctionsResource", "AsyncLlmFunctionsResource"]


class LlmFunctionsResource(SyncAPIResource):
    @cached_property
    def names(self) -> NamesResource:
        return NamesResource(self._client)

    @cached_property
    def provider_call_params(self) -> ProviderCallParamsResource:
        return ProviderCallParamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LlmFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LlmFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return LlmFunctionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        function_name: str,
        version_hash: str,
        input_arguments: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmFunctionBasePublic:
        """
        Get prompt version id by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/llm-functions/",
            body=maybe_transform(
                {
                    "code": code,
                    "function_name": function_name,
                    "version_hash": version_hash,
                    "input_arguments": input_arguments,
                },
                llm_function_create_params.LlmFunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmFunctionBasePublic,
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
    ) -> LlmFunctionBasePublic:
        """
        Get llm function by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_hash:
            raise ValueError(f"Expected a non-empty value for `version_hash` but received {version_hash!r}")
        return self._get(
            f"/llm-functions/{version_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmFunctionBasePublic,
        )

    def list(
        self,
        *,
        function_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmFunctionListResponse:
        """
        Get prompt version id by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/llm-functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"function_name": function_name}, llm_function_list_params.LlmFunctionListParams),
            ),
            cast_to=LlmFunctionListResponse,
        )


class AsyncLlmFunctionsResource(AsyncAPIResource):
    @cached_property
    def names(self) -> AsyncNamesResource:
        return AsyncNamesResource(self._client)

    @cached_property
    def provider_call_params(self) -> AsyncProviderCallParamsResource:
        return AsyncProviderCallParamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLlmFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return AsyncLlmFunctionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        function_name: str,
        version_hash: str,
        input_arguments: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmFunctionBasePublic:
        """
        Get prompt version id by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/llm-functions/",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "function_name": function_name,
                    "version_hash": version_hash,
                    "input_arguments": input_arguments,
                },
                llm_function_create_params.LlmFunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmFunctionBasePublic,
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
    ) -> LlmFunctionBasePublic:
        """
        Get llm function by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_hash:
            raise ValueError(f"Expected a non-empty value for `version_hash` but received {version_hash!r}")
        return await self._get(
            f"/llm-functions/{version_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmFunctionBasePublic,
        )

    async def list(
        self,
        *,
        function_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmFunctionListResponse:
        """
        Get prompt version id by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/llm-functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"function_name": function_name}, llm_function_list_params.LlmFunctionListParams
                ),
            ),
            cast_to=LlmFunctionListResponse,
        )


class LlmFunctionsResourceWithRawResponse:
    def __init__(self, llm_functions: LlmFunctionsResource) -> None:
        self._llm_functions = llm_functions

        self.create = to_raw_response_wrapper(
            llm_functions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            llm_functions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            llm_functions.list,
        )

    @cached_property
    def names(self) -> NamesResourceWithRawResponse:
        return NamesResourceWithRawResponse(self._llm_functions.names)

    @cached_property
    def provider_call_params(self) -> ProviderCallParamsResourceWithRawResponse:
        return ProviderCallParamsResourceWithRawResponse(self._llm_functions.provider_call_params)


class AsyncLlmFunctionsResourceWithRawResponse:
    def __init__(self, llm_functions: AsyncLlmFunctionsResource) -> None:
        self._llm_functions = llm_functions

        self.create = async_to_raw_response_wrapper(
            llm_functions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            llm_functions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            llm_functions.list,
        )

    @cached_property
    def names(self) -> AsyncNamesResourceWithRawResponse:
        return AsyncNamesResourceWithRawResponse(self._llm_functions.names)

    @cached_property
    def provider_call_params(self) -> AsyncProviderCallParamsResourceWithRawResponse:
        return AsyncProviderCallParamsResourceWithRawResponse(self._llm_functions.provider_call_params)


class LlmFunctionsResourceWithStreamingResponse:
    def __init__(self, llm_functions: LlmFunctionsResource) -> None:
        self._llm_functions = llm_functions

        self.create = to_streamed_response_wrapper(
            llm_functions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            llm_functions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            llm_functions.list,
        )

    @cached_property
    def names(self) -> NamesResourceWithStreamingResponse:
        return NamesResourceWithStreamingResponse(self._llm_functions.names)

    @cached_property
    def provider_call_params(self) -> ProviderCallParamsResourceWithStreamingResponse:
        return ProviderCallParamsResourceWithStreamingResponse(self._llm_functions.provider_call_params)


class AsyncLlmFunctionsResourceWithStreamingResponse:
    def __init__(self, llm_functions: AsyncLlmFunctionsResource) -> None:
        self._llm_functions = llm_functions

        self.create = async_to_streamed_response_wrapper(
            llm_functions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            llm_functions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            llm_functions.list,
        )

    @cached_property
    def names(self) -> AsyncNamesResourceWithStreamingResponse:
        return AsyncNamesResourceWithStreamingResponse(self._llm_functions.names)

    @cached_property
    def provider_call_params(self) -> AsyncProviderCallParamsResourceWithStreamingResponse:
        return AsyncProviderCallParamsResourceWithStreamingResponse(self._llm_functions.provider_call_params)
