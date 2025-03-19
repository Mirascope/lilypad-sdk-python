# Ee

## Projects

Types:

```python
from lilypad_sdk.types.ee import GenerationCreate
```

Methods:

- <code title="post /ee/projects/{project_uuid}/managed-generations">client.ee.projects.<a href="./src/lilypad_sdk/resources/ee/projects/projects.py">create_managed_generation</a>(project_uuid_1, \*\*<a href="src/lilypad_sdk/types/ee/project_create_managed_generation_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>

### Annotations

Types:

```python
from lilypad_sdk.types.ee.projects import (
    AnnotationPublic,
    EvaluationType,
    Label,
    AnnotationCreateResponse,
)
```

Methods:

- <code title="post /ee/projects/{project_uuid}/annotations">client.ee.projects.annotations.<a href="./src/lilypad_sdk/resources/ee/projects/annotations.py">create</a>(project_uuid, \*\*<a href="src/lilypad_sdk/types/ee/projects/annotation_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/annotation_create_response.py">AnnotationCreateResponse</a></code>
- <code title="patch /ee/projects/{project_uuid}/annotations/{annotation_uuid}">client.ee.projects.annotations.<a href="./src/lilypad_sdk/resources/ee/projects/annotations.py">update</a>(annotation_uuid, \*, project_uuid, \*\*<a href="src/lilypad_sdk/types/ee/projects/annotation_update_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/annotation_public.py">AnnotationPublic</a></code>

### Generations

Types:

```python
from lilypad_sdk.types.ee.projects import (
    GenerationGetAnnotationsResponse,
    GenerationRunVersionResponse,
)
```

Methods:

- <code title="get /ee/projects/{project_uuid}/generations/{generation_uuid}/annotations">client.ee.projects.generations.<a href="./src/lilypad_sdk/resources/ee/projects/generations/generations.py">get_annotations</a>(generation_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_get_annotations_response.py">GenerationGetAnnotationsResponse</a></code>
- <code title="post /ee/projects/{project_uuid}/generations/{generation_uuid}/run">client.ee.projects.generations.<a href="./src/lilypad_sdk/resources/ee/projects/generations/generations.py">run_version</a>(generation_uuid, \*, project_uuid, \*\*<a href="src/lilypad_sdk/types/ee/projects/generation_run_version_params.py">params</a>) -> str</code>

#### Name

Types:

```python
from lilypad_sdk.types.ee.projects.generations import NameGetByNameResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/generations/name/{generation_name}">client.ee.projects.generations.name.<a href="./src/lilypad_sdk/resources/ee/projects/generations/name.py">get_by_name</a>(generation_name, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/generations/name_get_by_name_response.py">NameGetByNameResponse</a></code>
- <code title="get /ee/projects/{project_uuid}/generations/name/{generation_name}/version/{version_num}">client.ee.projects.generations.name.<a href="./src/lilypad_sdk/resources/ee/projects/generations/name.py">get_by_version</a>(version_num, \*, project_uuid, generation_name) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>
- <code title="get /ee/projects/{project_uuid}/generations/name/{generation_name}/environments">client.ee.projects.generations.name.<a href="./src/lilypad_sdk/resources/ee/projects/generations/name.py">get_deployed_by_name</a>(generation_name, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>

### Spans

Types:

```python
from lilypad_sdk.types.ee.projects import SpanGenerateAnnotationResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/spans/{span_uuid}/generate-annotation">client.ee.projects.spans.<a href="./src/lilypad_sdk/resources/ee/projects/spans.py">generate_annotation</a>(span_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/span_generate_annotation_response.py">object</a></code>

### Environments

Types:

```python
from lilypad_sdk.types.ee.projects import (
    CommonCallParams,
    DeploymentPublic,
    EnvironmentPublic,
    GenerationPublic,
    EnvironmentListResponse,
    EnvironmentDeleteResponse,
    EnvironmentGetDeploymentHistoryResponse,
)
```

Methods:

- <code title="post /ee/projects/{project_uuid}/environments">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">create</a>(project_uuid_1, \*\*<a href="src/lilypad_sdk/types/ee/projects/environment_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/environment_public.py">EnvironmentPublic</a></code>
- <code title="get /ee/projects/{project_uuid}/environments/{environment_uuid}">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">retrieve</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/environment_public.py">EnvironmentPublic</a></code>
- <code title="get /ee/projects/{project_uuid}/environments">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">list</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/environment_list_response.py">EnvironmentListResponse</a></code>
- <code title="delete /ee/projects/{project_uuid}/environments/{environment_uuid}">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">delete</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/environment_delete_response.py">EnvironmentDeleteResponse</a></code>
- <code title="post /ee/projects/{project_uuid}/environments/{environment_uuid}/deploy">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">deploy_generation</a>(environment_uuid, \*, project_uuid, \*\*<a href="src/lilypad_sdk/types/ee/projects/environment_deploy_generation_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/deployment_public.py">DeploymentPublic</a></code>
- <code title="get /ee/projects/{project_uuid}/environments/{environment_uuid}/deployment">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">get_active_deployment</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/deployment_public.py">DeploymentPublic</a></code>
- <code title="get /ee/projects/{project_uuid}/environments/{environment_uuid}/history">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">get_deployment_history</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/environment_get_deployment_history_response.py">EnvironmentGetDeploymentHistoryResponse</a></code>
- <code title="get /ee/projects/{project_uuid}/environments/{environment_uuid}/generation">client.ee.projects.environments.<a href="./src/lilypad_sdk/resources/ee/projects/environments.py">get_environment_generation</a>(environment_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>

## Organizations

Types:

```python
from lilypad_sdk.types.ee import OrganizationGetLicenseResponse
```

Methods:

- <code title="get /ee/organizations/license">client.ee.organizations.<a href="./src/lilypad_sdk/resources/ee/organizations.py">get_license</a>() -> <a href="./src/lilypad_sdk/types/ee/organization_get_license_response.py">OrganizationGetLicenseResponse</a></code>

# APIKeys

Types:

```python
from lilypad_sdk.types import APIKeyCreateResponse, APIKeyListResponse, APIKeyDeleteResponse
```

Methods:

- <code title="post /api-keys">client.api_keys.<a href="./src/lilypad_sdk/resources/api_keys.py">create</a>(\*\*<a href="src/lilypad_sdk/types/api_key_create_params.py">params</a>) -> str</code>
- <code title="get /api-keys">client.api_keys.<a href="./src/lilypad_sdk/resources/api_keys.py">list</a>() -> <a href="./src/lilypad_sdk/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api-keys/{api_key_uuid}">client.api_keys.<a href="./src/lilypad_sdk/resources/api_keys.py">delete</a>(api_key_uuid) -> <a href="./src/lilypad_sdk/types/api_key_delete_response.py">APIKeyDeleteResponse</a></code>

# Projects

Types:

```python
from lilypad_sdk.types import (
    ProjectCreate,
    ProjectPublic,
    ProjectListResponse,
    ProjectDeleteResponse,
)
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/lilypad_sdk/resources/projects/projects.py">create</a>(\*\*<a href="src/lilypad_sdk/types/project_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects/{project_uuid}">client.projects.<a href="./src/lilypad_sdk/resources/projects/projects.py">retrieve</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/project_public.py">ProjectPublic</a></code>
- <code title="patch /projects/{project_uuid}">client.projects.<a href="./src/lilypad_sdk/resources/projects/projects.py">update</a>(project_uuid, \*\*<a href="src/lilypad_sdk/types/project_update_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects">client.projects.<a href="./src/lilypad_sdk/resources/projects/projects.py">list</a>() -> <a href="./src/lilypad_sdk/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /projects/{project_uuid}">client.projects.<a href="./src/lilypad_sdk/resources/projects/projects.py">delete</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/project_delete_response.py">ProjectDeleteResponse</a></code>

## Generations

Types:

```python
from lilypad_sdk.types.projects import (
    GenerationListResponse,
    GenerationArchiveResponse,
    GenerationArchiveByNameResponse,
)
```

Methods:

- <code title="post /projects/{project_uuid}/generations">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">create</a>(project_uuid_1, \*\*<a href="src/lilypad_sdk/types/projects/generation_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>
- <code title="get /projects/{project_uuid}/generations/{generation_uuid}">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">retrieve</a>(generation_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>
- <code title="patch /projects/{project_uuid}/generations/{generation_uuid}">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">update</a>(generation_uuid, \*, project_uuid, \*\*<a href="src/lilypad_sdk/types/projects/generation_update_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>
- <code title="get /projects/{project_uuid}/generations">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">list</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/projects/generation_list_response.py">GenerationListResponse</a></code>
- <code title="delete /projects/{project_uuid}/generations/{generation_uuid}">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">archive</a>(generation_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/projects/generation_archive_response.py">GenerationArchiveResponse</a></code>
- <code title="delete /projects/{project_uuid}/generations/names/{generation_name}">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">archive_by_name</a>(generation_name, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/projects/generation_archive_by_name_response.py">GenerationArchiveByNameResponse</a></code>
- <code title="get /projects/{project_uuid}/generations/hash/{generation_hash}">client.projects.generations.<a href="./src/lilypad_sdk/resources/projects/generations/generations.py">retrieve_by_hash</a>(generation_hash, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/ee/projects/generation_public.py">GenerationPublic</a></code>

### Metadata

#### Names

Types:

```python
from lilypad_sdk.types.projects.generations.metadata import (
    NameListResponse,
    NameListLatestVersionsResponse,
)
```

Methods:

- <code title="get /projects/{project_uuid}/generations/metadata/names">client.projects.generations.metadata.names.<a href="./src/lilypad_sdk/resources/projects/generations/metadata/names.py">list</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/projects/generations/metadata/name_list_response.py">NameListResponse</a></code>
- <code title="get /projects/{project_uuid}/generations/metadata/names/versions">client.projects.generations.metadata.names.<a href="./src/lilypad_sdk/resources/projects/generations/metadata/names.py">list_latest_versions</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/projects/generations/metadata/name_list_latest_versions_response.py">NameListLatestVersionsResponse</a></code>

### Spans

Types:

```python
from lilypad_sdk.types.projects.generations import (
    AggregateMetrics,
    SpanPublic,
    TimeFrame,
    SpanListResponse,
    SpanGetAggregatesResponse,
)
```

Methods:

- <code title="get /projects/{project_uuid}/generations/{generation_uuid}/spans">client.projects.generations.spans.<a href="./src/lilypad_sdk/resources/projects/generations/spans.py">list</a>(generation_uuid, \*, project_uuid) -> <a href="./src/lilypad_sdk/types/projects/generations/span_list_response.py">SpanListResponse</a></code>
- <code title="get /projects/{project_uuid}/generations/{generation_uuid}/spans/metadata">client.projects.generations.spans.<a href="./src/lilypad_sdk/resources/projects/generations/spans.py">get_aggregates</a>(generation_uuid, \*, project_uuid, \*\*<a href="src/lilypad_sdk/types/projects/generations/span_get_aggregates_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/projects/generations/span_get_aggregates_response.py">SpanGetAggregatesResponse</a></code>

## Spans

Types:

```python
from lilypad_sdk.types.projects import SpanGetAggregatesResponse
```

Methods:

- <code title="get /projects/{project_uuid}/spans/metadata">client.projects.spans.<a href="./src/lilypad_sdk/resources/projects/spans.py">get_aggregates</a>(project_uuid, \*\*<a href="src/lilypad_sdk/types/projects/span_get_aggregates_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/projects/span_get_aggregates_response.py">SpanGetAggregatesResponse</a></code>

## Traces

Types:

```python
from lilypad_sdk.types.projects import TraceCreateResponse, TraceListResponse
```

Methods:

- <code title="post /projects/{project_uuid}/traces">client.projects.traces.<a href="./src/lilypad_sdk/resources/projects/traces.py">create</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/projects/trace_create_response.py">TraceCreateResponse</a></code>
- <code title="get /projects/{project_uuid}/traces">client.projects.traces.<a href="./src/lilypad_sdk/resources/projects/traces.py">list</a>(project_uuid) -> <a href="./src/lilypad_sdk/types/projects/trace_list_response.py">TraceListResponse</a></code>

# Spans

Types:

```python
from lilypad_sdk.types import SpanMoreDetails
```

Methods:

- <code title="get /spans/{span_uuid}">client.spans.<a href="./src/lilypad_sdk/resources/spans.py">retrieve</a>(span_uuid) -> <a href="./src/lilypad_sdk/types/span_more_details.py">SpanMoreDetails</a></code>

# Auth

## GitHub

Types:

```python
from lilypad_sdk.types.auth import UserPublic
```

Methods:

- <code title="get /auth/github/callback">client.auth.github.<a href="./src/lilypad_sdk/resources/auth/github.py">handle_callback</a>(\*\*<a href="src/lilypad_sdk/types/auth/github_handle_callback_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/auth/user_public.py">UserPublic</a></code>

## Google

Methods:

- <code title="get /auth/google/callback">client.auth.google.<a href="./src/lilypad_sdk/resources/auth/google.py">handle_callback</a>(\*\*<a href="src/lilypad_sdk/types/auth/google_handle_callback_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/auth/user_public.py">UserPublic</a></code>

# UserOrganizations

Types:

```python
from lilypad_sdk.types import (
    UserOrganization,
    UserRole,
    UserOrganizationListResponse,
    UserOrganizationDeleteResponse,
    UserOrganizationGetUsersResponse,
)
```

Methods:

- <code title="post /user-organizations">client.user_organizations.<a href="./src/lilypad_sdk/resources/user_organizations.py">create</a>(\*\*<a href="src/lilypad_sdk/types/user_organization_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/user_organization.py">UserOrganization</a></code>
- <code title="patch /user-organizations/{user_organization_uuid}">client.user_organizations.<a href="./src/lilypad_sdk/resources/user_organizations.py">update</a>(user_organization_uuid, \*\*<a href="src/lilypad_sdk/types/user_organization_update_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/user_organization.py">UserOrganization</a></code>
- <code title="get /user-organizations">client.user_organizations.<a href="./src/lilypad_sdk/resources/user_organizations.py">list</a>() -> <a href="./src/lilypad_sdk/types/user_organization_list_response.py">UserOrganizationListResponse</a></code>
- <code title="delete /user-organizations/{user_organization_uuid}">client.user_organizations.<a href="./src/lilypad_sdk/resources/user_organizations.py">delete</a>(user_organization_uuid) -> <a href="./src/lilypad_sdk/types/user_organization_delete_response.py">UserOrganizationDeleteResponse</a></code>
- <code title="get /user-organizations/users">client.user_organizations.<a href="./src/lilypad_sdk/resources/user_organizations.py">get_users</a>() -> <a href="./src/lilypad_sdk/types/user_organization_get_users_response.py">UserOrganizationGetUsersResponse</a></code>

# Users

Methods:

- <code title="put /users/{activeOrganizationUuid}">client.users.<a href="./src/lilypad_sdk/resources/users.py">update_active_organization</a>(active_organization_uuid) -> <a href="./src/lilypad_sdk/types/auth/user_public.py">UserPublic</a></code>
- <code title="patch /users">client.users.<a href="./src/lilypad_sdk/resources/users.py">update_keys</a>(\*\*<a href="src/lilypad_sdk/types/user_update_keys_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/auth/user_public.py">UserPublic</a></code>

# CurrentUser

Methods:

- <code title="get /current-user">client.current_user.<a href="./src/lilypad_sdk/resources/current_user.py">retrieve</a>() -> <a href="./src/lilypad_sdk/types/auth/user_public.py">UserPublic</a></code>

# Organizations

Types:

```python
from lilypad_sdk.types import Organization
```

Methods:

- <code title="patch /organizations">client.organizations.<a href="./src/lilypad_sdk/resources/organizations/organizations.py">update</a>(\*\*<a href="src/lilypad_sdk/types/organization_update_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/organization.py">Organization</a></code>

## Invites

Types:

```python
from lilypad_sdk.types.organizations import OrganizationInvite
```

Methods:

- <code title="post /organizations/invites">client.organizations.invites.<a href="./src/lilypad_sdk/resources/organizations/invites.py">create</a>(\*\*<a href="src/lilypad_sdk/types/organizations/invite_create_params.py">params</a>) -> <a href="./src/lilypad_sdk/types/organizations/organization_invite.py">OrganizationInvite</a></code>
- <code title="get /organizations/invites/{invite_token}">client.organizations.invites.<a href="./src/lilypad_sdk/resources/organizations/invites.py">retrieve</a>(invite_token) -> <a href="./src/lilypad_sdk/types/organizations/organization_invite.py">OrganizationInvite</a></code>

# Settings

Types:

```python
from lilypad_sdk.types import SettingRetrieveResponse
```

Methods:

- <code title="get /settings">client.settings.<a href="./src/lilypad_sdk/resources/settings.py">retrieve</a>() -> <a href="./src/lilypad_sdk/types/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
