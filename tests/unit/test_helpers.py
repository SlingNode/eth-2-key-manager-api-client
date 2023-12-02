"""Test cases for the helpers module."""

import httpx
import pytest

from eth_2_key_manager_api_client import errors
from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.helpers import _build_response, _get_kwargs, _parse_error_response, _parse_response
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.list_remote_keys_response import ListRemoteKeysResponse
from eth_2_key_manager_api_client.models.set_gas_limit_request import SetGasLimitRequest
from eth_2_key_manager_api_client.types import Response

from ..mocks import (
    mock_response_400,
    mock_response_401,
    mock_response_403,
    mock_response_404,
    mock_response_500,
    mock_response_list_remote_keys_200,
)


def test_build_response():
    """Test the _build_response helper."""

    response = httpx.Response(200, json=mock_response_list_remote_keys_200, headers={"test_header": "test_value"})

    client = AuthenticatedClient(base_url="http://localhost:8080", token="test_token")

    built_response = _build_response(client=client, response=response, cls=ListRemoteKeysResponse)

    assert isinstance(built_response, Response)
    assert isinstance(built_response.parsed, ListRemoteKeysResponse)
    assert built_response.parsed.to_dict() == mock_response_list_remote_keys_200
    assert built_response.status_code == 200
    assert built_response.headers["test_header"] == "test_value"
    assert built_response.content == response.content


test_data_error_responses = [
    (400, mock_response_400),
    (401, mock_response_401),
    (403, mock_response_403),
    (404, mock_response_404),
    (500, mock_response_500),
]


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_parse_error_response(status_code, mock_response):

    response = httpx.Response(status_code, json=mock_response)
    error_response = _parse_error_response(response)

    assert isinstance(error_response, ErrorResponse)
    assert error_response.message == mock_response["message"]


def test_parse_error_response_none():

    response = httpx.Response(407, json={"message": "Unexpected status code"})
    error_response = _parse_error_response(response)

    assert error_response is None


def test_parse_response_raise_model_class_unspecified():
    """Test the _parse_response helper."""

    response = httpx.Response(200, json={"test": "test"})

    client = AuthenticatedClient(base_url="http://localhost:8080", token="test_token")

    with pytest.raises(errors.ModelClassUnspecified):
        _parse_response(client=client, response=response)


def test_parse_response_raise_unexpected_status():
    """Test the _parse_response helper."""

    response = httpx.Response(407, json={"test": "test"})

    client = AuthenticatedClient(
        base_url="http://localhost:8080",
        token="test_token",
        raise_on_unexpected_status=True,
    )

    with pytest.raises(errors.UnexpectedStatus):
        _parse_response(client=client, response=response)


def test_parse_response_200():
    """Test the _parse_response helper."""

    response = httpx.Response(200, json=mock_response_list_remote_keys_200)

    client = AuthenticatedClient(base_url="http://localhost:8080", token="test_token")

    parsed_response = _parse_response(client=client, response=response, cls=ListRemoteKeysResponse)

    assert isinstance(parsed_response, ListRemoteKeysResponse)


test_data_responses = [(202), (204)]


@pytest.mark.parametrize("status_code", test_data_responses)
def test_parse_response(status_code):
    """Test the _parse_response helper."""

    response = httpx.Response(status_code)

    client = AuthenticatedClient(base_url="http://localhost:8080", token="test_token")

    parsed_response = _parse_response(client=client, response=response)

    assert parsed_response is None


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_parse_response_errors(status_code, mock_response):

    response = httpx.Response(status_code, json=mock_response)
    client = AuthenticatedClient(base_url="http://localhost:8080", token="test_token")

    parsed_response = _parse_response(client=client, response=response)

    assert isinstance(parsed_response, ErrorResponse)
    assert parsed_response.message == mock_response["message"]


def test_get_kwargs_without_json_body():
    """Test the _get_kwargs helper without json body."""
    client = AuthenticatedClient(
        base_url="http://localhost:8080",
        token="test_token",
        headers={"test_header": "test_value"},
        cookies={"test_cookie": "test_value"},
    )
    kwargs = _get_kwargs(client=client, endpoint="test", method="GET")
    assert kwargs["headers"]["test_header"] == "test_value"
    assert kwargs["cookies"]["test_cookie"] == "test_value"
    assert kwargs["url"] == "http://localhost:8080/eth/v1/test"
    assert kwargs["method"] == "GET"
    assert kwargs["timeout"] == 5.0
    assert not kwargs["follow_redirects"]


def test_get_kwargs_with_json_body():
    """Test the _get_kwargs helper with json body."""
    client = AuthenticatedClient(
        base_url="http://localhost:8080",
        token="test_token",
        headers={"test_header": "test_value"},
        cookies={"test_cookie": "test_value"},
    )

    json_body = SetGasLimitRequest(gas_limit=999999)
    kwargs = _get_kwargs(client=client, endpoint="test", method="GET", json_body=json_body)

    assert kwargs["headers"]["test_header"] == "test_value"
    assert kwargs["cookies"]["test_cookie"] == "test_value"
    assert kwargs["url"] == "http://localhost:8080/eth/v1/test"
    assert kwargs["method"] == "GET"
    assert kwargs["timeout"] == 5.0
    assert not kwargs["follow_redirects"]
    assert kwargs["json"] == {"gas_limit": 999999}
