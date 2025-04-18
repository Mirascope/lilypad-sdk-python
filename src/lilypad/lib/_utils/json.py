from typing import Any

import orjson


def json_dumps(obj: Any) -> str:
    """Serialize Python objects to JSON using orjson."""
    # json should be utf-8 encoded
    return orjson.dumps(obj).decode("utf-8")

