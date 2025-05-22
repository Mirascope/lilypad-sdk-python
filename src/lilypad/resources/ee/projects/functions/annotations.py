# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ee.projects.functions.annotation_list_response import AnnotationListResponse
from .....types.ee.projects.functions.annotation_get_metrics_response import AnnotationGetMetricsResponse

__all__ = ["AnnotationsResource", "AsyncAnnotationsResource"]


class AnnotationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AnnotationsResourceWithStreamingResponse(self)

    def list(
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
    ) -> AnnotationListResponse:
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
            cast_to=AnnotationListResponse,
        )

    def get_metrics(
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
    ) -> AnnotationGetMetricsResponse:
        """
        Get annotation metrics by function.

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
            f"/ee/projects/{project_uuid}/functions/{function_uuid}/annotations/metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationGetMetricsResponse,
        )


class AsyncAnnotationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncAnnotationsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> AnnotationListResponse:
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
            cast_to=AnnotationListResponse,
        )

    async def get_metrics(
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
    ) -> AnnotationGetMetricsResponse:
        """
        Get annotation metrics by function.

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
            f"/ee/projects/{project_uuid}/functions/{function_uuid}/annotations/metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationGetMetricsResponse,
        )


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.list = to_raw_response_wrapper(
            annotations.list,
        )
        self.get_metrics = to_raw_response_wrapper(
            annotations.get_metrics,
        )


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.list = async_to_raw_response_wrapper(
            annotations.list,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            annotations.get_metrics,
        )


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.list = to_streamed_response_wrapper(
            annotations.list,
        )
        self.get_metrics = to_streamed_response_wrapper(
            annotations.get_metrics,
        )


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.list = async_to_streamed_response_wrapper(
            annotations.list,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            annotations.get_metrics,
        )
