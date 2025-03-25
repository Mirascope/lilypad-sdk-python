# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ee.projects import function_run_playground_params
from ....types.function_create_param import FunctionCreateParam
from ....types.ee.projects.function_get_annotations_response import FunctionGetAnnotationsResponse

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def get_annotations(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionGetAnnotationsResponse:
        """
        Get annotations by functions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not function_uuid:
            raise ValueError(f"Expected a non-empty value for `function_uuid` but received {function_uuid!r}")
        return self._get(
            f"/ee/projects/{project_uuid}/functions/{function_uuid}/annotations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionGetAnnotationsResponse,
        )

    def run_playground(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        arg_values: Dict[str, Union[float, bool, str, Iterable[object], object]],
        model: str,
        provider: Literal["openai", "anthropic", "openrouter", "gemini"],
        function: Optional[FunctionCreateParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Run playground version.

        Args:
          provider: Provider name enum

          function: Function create model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not function_uuid:
            raise ValueError(f"Expected a non-empty value for `function_uuid` but received {function_uuid!r}")
        return self._post(
            f"/ee/projects/{project_uuid}/functions/{function_uuid}/playground",
            body=maybe_transform(
                {
                    "arg_values": arg_values,
                    "model": model,
                    "provider": provider,
                    "function": function,
                },
                function_run_playground_params.FunctionRunPlaygroundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def get_annotations(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionGetAnnotationsResponse:
        """
        Get annotations by functions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not function_uuid:
            raise ValueError(f"Expected a non-empty value for `function_uuid` but received {function_uuid!r}")
        return await self._get(
            f"/ee/projects/{project_uuid}/functions/{function_uuid}/annotations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionGetAnnotationsResponse,
        )

    async def run_playground(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        arg_values: Dict[str, Union[float, bool, str, Iterable[object], object]],
        model: str,
        provider: Literal["openai", "anthropic", "openrouter", "gemini"],
        function: Optional[FunctionCreateParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Run playground version.

        Args:
          provider: Provider name enum

          function: Function create model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not function_uuid:
            raise ValueError(f"Expected a non-empty value for `function_uuid` but received {function_uuid!r}")
        return await self._post(
            f"/ee/projects/{project_uuid}/functions/{function_uuid}/playground",
            body=await async_maybe_transform(
                {
                    "arg_values": arg_values,
                    "model": model,
                    "provider": provider,
                    "function": function,
                },
                function_run_playground_params.FunctionRunPlaygroundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.get_annotations = to_raw_response_wrapper(
            functions.get_annotations,
        )
        self.run_playground = to_raw_response_wrapper(
            functions.run_playground,
        )


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.get_annotations = async_to_raw_response_wrapper(
            functions.get_annotations,
        )
        self.run_playground = async_to_raw_response_wrapper(
            functions.run_playground,
        )


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.get_annotations = to_streamed_response_wrapper(
            functions.get_annotations,
        )
        self.run_playground = to_streamed_response_wrapper(
            functions.run_playground,
        )


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.get_annotations = async_to_streamed_response_wrapper(
            functions.get_annotations,
        )
        self.run_playground = async_to_streamed_response_wrapper(
            functions.run_playground,
        )
