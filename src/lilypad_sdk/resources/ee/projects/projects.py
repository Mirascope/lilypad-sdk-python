# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .spans import (
    SpansResource,
    AsyncSpansResource,
    SpansResourceWithRawResponse,
    AsyncSpansResourceWithRawResponse,
    SpansResourceWithStreamingResponse,
    AsyncSpansResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .annotations import (
    AnnotationsResource,
    AsyncAnnotationsResource,
    AnnotationsResourceWithRawResponse,
    AsyncAnnotationsResourceWithRawResponse,
    AnnotationsResourceWithStreamingResponse,
    AsyncAnnotationsResourceWithStreamingResponse,
)
from .generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .environments import (
    EnvironmentsResource,
    AsyncEnvironmentsResource,
    EnvironmentsResourceWithRawResponse,
    AsyncEnvironmentsResourceWithRawResponse,
    EnvironmentsResourceWithStreamingResponse,
    AsyncEnvironmentsResourceWithStreamingResponse,
)

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def annotations(self) -> AnnotationsResource:
        return AnnotationsResource(self._client)

    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def spans(self) -> SpansResource:
        return SpansResource(self._client)

    @cached_property
    def environments(self) -> EnvironmentsResource:
        return EnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def annotations(self) -> AsyncAnnotationsResource:
        return AsyncAnnotationsResource(self._client)

    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def spans(self) -> AsyncSpansResource:
        return AsyncSpansResource(self._client)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResource:
        return AsyncEnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

    @cached_property
    def annotations(self) -> AnnotationsResourceWithRawResponse:
        return AnnotationsResourceWithRawResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._projects.generations)

    @cached_property
    def spans(self) -> SpansResourceWithRawResponse:
        return SpansResourceWithRawResponse(self._projects.spans)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithRawResponse:
        return EnvironmentsResourceWithRawResponse(self._projects.environments)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

    @cached_property
    def annotations(self) -> AsyncAnnotationsResourceWithRawResponse:
        return AsyncAnnotationsResourceWithRawResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._projects.generations)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithRawResponse:
        return AsyncSpansResourceWithRawResponse(self._projects.spans)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithRawResponse:
        return AsyncEnvironmentsResourceWithRawResponse(self._projects.environments)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

    @cached_property
    def annotations(self) -> AnnotationsResourceWithStreamingResponse:
        return AnnotationsResourceWithStreamingResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._projects.generations)

    @cached_property
    def spans(self) -> SpansResourceWithStreamingResponse:
        return SpansResourceWithStreamingResponse(self._projects.spans)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithStreamingResponse:
        return EnvironmentsResourceWithStreamingResponse(self._projects.environments)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

    @cached_property
    def annotations(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        return AsyncAnnotationsResourceWithStreamingResponse(self._projects.annotations)

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._projects.generations)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithStreamingResponse:
        return AsyncSpansResourceWithStreamingResponse(self._projects.spans)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        return AsyncEnvironmentsResourceWithStreamingResponse(self._projects.environments)
