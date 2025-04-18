import datetime
import dataclasses
from re import Pattern
from enum import Enum
from uuid import UUID
from types import GeneratorType
from typing import (
    Any,
    TypeVar,
    ParamSpec,
)
from decimal import Decimal
from pathlib import Path, PurePath
from ipaddress import (
    IPv4Address,
    IPv4Network,
    IPv6Address,
    IPv6Network,
    IPv4Interface,
    IPv6Interface,
)
from collections import deque, defaultdict
from collections.abc import Callable

from pydantic import BaseModel

_P = ParamSpec("_P")
_R = TypeVar("_R")

MAP_STANDARD_TYPES = {
    "List": "list",
    "Dict": "dict",
    "Set": "set",
    "Tuple": "tuple",
    "NoneType": "None",
}

import orjson

ORJSON_OPTS = (
    orjson.OPT_NON_STR_KEYS
    | orjson.OPT_NAIVE_UTC
    | orjson.OPT_SERIALIZE_NUMPY
    | orjson.OPT_SERIALIZE_DATACLASS
    | orjson.OPT_SERIALIZE_UUID
)

_PRIMITIVES = (str, int, float, bool, type(None))


IncEx = set[str] | dict[str, Any]


# Helper function for date and time formatting
def isoformat(o: datetime.date | datetime.time) -> str:
    """Convert date or time object to ISO format string"""
    return o.isoformat()


# Helper function for decimal encoding
def decimal_encoder(dec_value: Decimal) -> int | float:
    """Encodes a Decimal as int if there's no exponent, otherwise float

    This is useful when we use ConstrainedDecimal to represent Numeric(x,0)
    where a integer (but not int typed) is used. Encoding this as a float
    results in failed round-tripping between encode and parse.

    >>> decimal_encoder(Decimal("1.0"))
    1.0

    >>> decimal_encoder(Decimal("1"))
    1
    """
    tup = dec_value.as_tuple()
    if isinstance(tup.exponent, int) and tup.exponent >= 0:
        return int(dec_value)
    else:
        return float(dec_value)


ENCODERS_BY_TYPE: dict[type[Any], Callable[[Any], Any]] = {
    bytes: lambda o: o.decode(),
    datetime.date: isoformat,
    datetime.datetime: isoformat,
    datetime.time: isoformat,
    datetime.timedelta: lambda td: td.total_seconds(),
    Decimal: decimal_encoder,
    Enum: lambda o: o.value,
    frozenset: list,
    deque: list,
    GeneratorType: list,
    IPv4Address: str,
    IPv4Interface: str,
    IPv4Network: str,
    IPv6Address: str,
    IPv6Interface: str,
    IPv6Network: str,
    Path: str,
    Pattern: lambda o: o.pattern,
    set: list,
    UUID: str,
}


def generate_encoders_by_class_tuples(
    type_encoder_map: dict[Any, Callable[[Any], Any]],
) -> dict[Callable[[Any], Any], tuple[Any, ...]]:
    """Generate a mapping of encoder functions to tuples of types they can handle"""
    encoders_by_class_tuples: dict[Callable[[Any], Any], tuple[Any, ...]] = defaultdict(tuple)
    for type_, encoder in type_encoder_map.items():
        encoders_by_class_tuples[encoder] += (type_,)
    return encoders_by_class_tuples


# Pre-compute the encoder lookup table
encoders_by_class_tuples = generate_encoders_by_class_tuples(ENCODERS_BY_TYPE)


class UndefinedType:
    """A class to represent undefined values"""

    pass


