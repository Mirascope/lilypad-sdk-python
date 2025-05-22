# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import span_update_params, span_list_paginated_params, span_retrieve_aggregates_params
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
from ..types.projects import TimeFrame
from ..types.span_more_details import SpanMoreDetails
from ..types.projects.time_frame import TimeFrame
from ..types.projects.span_public import SpanPublic
from ..types.paginated_span_public import PaginatedSpanPublic
from ..types.span_retrieve_aggregates_response import SpanRetrieveAggregatesResponse

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
        span_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanMoreDetails:
        """
        Get span by uuid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_uuid:
            raise ValueError(f"Expected a non-empty value for `span_uuid` but received {span_uuid!r}")
        return self._get(
            f"/spans/{span_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanMoreDetails,
        )

    def update(
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
                span_update_params.SpanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanPublic,
        )

    def list_paginated(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedSpanPublic:
        """
        Get spans for a function with pagination (new, non-breaking).

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
            f"/projects/{project_uuid}/functions/{function_uuid}/spans/paginated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                    },
                    span_list_paginated_params.SpanListPaginatedParams,
                ),
            ),
            cast_to=PaginatedSpanPublic,
        )

    def retrieve_aggregates(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        time_frame: TimeFrame,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanRetrieveAggregatesResponse:
        """
        Get aggregated span by function uuid.

        Args:
          time_frame: Timeframe for aggregation

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
            f"/projects/{project_uuid}/functions/{function_uuid}/spans/metadata",
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
        span_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanMoreDetails:
        """
        Get span by uuid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_uuid:
            raise ValueError(f"Expected a non-empty value for `span_uuid` but received {span_uuid!r}")
        return await self._get(
            f"/spans/{span_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanMoreDetails,
        )

    async def update(
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
                span_update_params.SpanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanPublic,
        )

    async def list_paginated(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedSpanPublic:
        """
        Get spans for a function with pagination (new, non-breaking).

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
            f"/projects/{project_uuid}/functions/{function_uuid}/spans/paginated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                    },
                    span_list_paginated_params.SpanListPaginatedParams,
                ),
            ),
            cast_to=PaginatedSpanPublic,
        )

    async def retrieve_aggregates(
        self,
        function_uuid: str,
        *,
        project_uuid: str,
        time_frame: TimeFrame,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanRetrieveAggregatesResponse:
        """
        Get aggregated span by function uuid.

        Args:
          time_frame: Timeframe for aggregation

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
            f"/projects/{project_uuid}/functions/{function_uuid}/spans/metadata",
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


class SpansResourceWithRawResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.retrieve = to_raw_response_wrapper(
            spans.retrieve,
        )
        self.update = to_raw_response_wrapper(
            spans.update,
        )
        self.list_paginated = to_raw_response_wrapper(
            spans.list_paginated,
        )
        self.retrieve_aggregates = to_raw_response_wrapper(
            spans.retrieve_aggregates,
        )


class AsyncSpansResourceWithRawResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.retrieve = async_to_raw_response_wrapper(
            spans.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            spans.update,
        )
        self.list_paginated = async_to_raw_response_wrapper(
            spans.list_paginated,
        )
        self.retrieve_aggregates = async_to_raw_response_wrapper(
            spans.retrieve_aggregates,
        )


class SpansResourceWithStreamingResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.retrieve = to_streamed_response_wrapper(
            spans.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            spans.update,
        )
        self.list_paginated = to_streamed_response_wrapper(
            spans.list_paginated,
        )
        self.retrieve_aggregates = to_streamed_response_wrapper(
            spans.retrieve_aggregates,
        )


class AsyncSpansResourceWithStreamingResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.retrieve = async_to_streamed_response_wrapper(
            spans.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            spans.update,
        )
        self.list_paginated = async_to_streamed_response_wrapper(
            spans.list_paginated,
        )
        self.retrieve_aggregates = async_to_streamed_response_wrapper(
            spans.retrieve_aggregates,
        )
