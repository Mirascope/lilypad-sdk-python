# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ..._base_client import make_request_options
from ...types.projects import Scope, TimeFrame, span_search_traces_params, span_retrieve_aggregates_params
from ...types.projects.scope import Scope
from ...types.span_more_details import SpanMoreDetails
from ...types.projects.time_frame import TimeFrame
from ...types.projects.span_delete_response import SpanDeleteResponse
from ...types.projects.span_search_traces_response import SpanSearchTracesResponse
from ...types.projects.span_retrieve_aggregates_response import SpanRetrieveAggregatesResponse

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

    def delete(
        self,
        span_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanDeleteResponse:
        """
        Delete spans by UUID.

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
        return self._delete(
            f"/projects/{project_uuid}/spans/{span_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanDeleteResponse,
        )

    def retrieve_aggregates(
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
    ) -> SpanRetrieveAggregatesResponse:
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
                query=maybe_transform(
                    {"time_frame": time_frame}, span_retrieve_aggregates_params.SpanRetrieveAggregatesParams
                ),
            ),
            cast_to=SpanRetrieveAggregatesResponse,
        )

    def retrieve_by_id(
        self,
        span_id: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanMoreDetails:
        """
        Get span by project_uuid and span_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return self._get(
            f"/projects/{project_uuid}/spans/{span_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanMoreDetails,
        )

    def search_traces(
        self,
        project_uuid: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        query_string: Optional[str] | NotGiven = NOT_GIVEN,
        scope: Optional[Scope] | NotGiven = NOT_GIVEN,
        time_range_end: Optional[int] | NotGiven = NOT_GIVEN,
        time_range_start: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanSearchTracesResponse:
        """
        Search for traces in OpenSearch.

        Args:
          scope: Instrumentation Scope name of the span

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/spans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query_string": query_string,
                        "scope": scope,
                        "time_range_end": time_range_end,
                        "time_range_start": time_range_start,
                        "type": type,
                    },
                    span_search_traces_params.SpanSearchTracesParams,
                ),
            ),
            cast_to=SpanSearchTracesResponse,
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

    async def delete(
        self,
        span_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanDeleteResponse:
        """
        Delete spans by UUID.

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
        return await self._delete(
            f"/projects/{project_uuid}/spans/{span_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanDeleteResponse,
        )

    async def retrieve_aggregates(
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
    ) -> SpanRetrieveAggregatesResponse:
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
                    {"time_frame": time_frame}, span_retrieve_aggregates_params.SpanRetrieveAggregatesParams
                ),
            ),
            cast_to=SpanRetrieveAggregatesResponse,
        )

    async def retrieve_by_id(
        self,
        span_id: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanMoreDetails:
        """
        Get span by project_uuid and span_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return await self._get(
            f"/projects/{project_uuid}/spans/{span_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanMoreDetails,
        )

    async def search_traces(
        self,
        project_uuid: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        query_string: Optional[str] | NotGiven = NOT_GIVEN,
        scope: Optional[Scope] | NotGiven = NOT_GIVEN,
        time_range_end: Optional[int] | NotGiven = NOT_GIVEN,
        time_range_start: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanSearchTracesResponse:
        """
        Search for traces in OpenSearch.

        Args:
          scope: Instrumentation Scope name of the span

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/spans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query_string": query_string,
                        "scope": scope,
                        "time_range_end": time_range_end,
                        "time_range_start": time_range_start,
                        "type": type,
                    },
                    span_search_traces_params.SpanSearchTracesParams,
                ),
            ),
            cast_to=SpanSearchTracesResponse,
        )


class SpansResourceWithRawResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.delete = to_raw_response_wrapper(
            spans.delete,
        )
        self.retrieve_aggregates = to_raw_response_wrapper(
            spans.retrieve_aggregates,
        )
        self.retrieve_by_id = to_raw_response_wrapper(
            spans.retrieve_by_id,
        )
        self.search_traces = to_raw_response_wrapper(
            spans.search_traces,
        )


class AsyncSpansResourceWithRawResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.delete = async_to_raw_response_wrapper(
            spans.delete,
        )
        self.retrieve_aggregates = async_to_raw_response_wrapper(
            spans.retrieve_aggregates,
        )
        self.retrieve_by_id = async_to_raw_response_wrapper(
            spans.retrieve_by_id,
        )
        self.search_traces = async_to_raw_response_wrapper(
            spans.search_traces,
        )


class SpansResourceWithStreamingResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.delete = to_streamed_response_wrapper(
            spans.delete,
        )
        self.retrieve_aggregates = to_streamed_response_wrapper(
            spans.retrieve_aggregates,
        )
        self.retrieve_by_id = to_streamed_response_wrapper(
            spans.retrieve_by_id,
        )
        self.search_traces = to_streamed_response_wrapper(
            spans.search_traces,
        )


class AsyncSpansResourceWithStreamingResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.delete = async_to_streamed_response_wrapper(
            spans.delete,
        )
        self.retrieve_aggregates = async_to_streamed_response_wrapper(
            spans.retrieve_aggregates,
        )
        self.retrieve_by_id = async_to_streamed_response_wrapper(
            spans.retrieve_by_id,
        )
        self.search_traces = async_to_streamed_response_wrapper(
            spans.search_traces,
        )
