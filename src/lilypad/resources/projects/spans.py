# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ...types.projects import span_list_aggregates_params
from ...types.projects.functions import TimeFrame
from ...types.projects.functions.time_frame import TimeFrame
from ...types.projects.functions.span_public import SpanPublic
from ...types.projects.span_list_aggregates_response import SpanListAggregatesResponse

__all__ = ["SpansResource", "AsyncSpansResource"]


class SpansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SpansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return SpansResourceWithStreamingResponse(self)

    def list_aggregates(
        self,
        project_uuid: str,
        *,
        time_frame: TimeFrame,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanListAggregatesResponse:
        """
        Get aggregated span by project uuid.

        Args:
          time_frame: Timeframe for aggregation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/spans/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"time_frame": time_frame}, span_list_aggregates_params.SpanListAggregatesParams),
            ),
            cast_to=SpanListAggregatesResponse,
        )

    def update_tags(
        self,
        span_uuid: str,
        *,
        project_uuid: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanPublic:
        """
        Update span tags by uuid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not span_uuid:
            raise ValueError(f"Expected a non-empty value for `span_uuid` but received {span_uuid!r}")
        return self._patch(
            f"/projects/{project_uuid}/spans/{span_uuid}",
            body=maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanPublic,
        )


class AsyncSpansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncSpansResourceWithStreamingResponse(self)

    async def list_aggregates(
        self,
        project_uuid: str,
        *,
        time_frame: TimeFrame,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanListAggregatesResponse:
        """
        Get aggregated span by project uuid.

        Args:
          time_frame: Timeframe for aggregation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/spans/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"time_frame": time_frame}, span_list_aggregates_params.SpanListAggregatesParams
                ),
            ),
            cast_to=SpanListAggregatesResponse,
        )

    async def update_tags(
        self,
        span_uuid: str,
        *,
        project_uuid: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanPublic:
        """
        Update span tags by uuid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not span_uuid:
            raise ValueError(f"Expected a non-empty value for `span_uuid` but received {span_uuid!r}")
        return await self._patch(
            f"/projects/{project_uuid}/spans/{span_uuid}",
            body=await async_maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanPublic,
        )


class SpansResourceWithRawResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.list_aggregates = to_raw_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = to_raw_response_wrapper(
            spans.update_tags,
        )


class AsyncSpansResourceWithRawResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.list_aggregates = async_to_raw_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = async_to_raw_response_wrapper(
            spans.update_tags,
        )


class SpansResourceWithStreamingResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.list_aggregates = to_streamed_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = to_streamed_response_wrapper(
            spans.update_tags,
        )


class AsyncSpansResourceWithStreamingResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.list_aggregates = async_to_streamed_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = async_to_streamed_response_wrapper(
            spans.update_tags,
        )
