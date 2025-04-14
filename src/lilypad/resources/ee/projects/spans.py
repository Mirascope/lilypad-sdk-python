# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.ee.projects import span_assign_annotation_params
from ....types.ee.projects.span_assign_annotation_response import SpanAssignAnnotationResponse

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

    def assign_annotation(
        self,
        span_uuid: str,
        *,
        project_uuid: str,
        assignee_email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanAssignAnnotationResponse:
        """
        Assigns the annotation associated with the given span to a user specified by
        email. If no annotation exists, it will be created.

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
            f"/ee/projects/{project_uuid}/spans/{span_uuid}/assignment",
            body=maybe_transform(
                {"assignee_email": assignee_email}, span_assign_annotation_params.SpanAssignAnnotationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanAssignAnnotationResponse,
        )

    def generate_annotation(
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
    ) -> object:
        """
        Stream function.

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
        return self._get(
            f"/ee/projects/{project_uuid}/spans/{span_uuid}/generate-annotation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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

    async def assign_annotation(
        self,
        span_uuid: str,
        *,
        project_uuid: str,
        assignee_email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanAssignAnnotationResponse:
        """
        Assigns the annotation associated with the given span to a user specified by
        email. If no annotation exists, it will be created.

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
            f"/ee/projects/{project_uuid}/spans/{span_uuid}/assignment",
            body=await async_maybe_transform(
                {"assignee_email": assignee_email}, span_assign_annotation_params.SpanAssignAnnotationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanAssignAnnotationResponse,
        )

    async def generate_annotation(
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
    ) -> object:
        """
        Stream function.

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
        return await self._get(
            f"/ee/projects/{project_uuid}/spans/{span_uuid}/generate-annotation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SpansResourceWithRawResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.assign_annotation = to_raw_response_wrapper(
            spans.assign_annotation,
        )
        self.generate_annotation = to_raw_response_wrapper(
            spans.generate_annotation,
        )


class AsyncSpansResourceWithRawResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.assign_annotation = async_to_raw_response_wrapper(
            spans.assign_annotation,
        )
        self.generate_annotation = async_to_raw_response_wrapper(
            spans.generate_annotation,
        )


class SpansResourceWithStreamingResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.assign_annotation = to_streamed_response_wrapper(
            spans.assign_annotation,
        )
        self.generate_annotation = to_streamed_response_wrapper(
            spans.generate_annotation,
        )


class AsyncSpansResourceWithStreamingResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.assign_annotation = async_to_streamed_response_wrapper(
            spans.assign_annotation,
        )
        self.generate_annotation = async_to_streamed_response_wrapper(
            spans.generate_annotation,
        )
