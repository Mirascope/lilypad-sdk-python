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

### Spans

Types:

```python
from lilypad.types.ee.projects import SpanGenerateAnnotationResponse
```

Methods:

- <code title="get /ee/projects/{project_uuid}/spans/{span_uuid}/generate-annotation">client.ee.projects.spans.<a href="./src/lilypad/resources/ee/projects/spans.py">generate_annotation</a>(span_uuid, \*, project_uuid) -> <a href="./src/lilypad/types/ee/projects/span_generate_annotation_response.py">object</a></code>

### Environments

Types:

```python
from lilypad.types.ee.projects import CommonCallParams, DeploymentPublic, EnvironmentPublic
```

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
    UserOrganizationListResponse,
    UserOrganizationDeleteResponse,
    UserOrganizationGetUsersResponse,
)
```

Methods:

- <code title="post /ee/user-organizations">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">create</a>(\*\*<a href="src/lilypad/types/ee/user_organization_create_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_organization_table.py">UserOrganizationTable</a></code>
- <code title="patch /ee/user-organizations/{user_organization_uuid}">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">update</a>(user_organization_uuid, \*\*<a href="src/lilypad/types/ee/user_organization_update_params.py">params</a>) -> <a href="./src/lilypad/types/ee/user_organization_table.py">UserOrganizationTable</a></code>
- <code title="get /ee/user-organizations">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">list</a>() -> <a href="./src/lilypad/types/ee/user_organization_list_response.py">UserOrganizationListResponse</a></code>
- <code title="delete /ee/user-organizations/{user_organization_uuid}">client.ee.user_organizations.<a href="./src/lilypad/resources/ee/user_organizations.py">delete</a>(user_organization_uuid) -> <a href="./src/lilypad/types/ee/user_organization_delete_response.py">UserOrganizationDeleteResponse</a></code>
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
from lilypad.types import ProjectCreate, ProjectPublic, ProjectListResponse, ProjectDeleteResponse
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/lilypad/resources/projects/projects.py">create</a>(\*\*<a href="src/lilypad/types/project_create_params.py">params</a>) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">retrieve</a>(project_uuid) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="patch /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">update</a>(project_uuid, \*\*<a href="src/lilypad/types/project_update_params.py">params</a>) -> <a href="./src/lilypad/types/project_public.py">ProjectPublic</a></code>
- <code title="get /projects">client.projects.<a href="./src/lilypad/resources/projects/projects.py">list</a>() -> <a href="./src/lilypad/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /projects/{project_uuid}">client.projects.<a href="./src/lilypad/resources/projects/projects.py">delete</a>(project_uuid) -> <a href="./src/lilypad/types/project_delete_response.py">ProjectDeleteResponse</a></code>

## Generations

### Spans

Types:

```python
from lilypad.types.projects.generations import AggregateMetrics, SpanPublic, TimeFrame
```

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

# OrganizationsInvites

Types:

```python
from lilypad.types import OrganizationInvitePublic
```

Methods:

- <code title="post /organizations-invites">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">create</a>(\*\*<a href="src/lilypad/types/organizations_invite_create_params.py">params</a>) -> <a href="./src/lilypad/types/organization_invite_public.py">OrganizationInvitePublic</a></code>
- <code title="get /organizations-invites/{invite_token}">client.organizations_invites.<a href="./src/lilypad/resources/organizations_invites.py">retrieve</a>(invite_token) -> <a href="./src/lilypad/types/organization_invite_public.py">OrganizationInvitePublic</a></code>

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

- <code title="get /auth/github/callback">client.auth.github.<a href="./src/lilypad/resources/auth/github.py">handle_callback</a>(\*\*<a href="src/lilypad/types/auth/github_handle_callback_params.py">params</a>) -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>

## Google

Methods:

- <code title="get /auth/google/callback">client.auth.google.<a href="./src/lilypad/resources/auth/google.py">handle_callback</a>(\*\*<a href="src/lilypad/types/auth/google_handle_callback_params.py">params</a>) -> <a href="./src/lilypad/types/auth/user_public.py">UserPublic</a></code>

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

# Settings

Types:

```python
from lilypad.types import SettingRetrieveResponse
```

Methods:

- <code title="get /settings">client.settings.<a href="./src/lilypad/resources/settings.py">retrieve</a>() -> <a href="./src/lilypad/types/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
