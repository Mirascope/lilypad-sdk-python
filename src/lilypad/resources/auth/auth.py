# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .github import (
    GitHubResource,
    AsyncGitHubResource,
    GitHubResourceWithRawResponse,
    AsyncGitHubResourceWithRawResponse,
    GitHubResourceWithStreamingResponse,
    AsyncGitHubResourceWithStreamingResponse,
)
from .google import (
    GoogleResource,
    AsyncGoogleResource,
    GoogleResourceWithRawResponse,
    AsyncGoogleResourceWithRawResponse,
    GoogleResourceWithStreamingResponse,
    AsyncGoogleResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def github(self) -> GitHubResource:
        return GitHubResource(self._client)

    @cached_property
    def google(self) -> GoogleResource:
        return GoogleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def github(self) -> AsyncGitHubResource:
        return AsyncGitHubResource(self._client)

    @cached_property
    def google(self) -> AsyncGoogleResource:
        return AsyncGoogleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def github(self) -> GitHubResourceWithRawResponse:
        return GitHubResourceWithRawResponse(self._auth.github)

    @cached_property
    def google(self) -> GoogleResourceWithRawResponse:
        return GoogleResourceWithRawResponse(self._auth.google)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def github(self) -> AsyncGitHubResourceWithRawResponse:
        return AsyncGitHubResourceWithRawResponse(self._auth.github)

    @cached_property
    def google(self) -> AsyncGoogleResourceWithRawResponse:
        return AsyncGoogleResourceWithRawResponse(self._auth.google)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def github(self) -> GitHubResourceWithStreamingResponse:
        return GitHubResourceWithStreamingResponse(self._auth.github)

    @cached_property
    def google(self) -> GoogleResourceWithStreamingResponse:
        return GoogleResourceWithStreamingResponse(self._auth.google)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def github(self) -> AsyncGitHubResourceWithStreamingResponse:
        return AsyncGitHubResourceWithStreamingResponse(self._auth.github)

    @cached_property
    def google(self) -> AsyncGoogleResourceWithStreamingResponse:
        return AsyncGoogleResourceWithStreamingResponse(self._auth.google)
