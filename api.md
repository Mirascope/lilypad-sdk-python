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
)
```

Methods:

- <code title="post /ee/projects/{project_uuid}/annotations">client.ee.projects.annotations.<a href="./src/lilypad/resources/ee/projects/annotations.py">create</a>(project_uuid, \*\*<a href="src/lilypad/types/ee/projects/annotation_create_params.py">params</a>) -> <a href="./src/lilypad/types/ee/projects/annotation_create_response.py">AnnotationCreateResponse</a></code>
- <code title="patch /ee/projects/{project_uuid}/annotations/{annotation_uuid}">client.ee.projects.annotations.<a href="./src/lilypad/resources/ee/projects/annotations.py">update</a>(annotation_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/ee/projects/annotation_update_params.py">params</a>) -> <a href="./src/lilypad/types/ee/projects/annotation_public.py">AnnotationPublic</a></code>

### Functions

Types:

```python
from lilypad.types.ee.projects import FunctionGetAnnotationsResponse, FunctionRunPlaygroundResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/functions/{function_uuid}/annotations">client.ee.projects.functions.<a href="./src/lilypad/resources/ee/projects/functions.py">get_annotations</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/function_get_annotations_response.py">FunctionGetAnnotationsResponse</a></code>
- <code title="post /ee/projects/{project_uuid}/functions/{function_uuid}/playground">client.ee.projects.functions.<a href="./src/lilypad/resources/ee/projects/functions.py">run_playground</a>(function_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/ee/projects/function_run_playground_params.py">params</a>) -> str</code>

### Spans

Types:

```python
from lilypad.types.ee.projects import SpanGenerateAnnotationResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/spans/{span_uuid}/generate-annotation">client.ee.projects.spans.<a href="./src/lilypad/resources/ee/projects/spans.py">generate_annotation</a>(span_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/span_generate_annotation_response.py">object</a></code>

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
    UserRole,
    UserOrganizationDeleteResponse,
    UserOrganizationGetUserOrganizationsResponse,
    UserOrganizationGetUsersResponse,
)
```

Methods:

- <code title="post /ee/user-organizations">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">create</a>(\*\*<a href="src/lilypad/types/ee/user_organization_create_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_organization_table.py">UserOrganizationTable</a></code>
- <code title="patch /ee/user-organizations/{user_organization_uuid}">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">update</a>(user_organization_uuid, \*\*<a href="src/lilypad/types/ee/user_organization_update_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_organization_table.py">UserOrganizationTable</a></code>
- <code title="delete /ee/user-organizations/{user_organization_uuid}">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">delete</a>(user_organization_uuid) -> <a href="./src/lilypad/types/ee/user_organization_delete_response.py">UserOrganizationDeleteResponse</a></code>
- <code title="get /ee/user-organizations">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">get_user_organizations</a>() -> <a href="./src/lilypad/types/ee/user_organization_get_user_organizations_response.py">UserOrganizationGetUserOrganizationsResponse</a></code>
- <code title="get /ee/user-organizations/users">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">get_users</a>() -> <a href="./src/lilypad/types/ee/user_organization_get_users_response.py">UserOrganizationGetUsersResponse</a></code>

# APIKeys

Types:

```python
from lilypad.types import APIKeyCreateResponse, APIKeyListResponse, APIKeyDeleteResponse
```

Methods:

- <code title="post /api-keys">client.api_keys.<a href="./src/lilypad/resources/api_keys.py">create</a>(\*\*<a href="src/lilypad/types/api_key_create_params.py">params</a>) -> str</code>
- <code title="get /api-keys">client.api_keys.<a href="./src/lilypad/resources/api_keys.py">list</a>() -> <a href="./src/lilypad/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api-keys/{api_key_uuid}">client.api_keys.<a href="./src/lilypad/resources/api_keys.py">delete</a>(api_key_uuid) -> <a href="./src/lilypad/types/api_key_delete_response.py">APIKeyDeleteResponse</a></code>

# Projects

Types:

```python
from lilypad.types import (
    FunctionCreate,
    ProjectCreate,
    ProjectPublic,
    ProjectListResponse,
    ProjectDeleteResponse,
)
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/lilypad/resources/projects/projects.py">create</a>(\*\*<a href="src/lilypad/types/project_create_params.py">params</a>) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">retrieve</a>(project_uuid) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="patch /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">update</a>(project_uuid, \*\*<a href="src/lilypad/types/project_update_params.py">params</a>) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects">client.projects.<a href="./src/lilypad/resources/projects/projects.py">list</a>() -> <a href="./src/lilypad/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">delete</a>(project_uuid) -> <a href="./src/lilypad/types/project_delete_response.py">ProjectDeleteResponse</a></code>
- <code title="post /projects/{project_uuid}/versioned-functions">client.projects.<a href="./src/lilypad/resources/projects/projects.py">create_versioned_function</a>(path_project_uuid, \*\*<a href="src/lilypad/types/project_create_versioned_function_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>

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
    NameRetrieveByNameResponse,
)
```

Methods:

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

### Spans

Types:

```python
from lilypad.types.projects.functions import (
    AggregateMetrics,
    SpanPublic,
    TimeFrame,
    SpanListResponse,
    SpanListAggregatesResponse,
)
```

Methods:

- <code title="get /projects/{project_uuid}/functions/{function_uuid}/spans">client.projects.functions.spans.<a href="./src/lilypad/resources/projects/functions/spans.py">list</a>(function_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/span_list_response.py">SpanListResponse</a></code>
- <code title="get /projects/{project_uuid}/functions/{function_uuid}/spans/metadata">client.projects.functions.spans.<a href="./src/lilypad/resources/projects/functions/spans.py">list_aggregates</a>(function_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/projects/functions/span_list_aggregates_params.py">params</a>) -> <a href="./src/lilypad/types/projects/functions/span_list_aggregates_response.py">SpanListAggregatesResponse</a></code>

## Spans

Types:

```python
from lilypad.types.projects import SpanListAggregatesResponse
```

Methods:

- <code title="get /projects/{project_uuid}/spans/metadata">client.projects.spans.<a href="./src/lilypad/resources/projects/spans.py">list_aggregates</a>(project_uuid, \*\*<a href="src/lilypad/types/projects/span_list_aggregates_params.py">params</a>) -> <a href="./src/lilypad/types/projects/span_list_aggregates_response.py">SpanListAggregatesResponse</a></code>

## Traces

Types:

```python
from lilypad.types.projects import TraceCreateResponse, TraceListResponse
```

Methods:

- <code title="post /projects/{project_uuid}/traces">client.projects.traces.<a href="./src/lilypad/resources/projects/traces.py">create</a>(project_uuid) -> <a href="./src/lilypad/types/projects/trace_create_response.py">TraceCreateResponse</a></code>
- <code title="get /projects/{project_uuid}/traces">client.projects.traces.<a href="./src/lilypad/resources/projects/traces.py">list</a>(project_uuid) -> <a href="./src/lilypad/types/projects/trace_list_response.py">TraceListResponse</a></code>

## Environments

Types:

```python
from lilypad.types.projects import DeploymentPublic, EnvironmentRetrieveDeploymentHistoryResponse
```

Methods:

- <code title="post /projects/{project_uuid}/environments/{environment_uuid}/deploy">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">deploy</a>(environment_uuid, \*, project_uuid, \*\*<a href="src/lilypad/types/projects/environment_deploy_params.py">params</a>) -> <a href="./src/lilypad/types/projects/deployment_public.py">DeploymentPublic</a></code>
- <code title="get /projects/{project_uuid}/environments/{environment_uuid}/deployment">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">retrieve_active_deployment</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/deployment_public.py">DeploymentPublic</a></code>
- <code title="get /projects/{project_uuid}/environments/{environment_uuid}/function">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">retrieve_active_function</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/functions/function_public.py">FunctionPublic</a></code>
- <code title="get /projects/{project_uuid}/environments/{environment_uuid}/history">client.projects.environments.<a href="./src/lilypad/resources/projects/environments.py">retrieve_deployment_history</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/projects/environment_retrieve_deployment_history_response.py">EnvironmentRetrieveDeploymentHistoryResponse</a></code>

# OrganizationsInvites

Types:

```python
from lilypad.types import OrganizationInvite
```

Methods:

- <code title="post /organizations-invites">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">create</a>(\*\*<a href="src/lilypad/types/organizations_invite_create_params.py">params</a>) -> <a href="./src/lilypad/types/organization_invite.py">OrganizationInvite</a></code>
- <code title="get /organizations-invites/{invite_token}">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">retrieve</a>(invite_token) -> <a href="./src/lilypad/types/organization_invite.py">OrganizationInvite</a></code>

# Spans

Types:

```python
from lilypad.types import SpanMoreDetails
```

Methods:

- <code title="get /spans/{span_uuid}">client.spans.<a href="./src/lilypad/resources/spans.py">retrieve</a>(span_uuid) -> <a href="./src/lilypad/types/span_more_details.py">SpanMoreDetails</a></code>

# Auth

## GitHub

Types:

```python
from lilypad.types.auth import UserPublic
```

Methods:

- <code title="get /auth/github/callback">client.auth.github.<a href="./src/lilypad/resources/auth/github.py">callback</a>(\*\*<a href="src/lilypad/types/auth/github_callback_params.py">params</a>) -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>

## Google

Methods:

- <code title="get /auth/google/callback">client.auth.google.<a href="./src/lilypad/resources/auth/google.py">callback</a>(\*\*<a href="src/lilypad/types/auth/google_callback_params.py">params</a>) -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>

# Users

Methods:

- <code title="put /users/{activeOrganizationUuid}">client.users.<a href="./src/lilypad/resources/users.py">update_active_organization</a>(active_organization_uuid) -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>
- <code title="patch /users">client.users.<a href="./src/lilypad/resources/users.py">update_keys</a>(\*\*<a href="src/lilypad/types/user_update_keys_params.py">params</a>) -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>

# CurrentUser

Methods:

- <code title="get /current-user">client.current_user.<a href="./src/lilypad/resources/current_user.py">retrieve</a>() -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>

# Organizations

Types:

```python
from lilypad.types import OrganizationPublic
```

Methods:

- <code title="patch /organizations">client.organizations.<a href="./src/lilypad/resources/organizations.py">update</a>(\*\*<a href="src/lilypad/types/organization_update_params.py">params</a>) -> <a href="./src/lilypad/types/organization_public.py">OrganizationPublic</a></code>

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

# Settings

Types:

```python
from lilypad.types import SettingRetrieveResponse
```

Methods:

- <code title="get /settings">client.settings.<a href="./src/lilypad/resources/settings.py">retrieve</a>() -> <a href="./src/lilypad/types/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
