# LlmFunctions

Types:

```python
from lilypad_sdk.types import LlmFunctionBasePublic, LlmFunctionTable, LlmFunctionListResponse
```

Methods:

- <code title="post /llm-functions/">client.llm_functions.<a href="./src/lilypad_sdk/resources/llm_functions/llm_functions.py">create</a>(\*\*<a href="src/lilypad_sdk/types/llm_function_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/llm_function_base_public.py">LlmFunctionBasePublic</a></code>
- <code title="get /llm-functions/{version_hash}">client.llm_functions.<a href="./src/lilypad_sdk/resources/llm_functions/llm_functions.py">retrieve</a>(version_hash) -> <a href="./src/lilypad_sdk/types/llm_function_base_public.py">LlmFunctionBasePublic</a></code>
- <code title="get /llm-functions">client.llm_functions.<a href="./src/lilypad_sdk/resources/llm_functions/llm_functions.py">list</a>(\*\*<a href="src/lilypad_sdk/types/llm_function_list_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/llm_function_list_response.py">LlmFunctionListResponse</a></code>

## Names

Types:

```python
from lilypad_sdk.types.llm_functions import NameListResponse
```

Methods:

- <code title="get /llm-functions/names">client.llm_functions.names.<a href="./src/lilypad_sdk/resources/llm_functions/names.py">list</a>() -> <a href="./src/lilypad_sdk/types/llm_functions/name_list_response.py">NameListResponse</a></code>

## ProviderCallParams

Types:

```python
from lilypad_sdk.types.llm_functions import CallArgsPublic, ProviderCallParamsTable
```

Methods:

- <code title="post /llm-functions/{llm_function_id}/provider-call-params">client.llm_functions.provider_call_params.<a href="./src/lilypad_sdk/resources/llm_functions/provider_call_params.py">create</a>(llm_function_id, \*\*<a href="src/lilypad_sdk/types/llm_functions/provider_call_param_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/llm_functions/provider_call_params_table.py">ProviderCallParamsTable</a></code>
- <code title="get /llm-functions/{version_hash}/provider-call-params">client.llm_functions.provider_call_params.<a href="./src/lilypad_sdk/resources/llm_functions/provider_call_params.py">retrieve</a>(version_hash) -> <a href="./src/lilypad_sdk/types/llm_functions/call_args_public.py">CallArgsPublic</a></code>

# Metrics

Types:

```python
from lilypad_sdk.types import MetricCreateResponse
```

Methods:

- <code title="post /v1/metrics">client.metrics.<a href="./src/lilypad_sdk/resources/metrics.py">create</a>() -> <a href="./src/lilypad_sdk/types/metric_create_response.py">object</a></code>

# Traces

Types:

```python
from lilypad_sdk.types import SpanPublic, TraceCreateResponse, TraceListResponse
```

Methods:

- <code title="post /v1/traces">client.traces.<a href="./src/lilypad_sdk/resources/traces.py">create</a>() -> <a href="./src/lilypad_sdk/types/trace_create_response.py">object</a></code>
- <code title="get /traces">client.traces.<a href="./src/lilypad_sdk/resources/traces.py">list</a>() -> <a href="./src/lilypad_sdk/types/trace_list_response.py">TraceListResponse</a></code>
