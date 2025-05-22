# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NameListPaginatedParams"]


class NameListPaginatedParams(TypedDict, total=False):
    project_uuid: Required[str]

    limit: int

    offset: int

    order: Literal["asc", "desc"]