def jsonable_encoder(
    obj: Any,
    include: IncEx | None = None,
    exclude: IncEx | None = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    custom_encoder: dict[Any, Callable[[Any], Any]] | None = None,
    sqlalchemy_safe: bool = True,
) -> Any:
    """Convert any object to something that can be encoded in JSON.

    This utility function converts various Python objects into JSON-compatible types.
    It handles Pydantic models, dataclasses, enums, paths, dictionaries, lists, and more.

    Parameters:
    -----------
    obj : Any
        The input object to convert to JSON.

    include : Optional[IncEx]
        Fields to include in the output.

    exclude : Optional[IncEx]
        Fields to exclude from the output.

    by_alias : bool
        Whether to use field aliases from Pydantic models.

    exclude_unset : bool
        Whether to exclude unset fields from Pydantic models.

    exclude_defaults : bool
        Whether to exclude fields with default values from Pydantic models.

    exclude_none : bool
        Whether to exclude fields with None values.

    custom_encoder : Optional[Dict[Any, Callable[[Any], Any]]]
        Custom encoders for specific types.

    sqlalchemy_safe : bool
        Whether to exclude SQLAlchemy internal fields.

    Returns:
    --------
    Any
        A JSON-compatible representation of the input object.
    """
    custom_encoder = custom_encoder or {}

    # Apply custom encoder if available for this type
    if custom_encoder:
        if type(obj) in custom_encoder:
            return custom_encoder[type(obj)](obj)
        else:
            for encoder_type, encoder_instance in custom_encoder.items():
                if isinstance(obj, encoder_type):
                    return encoder_instance(obj)

    # Convert sets to lists for include/exclude parameters
    if include is not None and not isinstance(include, set | dict):
        include = set(include)
    if exclude is not None and not isinstance(exclude, set | dict):
        exclude = set(exclude)

    # Handle Pydantic models
    if isinstance(obj, BaseModel):
        # Convert model to dict using Pydantic v2 approach
        obj_dict = obj.model_dump(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_none=exclude_none,
            exclude_defaults=exclude_defaults,
        )

        # Handle root models
        if "__root__" in obj_dict:
            obj_dict = obj_dict["__root__"]

        # Recursively encode the resulting dict
        return jsonable_encoder(
            obj_dict,
            exclude_none=exclude_none,
            exclude_defaults=exclude_defaults,
            custom_encoder=custom_encoder,
            sqlalchemy_safe=sqlalchemy_safe,
        )

    # Handle dataclasses
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        obj_dict = dataclasses.asdict(obj)
        return jsonable_encoder(
            obj_dict,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            custom_encoder=custom_encoder,
            sqlalchemy_safe=sqlalchemy_safe,
        )

    # Handle Enum types
    if isinstance(obj, Enum):
        return obj.value

    # Handle Path objects
    if isinstance(obj, PurePath):
        return str(obj)

    # Handle primitive types directly
    if isinstance(obj, str | int | float | type(None)):
        return obj

    # Handle undefined values
    if isinstance(obj, UndefinedType):
        return None

    # Handle dictionaries
    if isinstance(obj, dict):
        encoded_dict = {}
        allowed_keys = set(obj.keys())

        if include is not None:
            allowed_keys &= set(include)
        if exclude is not None:
            allowed_keys -= set(exclude)

        for key, value in obj.items():
            if (
                (not sqlalchemy_safe or (not isinstance(key, str)) or (not key.startswith("_sa")))
                and (value is not None or not exclude_none)
                and key in allowed_keys
            ):
                encoded_key = jsonable_encoder(
                    key,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_none=exclude_none,
                    custom_encoder=custom_encoder,
                    sqlalchemy_safe=sqlalchemy_safe,
                )
                encoded_value = jsonable_encoder(
                    value,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_none=exclude_none,
                    custom_encoder=custom_encoder,
                    sqlalchemy_safe=sqlalchemy_safe,
                )
                encoded_dict[encoded_key] = encoded_value
        return encoded_dict

    # Handle sequences (list, set, etc.)
    if isinstance(obj, list | set | frozenset | GeneratorType | tuple | deque):
        encoded_list = []
        for item in obj:
            encoded_list.append(
                jsonable_encoder(
                    item,
                    include=include,
                    exclude=exclude,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    exclude_none=exclude_none,
                    custom_encoder=custom_encoder,
                    sqlalchemy_safe=sqlalchemy_safe,
                )
            )
        return encoded_list

    # Handle types with specific encoders
    if type(obj) in ENCODERS_BY_TYPE:
        return ENCODERS_BY_TYPE[type(obj)](obj)

    # Check all registered encoders (more efficient for inheritance hierarchies)
    for encoder, classes_tuple in encoders_by_class_tuples.items():
        if isinstance(obj, classes_tuple):
            return encoder(obj)

    # Handle objects without any specific encoder
    # Try to convert to dict first, then fall back to vars()
    try:
        from collections.abc import Mapping

        if isinstance(obj, Mapping):
            data = dict(obj)
        elif isinstance(obj, type):
            data = vars(obj)
        elif hasattr(obj, "__iter__"):
            data = dict(obj)
        else:
            data = vars(obj)
    except Exception as e:
        errors: list[Exception] = [e]
        try:
            data = vars(obj)
        except Exception as e:
            errors.append(e)
            raise ValueError(errors) from e

    # Recursively encode the resulting dict
    return jsonable_encoder(
        data,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        custom_encoder=custom_encoder,
        sqlalchemy_safe=sqlalchemy_safe,
    )


def json_dumps(obj: Any) -> str:
    """Serialize Python objects to JSON using orjson."""
    # json should be utf-8 encoded, json key should be str
    return orjson.dumps(obj, option=ORJSON_OPTS).decode("utf-8")


def _to_json_serializable(obj: Any) -> Any:
    """Convert Python objects to JSON serializable format."""
    if isinstance(obj, BaseModel):
        return obj.model_dump(mode="json")
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return dataclasses.asdict(obj)
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, PurePath):
        return str(obj)
    return obj


def fast_jsonable(val: Any) -> str | int | float | bool | None:
    """Convert a value to a JSON serializable format."""
    if isinstance(val, _PRIMITIVES):
        return val

    try:
        return orjson.dumps(_to_json_serializable(val), option=ORJSON_OPTS).decode("utf-8")
    except TypeError:
        return orjson.dumps(jsonable_encoder(val), option=ORJSON_OPTS).decode("utf-8")


__all__ = [
    "json_dumps",
    "fast_jsonable",
]
