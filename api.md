# Ee

## Projects

### Annotations

Types:

```python
from lilypad.types.ee.projects import (
    AnnotationPublic,
    EvaluationType,
    Label,
    AnnotationCreateResponse,
    AnnotationListResponse,
    AnnotationDeleteResponse,
)
```

Methods:

- <code title="post /ee/projects/{project_uuid}/annotations">client.ee.projects.annotations.<a href="./src/lilypad/resources/ee/projects/annotations.py">create</a>(project_uuid, \*\*<a href="src/lilypad/types/ee/projects/annotation_create_params.py">params</a>) -> <a href="./src/lilypad/types/ee/projects/annotation_create_response.py">AnnotationCreateResponse</a></code>
- <code title="patch /ee/projects/{project_uuid}/annotations/{annotation_uuid}">client.ee.projects.annotations.<a href="./src/lilypad/resources/ee/projects/annotations.py">update</a>(annotation_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/ee/projects/annotation_update_params.py">params</a>) -> <a href="./src/lilypad/types/ee/projects/annotation_public.py">AnnotationPublic</a></code>
- <code title="get /ee/projects/{project_uuid}/annotations">client.ee.projects.annotations.<a href="./src/lilypad/resources/ee/projects/annotations.py">list</a>(project_uuid) -> <a href="./src/lilypad/types/ee/projects/annotation_list_response.py">AnnotationListResponse</a></code>
- <code title="delete /ee/projects/{project_uuid}/annotations/{annotation_uuid}">client.ee.projects.annotations.<a href="./src/lilypad/resources/ee/projects/annotations.py">delete</a>(annotation_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/annotation_delete_response.py">AnnotationDeleteResponse</a></code>

### Functions

Types:

```python
from lilypad.types.ee.projects import FunctionRunInPlaygroundResponse
```

Methods:

- <code title="post /ee/projects/{project_uuid}/functions/{function_uuid}/playground">client.ee.projects.functions.<a href="./src/lilypad/resources/ee/projects/functions/functions.py">run_in_playground</a>(function_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/ee/projects/function_run_in_playground_params.py">params</a>) -> <a href="./src/lilypad/types/ee/projects/function_run_in_playground_response.py">FunctionRunInPlaygroundResponse</a></code>

#### Annotations

Types:

```python
from lilypad.types.ee.projects.functions import AnnotationListResponse, AnnotationGetMetricsResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/functions/{function_uuid}/annotations">client.ee.projects.functions.annotations.<a href="./src/lilypad/resources/ee/projects/functions/annotations.py">list</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/functions/annotation_list_response.py">AnnotationListResponse</a></code>
- <code title="get /ee/projects/{project_uuid}/functions/{function_uuid}/annotations/metrics">client.ee.projects.functions.annotations.<a href="./src/lilypad/resources/ee/projects/functions/annotations.py">get_metrics</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/functions/annotation_get_metrics_response.py">AnnotationGetMetricsResponse</a></code>

### Spans

Types:

```python
from lilypad.types.ee.projects import SpanGenerateAnnotationResponse, SpanGetAnnotationsResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/spans/{span_uuid}/generate-annotation">client.ee.projects.spans.<a href="./src/lilypad/resources/ee/projects/spans.py">generate_annotation</a>(span_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/span_generate_annotation_response.py">object</a></code>
- <code title="get /ee/projects/{project_uuid}/spans/{span_uuid}/annotations">client.ee.projects.spans.<a href="./src/lilypad/resources/ee/projects/spans.py">get_annotations</a>(span_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/span_get_annotations_response.py">SpanGetAnnotationsResponse</a></code>

## Organizations

Types:

```python
from lilypad.types.ee import OrganizationGetLicenseResponse
```

Methods:

- <code title="get /ee/organizations/license">client.ee.organizations.<a href="./src/lilypad/resources/ee/organizations.py">get_license</a>() -> <a href="./src/lilypad/types/ee/organization_get_license_response.py">OrganizationGetLicenseResponse</a></code>

## UserOrganizations

Types:

```python
from lilypad.types.ee import (
    UserOrganizationTable,
    UserPublic,
    UserRole,
    UserOrganizationListResponse,
    UserOrganizationDeleteResponse,
    UserOrganizationListUsersResponse,
)
```

Methods:

- <code title="post /ee/user-organizations">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">create</a>(\*\*<a href="src/lilypad/types/ee/user_organization_create_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>
- <code title="patch /ee/user-organizations/{user_organization_uuid}">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">update</a>(user_organization_uuid, \*\*<a href="src/lilypad/types/ee/user_organization_update_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_organization_table.py">UserOrganizationTable</a></code>
- <code title="get /ee/user-organizations">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">list</a>() -> <a href="./src/lilypad/types/ee/user_organization_list_response.py">UserOrganizationListResponse</a></code>
- <code title="delete /ee/user-organizations/{user_organization_uuid}">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">delete</a>(user_organization_uuid) -> <a href="./src/lilypad/types/ee/user_organization_delete_response.py">UserOrganizationDeleteResponse</a></code>
- <code title="get /ee/user-organizations/users">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">list_users</a>() -> <a href="./src/lilypad/types/ee/user_organization_list_users_response.py">UserOrganizationListUsersResponse</a></code>

# APIKeys

Types:

```python
from lilypad.types import APIKeyCreateResponse, APIKeyListResponse, APIKeyDeleteResponse
```

Methods:

- <code title="post /api-keys">client.api_keys.<a href="./src/lilypad/resources/api_keys.py">create</a>(\*\*<a href="src/lilypad/types/api_key_create_params.py">params</a>) -> str</code>
- <code title="get /api-keys">client.api_keys.<a href="./src/lilypad/resources/api_keys.py">list</a>() -> <a href="./src/lilypad/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api-keys/{api_key_uuid}">client.api_keys.<a href="./src/lilypad/resources/api_keys.py">delete</a>(api_key_uuid) -> <a href="./src/lilypad/types/api_key_delete_response.py">APIKeyDeleteResponse</a></code>

# Webhooks

Types:

```python
from lilypad.types import WebhookHandleResponse
```

Methods:

- <code title="post /webhooks/stripe">client.webhooks.<a href="./src/lilypad/resources/webhooks.py">handle</a>() -> <a href="./src/lilypad/types/webhook_handle_response.py">WebhookHandleResponse</a></code>

# Projects

Types:

```python
from lilypad.types import (
    FunctionCreate,
    ProjectCreate,
    ProjectPublic,
    ProjectListResponse,
    ProjectDeleteResponse,
    ProjectRetrieveTagsResponse,
)
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/lilypad/resources/projects/projects.py">create</a>(\*\*<a href="src/lilypad/types/project_create_params.py">params</a>) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">retrieve</a>(project_uuid) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="patch /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">update</a>(project_uuid, \*\*<a href="src/lilypad/types/project_update_params.py">params</a>) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects">client.projects.<a href="./src/lilypad/resources/projects/projects.py">list</a>() -> <a href="./src/lilypad/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">delete</a>(project_uuid) -> <a href="./src/lilypad/types/project_delete_response.py">ProjectDeleteResponse</a></code>
- <code title="post /projects/{project_uuid}/versioned-functions">client.projects.<a href="./src/lilypad/resources/projects/projects.py">create_versioned_function</a>(path_project_uuid, \*\*<a href="src/lilypad/types/project_create_versioned_function_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="get /projects/{project_uuid}/tags">client.projects.<a href="./src/lilypad/resources/projects/projects.py">retrieve_tags</a>(project_uuid) -> <a href="./src/lilypad/types/project_retrieve_tags_response.py">ProjectRetrieveTagsResponse</a></code>

## Functions

Types:

```python
from lilypad.types.projects import (
    FunctionListResponse,
    FunctionArchiveResponse,
    FunctionArchiveByNameResponse,
)
```

Methods:

- <code title="post /projects/{project_uuid}/functions">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">create</a>(path_project_uuid, \*\*<a href="src/lilypad/types/projects/function_create_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="get /projects/{project_uuid}/functions/{function_uuid}">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">retrieve</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="patch /projects/{project_uuid}/functions/{function_uuid}">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">update</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="get /projects/{project_uuid}/functions">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">list</a>(project_uuid) -> <a href="./src/lilypad/types/projects/function_list_response.py">FunctionListResponse</a></code>
- <code title="delete /projects/{project_uuid}/functions/{function_uuid}">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">archive</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/function_archive_response.py">FunctionArchiveResponse</a></code>
- <code title="delete /projects/{project_uuid}/functions/names/{function_name}">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">archive_by_name</a>(function_name, \*, project_uuid) -> <a href="./src/lilypad/types/projects/function_archive_by_name_response.py">FunctionArchiveByNameResponse</a></code>
- <code title="get /projects/{project_uuid}/functions/hash/{function_hash}">client.projects.functions.<a href="./src/lilypad/resources/projects/functions/functions.py">retrieve_by_hash</a>(function_hash, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>

### Name

Types:

```python
from lilypad.types.projects.functions import (
    CommonCallParams,
    FunctionPublic,
    PaginatedSpanPublic,
    SpanPublic,
    NameRetrieveAggregatesResponse,
    NameRetrieveByNameResponse,
)
```

Methods:

- <code title="get /projects/{project_uuid}/functions/{function_uuid}/spans/paginated">client.projects.functions.name.<a href="./src/lilypad/resources/projects/functions/name.py">list_paginated</a>(function_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/projects/functions/name_list_paginated_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/paginated_span_public.py">PaginatedSpanPublic</a></code>
- <code title="get /projects/{project_uuid}/functions/{function_uuid}/spans/metadata">client.projects.functions.name.<a href="./src/lilypad/resources/projects/functions/name.py">retrieve_aggregates</a>(function_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/projects/functions/name_retrieve_aggregates_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/name_retrieve_aggregates_response.py">NameRetrieveAggregatesResponse</a></code>
- <code title="get /projects/{project_uuid}/functions/name/{function_name}">client.projects.functions.name.<a href="./src/lilypad/resources/projects/functions/name.py">retrieve_by_name</a>(function_name, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/name_retrieve_by_name_response.py">NameRetrieveByNameResponse</a></code>
- <code title="get /projects/{project_uuid}/functions/name/{function_name}/version/{version_num}">client.projects.functions.name.<a href="./src/lilypad/resources/projects/functions/name.py">retrieve_by_version</a>(version_num, \*, project_uuid, function_name) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="get /projects/{project_uuid}/functions/name/{function_name}/environments">client.projects.functions.name.<a href="./src/lilypad/resources/projects/functions/name.py">retrieve_deployed</a>(function_name, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>

### Metadata

#### Names

Types:

```python
from lilypad.types.projects.functions.metadata import (
    NameListResponse,
    NameListLatestVersionsResponse,
)
```

Methods:

- <code title="get /projects/{project_uuid}/functions/metadata/names">client.projects.functions.metadata.names.<a href="./src/lilypad/resources/projects/functions/metadata/names.py">list</a>(project_uuid) -> <a href="./src/lilypad/types/projects/functions/metadata/name_list_response.py">NameListResponse</a></code>
- <code title="get /projects/{project_uuid}/functions/metadata/names/versions">client.projects.functions.metadata.names.<a href="./src/lilypad/resources/projects/functions/metadata/names.py">list_latest_versions</a>(project_uuid) -> <a href="./src/lilypad/types/projects/functions/metadata/name_list_latest_versions_response.py">NameListLatestVersionsResponse</a></code>

## Spans

Types:

```python
from lilypad.types.projects import (
    AggregateMetrics,
    Scope,
    TimeFrame,
    SpanDeleteResponse,
    SpanRetrieveAggregatesResponse,
    SpanSearchTracesResponse,
)
```

Methods:

- <code title="delete /projects/{project_uuid}/spans/{span_uuid}">client.projects.spans.<a href="./src/lilypad/resources/projects/spans.py">delete</a>(span_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/span_delete_response.py">SpanDeleteResponse</a></code>
- <code title="get /projects/{project_uuid}/spans/metadata">client.projects.spans.<a href="./src/lilypad/resources/projects/spans.py">retrieve_aggregates</a>(project_uuid, \*\*<a href="src/lilypad/types/projects/span_retrieve_aggregates_params.py">params</a>) -> <a href="./src/lilypad/types/projects/span_retrieve_aggregates_response.py">SpanRetrieveAggregatesResponse</a></code>
- <code title="get /projects/{project_uuid}/spans/{span_id}">client.projects.spans.<a href="./src/lilypad/resources/projects/spans.py">retrieve_by_id</a>(span_id, \*, project_uuid) -> <a href="./src/lilypad/types/span_more_details.py">SpanMoreDetails</a></code>
- <code title="get /projects/{project_uuid}/spans">client.projects.spans.<a href="./src/lilypad/resources/projects/spans.py">search_traces</a>(project_uuid, \*\*<a href="src/lilypad/types/projects/span_search_traces_params.py">params</a>) -> <a href="./src/lilypad/types/projects/span_search_traces_response.py">SpanSearchTracesResponse</a></code>

## Traces

Types:

```python
from lilypad.types.projects import TraceCreateResponse
```

Methods:

- <code title="post /projects/{project_uuid}/traces">client.projects.traces.<a href="./src/lilypad/resources/projects/traces.py">create</a>(project_uuid) -> <a href="./src/lilypad/types/projects/trace_create_response.py">TraceCreateResponse</a></code>
- <code title="get /projects/{project_uuid}/traces">client.projects.traces.<a href="./src/lilypad/resources/projects/traces.py">list</a>(project_uuid, \*\*<a href="src/lilypad/types/projects/trace_list_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/paginated_span_public.py">PaginatedSpanPublic</a></code>
- <code title="get /projects/{project_uuid}/traces/{span_id}/root">client.projects.traces.<a href="./src/lilypad/resources/projects/traces.py">retrieve_by_span_id</a>(span_id, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/span_public.py">SpanPublic</a></code>

## Environments

Types:

```python
from lilypad.types.projects import DeploymentPublic, EnvironmentGetDeploymentHistoryResponse
```

Methods:

- <code title="post /projects/{project_uuid}/environments/{environment_uuid}/deploy">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">deploy_function</a>(environment_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/projects/environment_deploy_function_params.py">params</a>) -> <a href="./src/lilypad/types/projects/deployment_public.py">DeploymentPublic</a></code>
- <code title="get /projects/{project_uuid}/environments/{environment_uuid}/deployment">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">get_active_deployment</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/deployment_public.py">DeploymentPublic</a></code>
- <code title="get /projects/{project_uuid}/environments/{environment_uuid}/function">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">get_current_function</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="get /projects/{project_uuid}/environments/{environment_uuid}/history">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">get_deployment_history</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/environment_get_deployment_history_response.py">EnvironmentGetDeploymentHistoryResponse</a></code>

# OrganizationsInvites

Types:

```python
from lilypad.types import (
    OrganizationInvitePublic,
    OrganizationsInviteListResponse,
    OrganizationsInviteDeleteResponse,
)
```

Methods:

- <code title="post /organizations-invites">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">create</a>(\*\*<a href="src/lilypad/types/organizations_invite_create_params.py">params</a>) -> <a href="./src/lilypad/types/organization_invite_public.py">OrganizationInvitePublic</a></code>
- <code title="get /organizations-invites/{invite_token}">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">retrieve</a>(invite_token) -> <a href="./src/lilypad/types/organization_invite_public.py">OrganizationInvitePublic</a></code>
- <code title="get /organizations-invites/">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">list</a>() -> <a href="./src/lilypad/types/organizations_invite_list_response.py">OrganizationsInviteListResponse</a></code>
- <code title="delete /organizations-invites/{organization_invite_uuid}">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">delete</a>(organization_invite_uuid) -> <a href="./src/lilypad/types/organizations_invite_delete_response.py">OrganizationsInviteDeleteResponse</a></code>

# Spans

Types:

```python
from lilypad.types import SpanMoreDetails
```

Methods:

- <code title="get /spans/{span_uuid}">client.spans.<a href="./src/lilypad/resources/spans.py">retrieve</a>(span_uuid) -> <a href="./src/lilypad/types/span_more_details.py">SpanMoreDetails</a></code>
- <code title="patch /spans/{span_uuid}">client.spans.<a href="./src/lilypad/resources/spans.py">update</a>(span_uuid, \*\*<a href="src/lilypad/types/span_update_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/span_public.py">SpanPublic</a></code>

# Auth

## GitHub

Methods:

- <code title="get /auth/github/callback">client.auth.github.<a href="./src/lilypad/resources/auth/github.py">callback</a>(\*\*<a href="src/lilypad/types/auth/github_callback_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>

## Google

Methods:

- <code title="get /auth/google/callback">client.auth.google.<a href="./src/lilypad/resources/auth/google.py">callback</a>(\*\*<a href="src/lilypad/types/auth/google_callback_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>

# Users

Methods:

- <code title="put /users/{activeOrganizationUuid}">client.users.<a href="./src/lilypad/resources/users.py">update_active_organization</a>(active_organization_uuid) -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>
- <code title="patch /users">client.users.<a href="./src/lilypad/resources/users.py">update_keys</a>(\*\*<a href="src/lilypad/types/user_update_keys_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>

# CurrentUser

Methods:

- <code title="get /current-user">client.current_user.<a href="./src/lilypad/resources/current_user.py">retrieve</a>() -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>

# Organizations

Types:

```python
from lilypad.types import OrganizationPublic
```

Methods:

- <code title="post /organizations">client.organizations.<a href="./src/lilypad/resources/organizations.py">create</a>(\*\*<a href="src/lilypad/types/organization_create_params.py">params</a>) -> <a href="./src/lilypad/types/organization_public.py">OrganizationPublic</a></code>
- <code title="patch /organizations">client.organizations.<a href="./src/lilypad/resources/organizations.py">update</a>(\*\*<a href="src/lilypad/types/organization_update_params.py">params</a>) -> <a href="./src/lilypad/types/organization_public.py">OrganizationPublic</a></code>
- <code title="delete /organizations">client.organizations.<a href="./src/lilypad/resources/organizations.py">delete</a>() -> <a href="./src/lilypad/types/ee/user_public.py">UserPublic</a></code>

# ExternalAPIKeys

Types:

```python
from lilypad.types import (
    ExternalAPIKeyPublic,
    ExternalAPIKeyListResponse,
    ExternalAPIKeyDeleteResponse,
)
```

Methods:

- <code title="post /external-api-keys">client.external_api_keys.<a href="./src/lilypad/resources/external_api_keys.py">create</a>(\*\*<a href="src/lilypad/types/external_api_key_create_params.py">params</a>) -> <a href="./src/lilypad/types/external_api_key_public.py">ExternalAPIKeyPublic</a></code>
- <code title="get /external-api-keys/{service_name}">client.external_api_keys.<a href="./src/lilypad/resources/external_api_keys.py">retrieve</a>(service_name) -> <a href="./src/lilypad/types/external_api_key_public.py">ExternalAPIKeyPublic</a></code>
- <code title="patch /external-api-keys/{service_name}">client.external_api_keys.<a href="./src/lilypad/resources/external_api_keys.py">update</a>(service_name, \*\*<a href="src/lilypad/types/external_api_key_update_params.py">params</a>) -> <a href="./src/lilypad/types/external_api_key_public.py">ExternalAPIKeyPublic</a></code>
- <code title="get /external-api-keys">client.external_api_keys.<a href="./src/lilypad/resources/external_api_keys.py">list</a>() -> <a href="./src/lilypad/types/external_api_key_list_response.py">ExternalAPIKeyListResponse</a></code>
- <code title="delete /external-api-keys/{service_name}">client.external_api_keys.<a href="./src/lilypad/resources/external_api_keys.py">delete</a>(service_name) -> <a href="./src/lilypad/types/external_api_key_delete_response.py">ExternalAPIKeyDeleteResponse</a></code>

# Environments

Types:

```python
from lilypad.types import EnvironmentPublic, EnvironmentListResponse, EnvironmentDeleteResponse
```

Methods:

- <code title="post /environments">client.environments.<a href="./src/lilypad/resources/environments.py">create</a>(\*\*<a href="src/lilypad/types/environment_create_params.py">params</a>) -> <a href="./src/lilypad/types/environment_public.py">EnvironmentPublic</a></code>
- <code title="get /environments/{environment_uuid}">client.environments.<a href="./src/lilypad/resources/environments.py">retrieve</a>(environment_uuid) -> <a href="./src/lilypad/types/environment_public.py">EnvironmentPublic</a></code>
- <code title="get /environments">client.environments.<a href="./src/lilypad/resources/environments.py">list</a>() -> <a href="./src/lilypad/types/environment_list_response.py">EnvironmentListResponse</a></code>
- <code title="delete /environments/{environment_uuid}">client.environments.<a href="./src/lilypad/resources/environments.py">delete</a>(environment_uuid) -> <a href="./src/lilypad/types/environment_delete_response.py">EnvironmentDeleteResponse</a></code>

# UserConsents

Types:

```python
from lilypad.types import UserConsentPublic
```

Methods:

- <code title="post /user-consents">client.user_consents.<a href="./src/lilypad/resources/user_consents.py">create</a>(\*\*<a href="src/lilypad/types/user_consent_create_params.py">params</a>) -> <a href="./src/lilypad/types/user_consent_public.py">UserConsentPublic</a></code>
- <code title="patch /user-consents/{user_consent_uuid}">client.user_consents.<a href="./src/lilypad/resources/user_consents.py">update</a>(user_consent_uuid, \*\*<a href="src/lilypad/types/user_consent_update_params.py">params</a>) -> <a href="./src/lilypad/types/user_consent_public.py">UserConsentPublic</a></code>

# Tags

Types:

```python
from lilypad.types import TagCreate, TagPublic, TagListResponse, TagDeleteResponse
```

Methods:

- <code title="post /tags">client.tags.<a href="./src/lilypad/resources/tags.py">create</a>(\*\*<a href="src/lilypad/types/tag_create_params.py">params</a>) -> <a href="./src/lilypad/types/tag_public.py">TagPublic</a></code>
- <code title="get /tags/{tag_uuid}">client.tags.<a href="./src/lilypad/resources/tags.py">retrieve</a>(tag_uuid) -> <a href="./src/lilypad/types/tag_public.py">TagPublic</a></code>
- <code title="patch /tags/{tag_uuid}">client.tags.<a href="./src/lilypad/resources/tags.py">update</a>(tag_uuid, \*\*<a href="src/lilypad/types/tag_update_params.py">params</a>) -> <a href="./src/lilypad/types/tag_public.py">TagPublic</a></code>
- <code title="get /tags">client.tags.<a href="./src/lilypad/resources/tags.py">list</a>() -> <a href="./src/lilypad/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /tags/{tag_uuid}">client.tags.<a href="./src/lilypad/resources/tags.py">delete</a>(tag_uuid) -> <a href="./src/lilypad/types/tag_delete_response.py">TagDeleteResponse</a></code>

# Comments

Types:

```python
from lilypad.types import (
    CommentPublic,
    CommentListResponse,
    CommentDeleteResponse,
    CommentListCommentsBySpanResponse,
)
```

Methods:

- <code title="post /comments">client.comments.<a href="./src/lilypad/resources/comments.py">create</a>(\*\*<a href="src/lilypad/types/comment_create_params.py">params</a>) -> <a href="./src/lilypad/types/comment_public.py">CommentPublic</a></code>
- <code title="get /comments/{comment_uuid}">client.comments.<a href="./src/lilypad/resources/comments.py">retrieve</a>(comment_uuid) -> <a href="./src/lilypad/types/comment_public.py">CommentPublic</a></code>
- <code title="patch /comments/{comment_uuid}">client.comments.<a href="./src/lilypad/resources/comments.py">update</a>(comment_uuid, \*\*<a href="src/lilypad/types/comment_update_params.py">params</a>) -> <a href="./src/lilypad/types/comment_public.py">CommentPublic</a></code>
- <code title="get /comments">client.comments.<a href="./src/lilypad/resources/comments.py">list</a>() -> <a href="./src/lilypad/types/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /comments/{comment_uuid}">client.comments.<a href="./src/lilypad/resources/comments.py">delete</a>(comment_uuid) -> <a href="./src/lilypad/types/comment_delete_response.py">CommentDeleteResponse</a></code>
- <code title="get /spans/{span_uuid}/comments">client.comments.<a href="./src/lilypad/resources/comments.py">list_comments_by_span</a>(span_uuid) -> <a href="./src/lilypad/types/comment_list_comments_by_span_response.py">CommentListCommentsBySpanResponse</a></code>

# Settings

Types:

```python
from lilypad.types import SettingRetrieveResponse
```

Methods:

- <code title="get /settings">client.settings.<a href="./src/lilypad/resources/settings.py">retrieve</a>() -> <a href="./src/lilypad/types/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
