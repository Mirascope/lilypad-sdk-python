# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .spans import (
    SpansResource,
    AsyncSpansResource,
    SpansResourceWithRawResponse,
    AsyncSpansResourceWithRawResponse,
    SpansResourceWithStreamingResponse,
    AsyncSpansResourceWithStreamingResponse,
)
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
from ....types.projects import generation_create_params, generation_update_params
from .metadata.metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ....types.ee.projects.generation_public import GenerationPublic
from ....types.projects.generation_list_response import GenerationListResponse
from ....types.ee.projects.common_call_params_param import CommonCallParamsParam
from ....types.projects.generation_archive_response import GenerationArchiveResponse
from ....types.projects.generation_archive_by_name_response import GenerationArchiveByNameResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def spans(self) -> SpansResource:
        return SpansResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)

    def create(
        self,
        project_uuid_1: str,
        *,
        code: str,
        hash: str,
        name: str,
        signature: str,
        archived: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        arg_types: Dict[str, str] | NotGiven = NOT_GIVEN,
        call_params: CommonCallParamsParam | NotGiven = NOT_GIVEN,
        custom_id: Optional[str] | NotGiven = NOT_GIVEN,
        dependencies: Dict[str, generation_create_params.Dependencies] | NotGiven = NOT_GIVEN,
        is_default: Optional[bool] | NotGiven = NOT_GIVEN,
        is_managed: Optional[bool] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        project_uuid_2: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_template: Optional[str] | NotGiven = NOT_GIVEN,
        provider: Optional[str] | NotGiven = NOT_GIVEN,
        version_num: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Create a new generation version.

        Args:
          call_params: Common parameters shared across LLM providers.

              Note: Each provider may handle these parameters differently or not support them
              at all. Please check provider-specific documentation for parameter support and
              behavior.

              Attributes: temperature: Controls randomness in the output (0.0 to 1.0).
              max_tokens: Maximum number of tokens to generate. top_p: Nucleus sampling
              parameter (0.0 to 1.0). frequency_penalty: Penalizes frequent tokens (-2.0 to
              2.0). presence_penalty: Penalizes tokens based on presence (-2.0 to 2.0). seed:
              Random seed for reproducibility. stop: Stop sequence(s) to end generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid_1:
            raise ValueError(f"Expected a non-empty value for `project_uuid_1` but received {project_uuid_1!r}")
        return self._post(
            f"/projects/{project_uuid_1}/generations",
            body=maybe_transform(
                {
                    "code": code,
                    "hash": hash,
                    "name": name,
                    "signature": signature,
                    "archived": archived,
                    "arg_types": arg_types,
                    "call_params": call_params,
                    "custom_id": custom_id,
                    "dependencies": dependencies,
                    "is_default": is_default,
                    "is_managed": is_managed,
                    "model": model,
                    "project_uuid_2": project_uuid_2,
                    "prompt_template": prompt_template,
                    "provider": provider,
                    "version_num": version_num,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    def retrieve(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Grab generation by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/generations/{generation_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    def update(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        is_default: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Update a generation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return self._patch(
            f"/projects/{project_uuid}/generations/{generation_uuid}",
            body=maybe_transform({"is_default": is_default}, generation_update_params.GenerationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    def list(
        self,
        project_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationListResponse:
        """
        Grab all generations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return self._get(
            f"/projects/{project_uuid}/generations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationListResponse,
        )

    def archive(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationArchiveResponse:
        """
        Archive a generation and delete spans by generation UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return self._delete(
            f"/projects/{project_uuid}/generations/{generation_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationArchiveResponse,
        )

    def archive_by_name(
        self,
        generation_name: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationArchiveByNameResponse:
        """
        Archive a generation by name and delete spans by generation name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return self._delete(
            f"/projects/{project_uuid}/generations/names/{generation_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationArchiveByNameResponse,
        )

    def retrieve_by_hash(
        self,
        generation_hash: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Get generation by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_hash:
            raise ValueError(f"Expected a non-empty value for `generation_hash` but received {generation_hash!r}")
        return self._get(
            f"/projects/{project_uuid}/generations/hash/{generation_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def spans(self) -> AsyncSpansResource:
        return AsyncSpansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lilypad-sdk-python#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_uuid_1: str,
        *,
        code: str,
        hash: str,
        name: str,
        signature: str,
        archived: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        arg_types: Dict[str, str] | NotGiven = NOT_GIVEN,
        call_params: CommonCallParamsParam | NotGiven = NOT_GIVEN,
        custom_id: Optional[str] | NotGiven = NOT_GIVEN,
        dependencies: Dict[str, generation_create_params.Dependencies] | NotGiven = NOT_GIVEN,
        is_default: Optional[bool] | NotGiven = NOT_GIVEN,
        is_managed: Optional[bool] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        project_uuid_2: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_template: Optional[str] | NotGiven = NOT_GIVEN,
        provider: Optional[str] | NotGiven = NOT_GIVEN,
        version_num: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Create a new generation version.

        Args:
          call_params: Common parameters shared across LLM providers.

              Note: Each provider may handle these parameters differently or not support them
              at all. Please check provider-specific documentation for parameter support and
              behavior.

              Attributes: temperature: Controls randomness in the output (0.0 to 1.0).
              max_tokens: Maximum number of tokens to generate. top_p: Nucleus sampling
              parameter (0.0 to 1.0). frequency_penalty: Penalizes frequent tokens (-2.0 to
              2.0). presence_penalty: Penalizes tokens based on presence (-2.0 to 2.0). seed:
              Random seed for reproducibility. stop: Stop sequence(s) to end generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid_1:
            raise ValueError(f"Expected a non-empty value for `project_uuid_1` but received {project_uuid_1!r}")
        return await self._post(
            f"/projects/{project_uuid_1}/generations",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "hash": hash,
                    "name": name,
                    "signature": signature,
                    "archived": archived,
                    "arg_types": arg_types,
                    "call_params": call_params,
                    "custom_id": custom_id,
                    "dependencies": dependencies,
                    "is_default": is_default,
                    "is_managed": is_managed,
                    "model": model,
                    "project_uuid_2": project_uuid_2,
                    "prompt_template": prompt_template,
                    "provider": provider,
                    "version_num": version_num,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    async def retrieve(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Grab generation by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/generations/{generation_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    async def update(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        is_default: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Update a generation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return await self._patch(
            f"/projects/{project_uuid}/generations/{generation_uuid}",
            body=await async_maybe_transform(
                {"is_default": is_default}, generation_update_params.GenerationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )

    async def list(
        self,
        project_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationListResponse:
        """
        Grab all generations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        return await self._get(
            f"/projects/{project_uuid}/generations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationListResponse,
        )

    async def archive(
        self,
        generation_uuid: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationArchiveResponse:
        """
        Archive a generation and delete spans by generation UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_uuid:
            raise ValueError(f"Expected a non-empty value for `generation_uuid` but received {generation_uuid!r}")
        return await self._delete(
            f"/projects/{project_uuid}/generations/{generation_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationArchiveResponse,
        )

    async def archive_by_name(
        self,
        generation_name: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationArchiveByNameResponse:
        """
        Archive a generation by name and delete spans by generation name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_name:
            raise ValueError(f"Expected a non-empty value for `generation_name` but received {generation_name!r}")
        return await self._delete(
            f"/projects/{project_uuid}/generations/names/{generation_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationArchiveByNameResponse,
        )

    async def retrieve_by_hash(
        self,
        generation_hash: str,
        *,
        project_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationPublic:
        """
        Get generation by hash.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_uuid:
            raise ValueError(f"Expected a non-empty value for `project_uuid` but received {project_uuid!r}")
        if not generation_hash:
            raise ValueError(f"Expected a non-empty value for `generation_hash` but received {generation_hash!r}")
        return await self._get(
            f"/projects/{project_uuid}/generations/hash/{generation_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationPublic,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_raw_response_wrapper(
            generations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            generations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            generations.update,
        )
        self.list = to_raw_response_wrapper(
            generations.list,
        )
        self.archive = to_raw_response_wrapper(
            generations.archive,
        )
        self.archive_by_name = to_raw_response_wrapper(
            generations.archive_by_name,
        )
        self.retrieve_by_hash = to_raw_response_wrapper(
            generations.retrieve_by_hash,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._generations.metadata)

    @cached_property
    def spans(self) -> SpansResourceWithRawResponse:
        return SpansResourceWithRawResponse(self._generations.spans)


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_raw_response_wrapper(
            generations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            generations.update,
        )
        self.list = async_to_raw_response_wrapper(
            generations.list,
        )
        self.archive = async_to_raw_response_wrapper(
            generations.archive,
        )
        self.archive_by_name = async_to_raw_response_wrapper(
            generations.archive_by_name,
        )
        self.retrieve_by_hash = async_to_raw_response_wrapper(
            generations.retrieve_by_hash,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._generations.metadata)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithRawResponse:
        return AsyncSpansResourceWithRawResponse(self._generations.spans)


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_streamed_response_wrapper(
            generations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            generations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            generations.update,
        )
        self.list = to_streamed_response_wrapper(
            generations.list,
        )
        self.archive = to_streamed_response_wrapper(
            generations.archive,
        )
        self.archive_by_name = to_streamed_response_wrapper(
            generations.archive_by_name,
        )
        self.retrieve_by_hash = to_streamed_response_wrapper(
            generations.retrieve_by_hash,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._generations.metadata)

    @cached_property
    def spans(self) -> SpansResourceWithStreamingResponse:
        return SpansResourceWithStreamingResponse(self._generations.spans)


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_streamed_response_wrapper(
            generations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            generations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            generations.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            generations.archive,
        )
        self.archive_by_name = async_to_streamed_response_wrapper(
            generations.archive_by_name,
        )
        self.retrieve_by_hash = async_to_streamed_response_wrapper(
            generations.retrieve_by_hash,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._generations.metadata)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithStreamingResponse:
        return AsyncSpansResourceWithStreamingResponse(self._generations.spans)
