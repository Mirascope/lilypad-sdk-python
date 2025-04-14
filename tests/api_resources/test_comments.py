# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lilypad import Lilypad, AsyncLilypad
from tests.utils import assert_matches_type
from lilypad.types import (
    CommentListResponse,
    CommentCreateResponse,
    CommentDeleteResponse,
    CommentUpdateResponse,
    CommentRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Lilypad) -> None:
        comment = client.comments.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Lilypad) -> None:
        comment = client.comments.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            parent_comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Lilypad) -> None:
        response = client.comments.with_raw_response.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Lilypad) -> None:
        with client.comments.with_streaming_response.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Lilypad) -> None:
        comment = client.comments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Lilypad) -> None:
        response = client.comments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Lilypad) -> None:
        with client.comments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_uuid` but received ''"):
            client.comments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Lilypad) -> None:
        comment = client.comments.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Lilypad) -> None:
        comment = client.comments.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_edited=True,
            text="text",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Lilypad) -> None:
        response = client.comments.with_raw_response.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Lilypad) -> None:
        with client.comments.with_streaming_response.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentUpdateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_uuid` but received ''"):
            client.comments.with_raw_response.update(
                comment_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Lilypad) -> None:
        comment = client.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Lilypad) -> None:
        response = client.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Lilypad) -> None:
        with client.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Lilypad) -> None:
        comment = client.comments.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Lilypad) -> None:
        response = client.comments.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Lilypad) -> None:
        with client.comments.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Lilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_uuid` but received ''"):
            client.comments.with_raw_response.delete(
                "",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            parent_comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLilypad) -> None:
        response = await async_client.comments.with_raw_response.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLilypad) -> None:
        async with async_client.comments.with_streaming_response.create(
            span_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLilypad) -> None:
        response = await async_client.comments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLilypad) -> None:
        async with async_client.comments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_uuid` but received ''"):
            await async_client.comments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_edited=True,
            text="text",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLilypad) -> None:
        response = await async_client.comments.with_raw_response.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLilypad) -> None:
        async with async_client.comments.with_streaming_response.update(
            comment_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentUpdateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_uuid` but received ''"):
            await async_client.comments.with_raw_response.update(
                comment_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLilypad) -> None:
        response = await async_client.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLilypad) -> None:
        async with async_client.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncLilypad) -> None:
        comment = await async_client.comments.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLilypad) -> None:
        response = await async_client.comments.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLilypad) -> None:
        async with async_client.comments.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLilypad) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_uuid` but received ''"):
            await async_client.comments.with_raw_response.delete(
                "",
            )
