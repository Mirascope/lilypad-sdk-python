# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CallCreateParams"]


class CallCreateParams(TypedDict, total=False):
    input: Required[str]

    output: Required[str]

    project_name: Required[str]
