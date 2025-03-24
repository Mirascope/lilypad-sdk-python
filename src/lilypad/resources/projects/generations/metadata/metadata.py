# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .names import (
    NamesResource,
    AsyncNamesResource,
    NamesResourceWithRawResponse,
    AsyncNamesResourceWithRawResponse,
    NamesResourceWithStreamingResponse,
    AsyncNamesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def names(self) -> NamesResource:
        return NamesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def names(self) -> AsyncNamesResource:
        return AsyncNamesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mirascope/lilypad-sdk-python#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def names(self) -> NamesResourceWithRawResponse:
        return NamesResourceWithRawResponse(self._metadata.names)


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def names(self) -> AsyncNamesResourceWithRawResponse:
        return AsyncNamesResourceWithRawResponse(self._metadata.names)


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def names(self) -> NamesResourceWithStreamingResponse:
        return NamesResourceWithStreamingResponse(self._metadata.names)


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

    @cached_property
    def names(self) -> AsyncNamesResourceWithStreamingResponse:
        return AsyncNamesResourceWithStreamingResponse(self._metadata.names)
