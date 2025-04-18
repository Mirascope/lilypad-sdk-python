from typing import Any

import orjson


def json_dumps(obj: Any) -> str:
    """Serialize Python objects to JSON using orjson."""
    # json should be utf-8 encoded, json key should be str
    return orjson.dumps(obj, option=orjson.OPT_NON_STR_KEYS).decode("utf-8")

