# PromptVersions

Types:

```python
from lilypad_sdk.types import PromptVersionPublic
```

Methods:

- <code title="get /prompt-versions/{version_hash}">client.prompt_versions.<a href="./src/lilypad_sdk/resources/prompt_versions.py">retrieve</a>(version_hash) -> <a href="./src/lilypad_sdk/types/prompt_version_public.py">PromptVersionPublic</a></code>

# Calls

Types:

```python
from lilypad_sdk.types import CallPublicWithPromptVersion, CallCreateResponse, CallListResponse
```

Methods:

- <code title="post /calls">client.calls.<a href="./src/lilypad_sdk/resources/calls.py">create</a>(\*\*<a href="src/lilypad_sdk/types/call_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/call_create_response.py">CallCreateResponse</a></code>
- <code title="get /calls">client.calls.<a href="./src/lilypad_sdk/resources/calls.py">list</a>() -> <a href="./src/lilypad_sdk/types/call_list_response.py">CallListResponse</a></code>
