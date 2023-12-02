"""This module contains private helper functions for the API client methods."""


from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from eth_2_key_manager_api_client import errors
from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.models.delete_keys_json_body import DeleteKeysJsonBody
from eth_2_key_manager_api_client.models.delete_keys_response import DeleteKeysResponse
from eth_2_key_manager_api_client.models.delete_remote_keys_json_body import DeleteRemoteKeysJsonBody
from eth_2_key_manager_api_client.models.delete_remote_keys_response import DeleteRemoteKeysResponse
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.import_keystores_json_body import ImportKeystoresJsonBody
from eth_2_key_manager_api_client.models.import_keystores_response import ImportKeystoresResponse
from eth_2_key_manager_api_client.models.import_remote_keys_json_body import ImportRemoteKeysJsonBody
from eth_2_key_manager_api_client.models.import_remote_keys_response import ImportRemoteKeysResponse
from eth_2_key_manager_api_client.models.list_fee_recipient_response import ListFeeRecipientResponse
from eth_2_key_manager_api_client.models.list_gas_limit_response import ListGasLimitResponse
from eth_2_key_manager_api_client.models.list_keys_response import ListKeysResponse
from eth_2_key_manager_api_client.models.list_remote_keys_response import ListRemoteKeysResponse
from eth_2_key_manager_api_client.models.set_fee_recipient_request import SetFeeRecipientRequest
from eth_2_key_manager_api_client.models.set_gas_limit_request import SetGasLimitRequest
from eth_2_key_manager_api_client.types import Response


def _build_response(
    *,
    client: AuthenticatedClient,
    response: httpx.Response,
    cls: Optional[Any] = None,
) -> Any:
    """Builds a response class instance from the API response.

    Args:
        client: The instance of the API client used to make the request.
        response: The HTTP response from the API call.
        cls: The response type class. If None, the response type will be Any.

    Returns:
        The response class instance.
    """

    parsed_response = _parse_response(client=client, response=response, cls=cls)

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed_response,
    )


def _parse_error_response(response: httpx.Response) -> Optional[ErrorResponse]:
    """Checks if the response is one of the expected error types and returns the error response.

    Args:
        response: The HTTP response from the API call.

    Returns:
        The error response if the response is one of the expected error types, otherwise None.
    """

    if response.status_code in [
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNAUTHORIZED,
        HTTPStatus.NOT_FOUND,
        HTTPStatus.FORBIDDEN,
        HTTPStatus.INTERNAL_SERVER_ERROR,
    ]:
        response_error = ErrorResponse.from_dict(response.json())

        return response_error
    return None


def _parse_response(
    *,
    client: AuthenticatedClient,
    response: httpx.Response,
    cls: Optional[
        Union[
            ListRemoteKeysResponse,
            ImportRemoteKeysResponse,
            DeleteRemoteKeysResponse,
            ListKeysResponse,
            ImportKeystoresResponse,
            DeleteKeysResponse,
            ListGasLimitResponse,
            ListFeeRecipientResponse,
        ]
    ] = None,
) -> Any:
    """
    Parses the response and returns the expected response type if the response is successful or
    ErrorResponse if the response is an error.

    Args:
        client: The instance of the client used to make the request.
        response: The HTTP response from the API call.
        cls: The response type class. If None, the response type will be Any.

    Raises:
        errors.ModelClassUnspecified: If the response is successful but the response type class is not specified.
        errors.UnexpectedStatus: If the response is not successful and Client.raise_on_unexpected_status is True.

    Returns:
        The expected response type if the response is successful or ErrorResponse if the response is an error.
    """
    if response.status_code == HTTPStatus.OK and cls is None:
        raise errors.ModelClassUnspecified(response.status_code, response.content)

    if response.status_code == HTTPStatus.OK and cls is not None:
        response_200 = cls.from_dict(response.json())
        return response_200

    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204

    if _parse_error_response(response) is not None:
        return _parse_error_response(response)

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)

    return None


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    endpoint: str,
    method: str,
    json_body: Union[
        ImportRemoteKeysJsonBody,
        DeleteRemoteKeysJsonBody,
        ImportKeystoresJsonBody,
        DeleteKeysJsonBody,
        SetGasLimitRequest,
        SetFeeRecipientRequest,
        None,
    ] = None,
) -> Dict[str, Any]:
    """Builds the keyword arguments for the HTTP request.

    Args:
        client: The instance of the client used to make the request.
        endpoint: The API endpoint for the request.
        method: The HTTP method for the request.
        json_body: The JSON body of the request.

    Returns:
        A dictionary of keyword arguments to be passed to the HTTP request.
    """

    url = f"{client.base_url}/eth/v1/{endpoint}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    request_kwargs: Dict[str, Any] = {
        "method": method,
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }

    if json_body is not None:
        request_kwargs["json"] = json_body.to_dict()

    return request_kwargs
