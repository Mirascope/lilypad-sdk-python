# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

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
from ...types.projects import span_list_params, span_update_tags_params, span_list_aggregates_params
from ...types.span_more_details import SpanMoreDetails
from ...types.projects.functions import TimeFrame
from ...types.projects.span_list_response import SpanListResponse
from ...types.projects.functions.time_frame import TimeFrame
from ...types.projects.span_delete_response import SpanDeleteResponse
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

    def retrieve(
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

    def list(
        self,
        project_uuid: str,
        *,
        query_string: str,
        limit: int | NotGiven = NOT_GIVEN,
        scope: Optional[Literal["lilypad", "llm"]] | NotGiven = NOT_GIVEN,
        time_range_end: Optional[int] | NotGiven = NOT_GIVEN,
        time_range_start: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanListResponse:
        """
        Search for traces in OpenSearch.

        Args:
          query_string: Search query string

          limit: Maximum number of results to return

          scope: Instrumentation Scope name of the span

          time_range_end: End time range in milliseconds

          time_range_start: Start time range in milliseconds

          type: Type of spans to search for

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
                        "query_string": query_string,
                        "limit": limit,
                        "scope": scope,
                        "time_range_end": time_range_end,
                        "time_range_start": time_range_start,
                        "type": type,
                    },
                    span_list_params.SpanListParams,
                ),
            ),
            cast_to=SpanListResponse,
        )

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
        tags_by_name: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags_by_uuid: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanPublic:
        """
        Update span by uuid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_uuid:
            raise ValueError(f"Expected a non-empty value for `span_uuid` but received {span_uuid!r}")
        return self._patch(
            f"/spans/{span_uuid}",
            body=maybe_transform(
                {
                    "tags_by_name": tags_by_name,
                    "tags_by_uuid": tags_by_uuid,
                },
                span_update_tags_params.SpanUpdateTagsParams,
            ),
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

    async def retrieve(
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

    async def list(
        self,
        project_uuid: str,
        *,
        query_string: str,
        limit: int | NotGiven = NOT_GIVEN,
        scope: Optional[Literal["lilypad", "llm"]] | NotGiven = NOT_GIVEN,
        time_range_end: Optional[int] | NotGiven = NOT_GIVEN,
        time_range_start: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanListResponse:
        """
        Search for traces in OpenSearch.

        Args:
          query_string: Search query string

          limit: Maximum number of results to return

          scope: Instrumentation Scope name of the span

          time_range_end: End time range in milliseconds

          time_range_start: Start time range in milliseconds

          type: Type of spans to search for

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
                        "query_string": query_string,
                        "limit": limit,
                        "scope": scope,
                        "time_range_end": time_range_end,
                        "time_range_start": time_range_start,
                        "type": type,
                    },
                    span_list_params.SpanListParams,
                ),
            ),
            cast_to=SpanListResponse,
        )

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
        tags_by_name: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags_by_uuid: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanPublic:
        """
        Update span by uuid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_uuid:
            raise ValueError(f"Expected a non-empty value for `span_uuid` but received {span_uuid!r}")
        return await self._patch(
            f"/spans/{span_uuid}",
            body=await async_maybe_transform(
                {
                    "tags_by_name": tags_by_name,
                    "tags_by_uuid": tags_by_uuid,
                },
                span_update_tags_params.SpanUpdateTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanPublic,
        )


class SpansResourceWithRawResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.retrieve = to_raw_response_wrapper(
            spans.retrieve,
        )
        self.list = to_raw_response_wrapper(
            spans.list,
        )
        self.delete = to_raw_response_wrapper(
            spans.delete,
        )
        self.list_aggregates = to_raw_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = to_raw_response_wrapper(
            spans.update_tags,
        )


class AsyncSpansResourceWithRawResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.retrieve = async_to_raw_response_wrapper(
            spans.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            spans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            spans.delete,
        )
        self.list_aggregates = async_to_raw_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = async_to_raw_response_wrapper(
            spans.update_tags,
        )


class SpansResourceWithStreamingResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.retrieve = to_streamed_response_wrapper(
            spans.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            spans.list,
        )
        self.delete = to_streamed_response_wrapper(
            spans.delete,
        )
        self.list_aggregates = to_streamed_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = to_streamed_response_wrapper(
            spans.update_tags,
        )


class AsyncSpansResourceWithStreamingResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.retrieve = async_to_streamed_response_wrapper(
            spans.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            spans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            spans.delete,
        )
        self.list_aggregates = async_to_streamed_response_wrapper(
            spans.list_aggregates,
        )
        self.update_tags = async_to_streamed_response_wrapper(
            spans.update_tags,
        )
