# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    spans,
    users,
    api_keys,
    settings,
    current_user,
    environments,
    organizations,
    external_api_keys,
    organizations_invites,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LilypadError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.ee import ee
from .resources.auth import auth
from .resources.projects import projects

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Lilypad", "AsyncLilypad", "Client", "AsyncClient"]


class Lilypad(SyncAPIClient):
    ee: ee.EeResource
    api_keys: api_keys.APIKeysResource
    projects: projects.ProjectsResource
    organizations_invites: organizations_invites.OrganizationsInvitesResource
    spans: spans.SpansResource
    auth: auth.AuthResource
    users: users.UsersResource
    current_user: current_user.CurrentUserResource
    organizations: organizations.OrganizationsResource
    external_api_keys: external_api_keys.ExternalAPIKeysResource
    environments: environments.EnvironmentsResource
    settings: settings.SettingsResource
    with_raw_response: LilypadWithRawResponse
    with_streaming_response: LilypadWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Lilypad client instance.

        This automatically infers the `api_key` argument from the `LILYPAD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LILYPAD_API_KEY")
        if api_key is None:
            raise LilypadError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LILYPAD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LILYPAD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.mirascope.com/lilypad/v0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.ee = ee.EeResource(self)
        self.api_keys = api_keys.APIKeysResource(self)
        self.projects = projects.ProjectsResource(self)
        self.organizations_invites = organizations_invites.OrganizationsInvitesResource(self)
        self.spans = spans.SpansResource(self)
        self.auth = auth.AuthResource(self)
        self.users = users.UsersResource(self)
        self.current_user = current_user.CurrentUserResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.external_api_keys = external_api_keys.ExternalAPIKeysResource(self)
        self.environments = environments.EnvironmentsResource(self)
        self.settings = settings.SettingsResource(self)
        self.with_raw_response = LilypadWithRawResponse(self)
        self.with_streaming_response = LilypadWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLilypad(AsyncAPIClient):
    ee: ee.AsyncEeResource
    api_keys: api_keys.AsyncAPIKeysResource
    projects: projects.AsyncProjectsResource
    organizations_invites: organizations_invites.AsyncOrganizationsInvitesResource
    spans: spans.AsyncSpansResource
    auth: auth.AsyncAuthResource
    users: users.AsyncUsersResource
    current_user: current_user.AsyncCurrentUserResource
    organizations: organizations.AsyncOrganizationsResource
    external_api_keys: external_api_keys.AsyncExternalAPIKeysResource
    environments: environments.AsyncEnvironmentsResource
    settings: settings.AsyncSettingsResource
    with_raw_response: AsyncLilypadWithRawResponse
    with_streaming_response: AsyncLilypadWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLilypad client instance.

        This automatically infers the `api_key` argument from the `LILYPAD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LILYPAD_API_KEY")
        if api_key is None:
            raise LilypadError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LILYPAD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LILYPAD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.mirascope.com/lilypad/v0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.ee = ee.AsyncEeResource(self)
        self.api_keys = api_keys.AsyncAPIKeysResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.organizations_invites = organizations_invites.AsyncOrganizationsInvitesResource(self)
        self.spans = spans.AsyncSpansResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.users = users.AsyncUsersResource(self)
        self.current_user = current_user.AsyncCurrentUserResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.external_api_keys = external_api_keys.AsyncExternalAPIKeysResource(self)
        self.environments = environments.AsyncEnvironmentsResource(self)
        self.settings = settings.AsyncSettingsResource(self)
        self.with_raw_response = AsyncLilypadWithRawResponse(self)
        self.with_streaming_response = AsyncLilypadWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LilypadWithRawResponse:
    def __init__(self, client: Lilypad) -> None:
        self.ee = ee.EeResourceWithRawResponse(client.ee)
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.organizations_invites = organizations_invites.OrganizationsInvitesResourceWithRawResponse(
            client.organizations_invites
        )
        self.spans = spans.SpansResourceWithRawResponse(client.spans)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.current_user = current_user.CurrentUserResourceWithRawResponse(client.current_user)
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.external_api_keys = external_api_keys.ExternalAPIKeysResourceWithRawResponse(client.external_api_keys)
        self.environments = environments.EnvironmentsResourceWithRawResponse(client.environments)
        self.settings = settings.SettingsResourceWithRawResponse(client.settings)


class AsyncLilypadWithRawResponse:
    def __init__(self, client: AsyncLilypad) -> None:
        self.ee = ee.AsyncEeResourceWithRawResponse(client.ee)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.organizations_invites = organizations_invites.AsyncOrganizationsInvitesResourceWithRawResponse(
            client.organizations_invites
        )
        self.spans = spans.AsyncSpansResourceWithRawResponse(client.spans)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.current_user = current_user.AsyncCurrentUserResourceWithRawResponse(client.current_user)
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.external_api_keys = external_api_keys.AsyncExternalAPIKeysResourceWithRawResponse(client.external_api_keys)
        self.environments = environments.AsyncEnvironmentsResourceWithRawResponse(client.environments)
        self.settings = settings.AsyncSettingsResourceWithRawResponse(client.settings)


class LilypadWithStreamedResponse:
    def __init__(self, client: Lilypad) -> None:
        self.ee = ee.EeResourceWithStreamingResponse(client.ee)
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.organizations_invites = organizations_invites.OrganizationsInvitesResourceWithStreamingResponse(
            client.organizations_invites
        )
        self.spans = spans.SpansResourceWithStreamingResponse(client.spans)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.current_user = current_user.CurrentUserResourceWithStreamingResponse(client.current_user)
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.external_api_keys = external_api_keys.ExternalAPIKeysResourceWithStreamingResponse(
            client.external_api_keys
        )
        self.environments = environments.EnvironmentsResourceWithStreamingResponse(client.environments)
        self.settings = settings.SettingsResourceWithStreamingResponse(client.settings)


class AsyncLilypadWithStreamedResponse:
    def __init__(self, client: AsyncLilypad) -> None:
        self.ee = ee.AsyncEeResourceWithStreamingResponse(client.ee)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.organizations_invites = organizations_invites.AsyncOrganizationsInvitesResourceWithStreamingResponse(
            client.organizations_invites
        )
        self.spans = spans.AsyncSpansResourceWithStreamingResponse(client.spans)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.current_user = current_user.AsyncCurrentUserResourceWithStreamingResponse(client.current_user)
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.external_api_keys = external_api_keys.AsyncExternalAPIKeysResourceWithStreamingResponse(
            client.external_api_keys
        )
        self.environments = environments.AsyncEnvironmentsResourceWithStreamingResponse(client.environments)
        self.settings = settings.AsyncSettingsResourceWithStreamingResponse(client.settings)


Client = Lilypad

AsyncClient = AsyncLilypad
