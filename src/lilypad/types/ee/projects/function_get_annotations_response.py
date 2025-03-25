# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .annotation_public import AnnotationPublic

__all__ = ["FunctionGetAnnotationsResponse"]

FunctionGetAnnotationsResponse: TypeAlias = List[AnnotationPublic]
