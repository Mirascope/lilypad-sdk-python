# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ....types.ee.projects import Label, EvaluationType, annotation_create_params, annotation_update_params
from ....types.ee.projects.label import Label
from ....types.ee.projects.evaluation_type import EvaluationType
from ....types.ee.projects.annotation_public import AnnotationPublic
from ....types.ee.projects.annotation_create_response import AnnotationCreateResponse

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

    def create(
        self,
        project_uuid: str,
        *,
        body: Iterable[annotation_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationCreateResponse:
        """Create an annotation.

        Args: project_uuid: The project UUID.

        annotations_service: The annotation
        service. annotations_create: The annotation create model.

        Returns: AnnotationPublic: The created annotation.

        Raises: HTTPException: If the span has already been assigned to a user and has
        not been labeled yet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return self._post(
            f"/ee/projects/{project_uuid}/annotations",
            body=maybe_transform(body, Iterable[annotation_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationCreateResponse,
        )

    def update(
        self,
        annotation_uuid: str,
        *,
        project_uuid: str,
        assigned_to: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[object] | NotGiven = NOT_GIVEN,
        label: Optional[Label] | NotGiven = NOT_GIVEN,
        reasoning: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[EvaluationType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationPublic:
        """
        Update an annotation.

        Args:
          label: Label enum

          type: Evaluation type enum

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not annotation_uuid:
            raise ValueError(f"Expected a non-empty value for `annotation_uuid` but received {annotation_uuid!r}")
        return self._patch(
            f"/ee/projects/{project_uuid}/annotations/{annotation_uuid}",
            body=maybe_transform(
                {
                    "assigned_to": assigned_to,
                    "data": data,
                    "label": label,
                    "reasoning": reasoning,
                    "type": type,
                },
                annotation_update_params.AnnotationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationPublic,
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

    async def create(
        self,
        project_uuid: str,
        *,
        body: Iterable[annotation_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationCreateResponse:
        """Create an annotation.

        Args: project_uuid: The project UUID.

        annotations_service: The annotation
        service. annotations_create: The annotation create model.

        Returns: AnnotationPublic: The created annotation.

        Raises: HTTPException: If the span has already been assigned to a user and has
        not been labeled yet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return await self._post(
            f"/ee/projects/{project_uuid}/annotations",
            body=await async_maybe_transform(body, Iterable[annotation_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationCreateResponse,
        )

    async def update(
        self,
        annotation_uuid: str,
        *,
        project_uuid: str,
        assigned_to: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[object] | NotGiven = NOT_GIVEN,
        label: Optional[Label] | NotGiven = NOT_GIVEN,
        reasoning: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[EvaluationType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationPublic:
        """
        Update an annotation.

        Args:
          label: Label enum

          type: Evaluation type enum

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not annotation_uuid:
            raise ValueError(f"Expected a non-empty value for `annotation_uuid` but received {annotation_uuid!r}")
        return await self._patch(
            f"/ee/projects/{project_uuid}/annotations/{annotation_uuid}",
            body=await async_maybe_transform(
                {
                    "assigned_to": assigned_to,
                    "data": data,
                    "label": label,
                    "reasoning": reasoning,
                    "type": type,
                },
                annotation_update_params.AnnotationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationPublic,
        )


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.create = to_raw_response_wrapper(
            annotations.create,
        )
        self.update = to_raw_response_wrapper(
            annotations.update,
        )


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.create = async_to_raw_response_wrapper(
            annotations.create,
        )
        self.update = async_to_raw_response_wrapper(
            annotations.update,
        )


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.create = to_streamed_response_wrapper(
            annotations.create,
        )
        self.update = to_streamed_response_wrapper(
            annotations.update,
        )


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.create = async_to_streamed_response_wrapper(
            annotations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            annotations.update,
        )
