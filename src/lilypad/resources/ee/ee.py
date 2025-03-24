# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from .projects.projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from .user_organizations import (
    UserOrganizationsResource,
    AsyncUserOrganizationsResource,
    UserOrganizationsResourceWithRawResponse,
    AsyncUserOrganizationsResourceWithRawResponse,
    UserOrganizationsResourceWithStreamingResponse,
    AsyncUserOrganizationsResourceWithStreamingResponse,
)

__all__ = ["EeResource", "AsyncEeResource"]


class EeResource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def user_organizations(self) -> UserOrganizationsResource:
        return UserOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return EeResourceWithStreamingResponse(self)


class AsyncEeResource(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def user_organizations(self) -> AsyncUserOrganizationsResource:
        return AsyncUserOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncEeResourceWithStreamingResponse(self)


class EeResourceWithRawResponse:
    def __init__(self, ee: EeResource) -> None:
        self._ee = ee

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._ee.projects)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._ee.organizations)

    @cached_property
    def user_organizations(self) -> UserOrganizationsResourceWithRawResponse:
        return UserOrganizationsResourceWithRawResponse(self._ee.user_organizations)


class AsyncEeResourceWithRawResponse:
    def __init__(self, ee: AsyncEeResource) -> None:
        self._ee = ee

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._ee.projects)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._ee.organizations)

    @cached_property
    def user_organizations(self) -> AsyncUserOrganizationsResourceWithRawResponse:
        return AsyncUserOrganizationsResourceWithRawResponse(self._ee.user_organizations)


class EeResourceWithStreamingResponse:
    def __init__(self, ee: EeResource) -> None:
        self._ee = ee

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._ee.projects)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._ee.organizations)

    @cached_property
    def user_organizations(self) -> UserOrganizationsResourceWithStreamingResponse:
        return UserOrganizationsResourceWithStreamingResponse(self._ee.user_organizations)


class AsyncEeResourceWithStreamingResponse:
    def __init__(self, ee: AsyncEeResource) -> None:
        self._ee = ee

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._ee.projects)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._ee.organizations)

    @cached_property
    def user_organizations(self) -> AsyncUserOrganizationsResourceWithStreamingResponse:
        return AsyncUserOrganizationsResourceWithStreamingResponse(self._ee.user_organizations)
