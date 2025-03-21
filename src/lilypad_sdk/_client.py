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
from .resources import spans, users, api_keys, settings, current_user, user_organizations
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LilypadSDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.ee import ee
from .resources.auth import auth
from .resources.projects import projects
from .resources.organizations import organizations

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LilypadSDK",
    "AsyncLilypadSDK",
    "Client",
    "AsyncClient",
]


class LilypadSDK(SyncAPIClient):
    ee: ee.EeResource
    api_keys: api_keys.APIKeysResource
    projects: projects.ProjectsResource
    spans: spans.SpansResource
    auth: auth.AuthResource
    user_organizations: user_organizations.UserOrganizationsResource
    users: users.UsersResource
    current_user: current_user.CurrentUserResource
    organizations: organizations.OrganizationsResource
    settings: settings.SettingsResource
    with_raw_response: LilypadSDKWithRawResponse
    with_streaming_response: LilypadSDKWithStreamedResponse

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
        """Construct a new synchronous LilypadSDK client instance.

        This automatically infers the `api_key` argument from the `LILYPAD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LILYPAD_API_KEY")
        if api_key is None:
            raise LilypadSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LILYPAD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LILYPAD_SDK_BASE_URL")
        if base_url is None:
            base_url = f"/v0"

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
        self.spans = spans.SpansResource(self)
        self.auth = auth.AuthResource(self)
        self.user_organizations = user_organizations.UserOrganizationsResource(self)
        self.users = users.UsersResource(self)
        self.current_user = current_user.CurrentUserResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.settings = settings.SettingsResource(self)
        self.with_raw_response = LilypadSDKWithRawResponse(self)
        self.with_streaming_response = LilypadSDKWithStreamedResponse(self)

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


class AsyncLilypadSDK(AsyncAPIClient):
    ee: ee.AsyncEeResource
    api_keys: api_keys.AsyncAPIKeysResource
    projects: projects.AsyncProjectsResource
    spans: spans.AsyncSpansResource
    auth: auth.AsyncAuthResource
    user_organizations: user_organizations.AsyncUserOrganizationsResource
    users: users.AsyncUsersResource
    current_user: current_user.AsyncCurrentUserResource
    organizations: organizations.AsyncOrganizationsResource
    settings: settings.AsyncSettingsResource
    with_raw_response: AsyncLilypadSDKWithRawResponse
    with_streaming_response: AsyncLilypadSDKWithStreamedResponse

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
        """Construct a new async AsyncLilypadSDK client instance.

        This automatically infers the `api_key` argument from the `LILYPAD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LILYPAD_API_KEY")
        if api_key is None:
            raise LilypadSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LILYPAD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LILYPAD_SDK_BASE_URL")
        if base_url is None:
            base_url = f"/v0"

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
        self.spans = spans.AsyncSpansResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.user_organizations = user_organizations.AsyncUserOrganizationsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.current_user = current_user.AsyncCurrentUserResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.settings = settings.AsyncSettingsResource(self)
        self.with_raw_response = AsyncLilypadSDKWithRawResponse(self)
        self.with_streaming_response = AsyncLilypadSDKWithStreamedResponse(self)

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


class LilypadSDKWithRawResponse:
    def __init__(self, client: LilypadSDK) -> None:
        self.ee = ee.EeResourceWithRawResponse(client.ee)
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.spans = spans.SpansResourceWithRawResponse(client.spans)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.user_organizations = user_organizations.UserOrganizationsResourceWithRawResponse(client.user_organizations)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.current_user = current_user.CurrentUserResourceWithRawResponse(client.current_user)
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.settings = settings.SettingsResourceWithRawResponse(client.settings)


class AsyncLilypadSDKWithRawResponse:
    def __init__(self, client: AsyncLilypadSDK) -> None:
        self.ee = ee.AsyncEeResourceWithRawResponse(client.ee)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.spans = spans.AsyncSpansResourceWithRawResponse(client.spans)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.user_organizations = user_organizations.AsyncUserOrganizationsResourceWithRawResponse(
            client.user_organizations
        )
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.current_user = current_user.AsyncCurrentUserResourceWithRawResponse(client.current_user)
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.settings = settings.AsyncSettingsResourceWithRawResponse(client.settings)


class LilypadSDKWithStreamedResponse:
    def __init__(self, client: LilypadSDK) -> None:
        self.ee = ee.EeResourceWithStreamingResponse(client.ee)
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.spans = spans.SpansResourceWithStreamingResponse(client.spans)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.user_organizations = user_organizations.UserOrganizationsResourceWithStreamingResponse(
            client.user_organizations
        )
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.current_user = current_user.CurrentUserResourceWithStreamingResponse(client.current_user)
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.settings = settings.SettingsResourceWithStreamingResponse(client.settings)


class AsyncLilypadSDKWithStreamedResponse:
    def __init__(self, client: AsyncLilypadSDK) -> None:
        self.ee = ee.AsyncEeResourceWithStreamingResponse(client.ee)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.spans = spans.AsyncSpansResourceWithStreamingResponse(client.spans)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.user_organizations = user_organizations.AsyncUserOrganizationsResourceWithStreamingResponse(
            client.user_organizations
        )
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.current_user = current_user.AsyncCurrentUserResourceWithStreamingResponse(client.current_user)
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.settings = settings.AsyncSettingsResourceWithStreamingResponse(client.settings)


Client = LilypadSDK

AsyncClient = AsyncLilypadSDK
