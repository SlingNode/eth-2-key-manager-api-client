"""
API tests for LocalKeyManager
"""

# Standard Library
from typing import Dict

import pytest
from pytest_httpx import HTTPXMock

import eth_2_key_manager_api_client
from eth_2_key_manager_api_client import errors
from eth_2_key_manager_api_client.models.delete_keys_response import DeleteKeysResponse
from eth_2_key_manager_api_client.models.delete_keys_response_data_item import DeleteKeysResponseDataItem
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.import_keystores_response import ImportKeystoresResponse
from eth_2_key_manager_api_client.models.import_keystores_response_data_item import ImportKeystoresResponseDataItem
from eth_2_key_manager_api_client.models.list_keys_response import ListKeysResponse
from eth_2_key_manager_api_client.models.list_keys_response_data_item import ListKeysResponseDataItem
from eth_2_key_manager_api_client.types import Response

from ..mocks import mock_response_400, mock_response_401, mock_response_403, mock_response_500

# from httpx import Response

# list_keys tests


def test_list_keys_200(httpx_mock: HTTPXMock):
    """Test case for list_keys with 200 response"""

    mock_response_list_keys_200 = {
        "data": [
            {
                "validating_pubkey": "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad",
                "derivation_path": "m/12381/3600/1/0/0",
                "readonly": "false",
            }
        ]
    }

    httpx_mock.add_response(status_code=200, json=mock_response_list_keys_200)

    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.list_keys.sync()

    assert isinstance(response, ListKeysResponse)
    assert isinstance(response.data[0], ListKeysResponseDataItem)
    assert response.data[0].validating_pubkey == "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"


test_data_error_responses = [
    (401, mock_response_401),
    (403, mock_response_403),
    (500, mock_response_500),
]


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_list_keys_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test cases for list_keys errors"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.list_keys.sync()

    assert isinstance(response, ErrorResponse)


def test_unexpected_status_code_raise_on_unexpected_status(httpx_mock: HTTPXMock):
    """Test case for list_keys with unexpected status code"""

    httpx_mock.add_response(status_code=407, json={"message": "Unexpected status code"})
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token", raise_on_unexpected_status=True)

    with pytest.raises(errors.UnexpectedStatus):
        client.list_keys.sync()


def test_unexpected_status_code(httpx_mock: HTTPXMock):
    """Test case for list_keys with unexpected status code"""

    httpx_mock.add_response(status_code=407, json={"message": "Unexpected status code"})
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.list_keys.sync_detailed()

    assert isinstance(response, Response)
    assert response.status_code == 407


# import_keystores tests


def test_import_keystores_200(httpx_mock: HTTPXMock, keystore_str: str, keystore_password_str: str, slashing_protection_str: str):
    """Test case for import_keystores with 200 response"""

    mock_response = {"data": [{"status": "imported"}]}

    httpx_mock.add_response(status_code=200, json=mock_response)

    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.import_keystores.sync([keystore_str], [keystore_password_str], slashing_protection_str)

    assert isinstance(response, ImportKeystoresResponse)
    assert isinstance(response.data[0], ImportKeystoresResponseDataItem)


def test_import_keystores_200_without_slashing_protection(httpx_mock: HTTPXMock, keystore_str: str, keystore_password_str: str):
    """Test case for import_keystores with 200 response"""

    mock_response = {"data": [{"status": "imported"}]}

    httpx_mock.add_response(status_code=200, json=mock_response)

    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.import_keystores.sync([keystore_str], [keystore_password_str])

    assert isinstance(response, ImportKeystoresResponse)
    assert isinstance(response.data[0], ImportKeystoresResponseDataItem)


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses + [(400, mock_response_400)])
def test_import_keystores_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock, keystore_str: str, keystore_password_str):
    """Test case for import_keystores errors"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)

    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.import_keystores.sync([keystore_str], [keystore_password_str], "invalid_slashing_protection")

    assert isinstance(response, ErrorResponse)


# delete_keys keys


def test_delete_keys_200(httpx_mock: HTTPXMock):
    """Test case for delete_keys with 200 response"""

    pubkey: str = "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d"

    mock_response = {
        "data": [{"status": "deleted"}],
        "slashing_protection": """{"metadata":{"interchange_format_version":"5","genesis_validators_root":"0x043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb"},
        "data":[{"pubkey":"0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad","signed_blocks":[],"signed_attestations":[]}]}""",
    }

    httpx_mock.add_response(status_code=200, json=mock_response)

    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.delete_keys.sync([pubkey])

    assert isinstance(response, DeleteKeysResponse)
    assert isinstance(response.data[0], DeleteKeysResponseDataItem)


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses + [(400, mock_response_400)])
def test_delete_keys_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for delete_keys error responses"""

    pubkey: str = "invalid_key"

    httpx_mock.add_response(status_code=status_code, json=mock_response)

    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")
    response = client.delete_keys.sync([pubkey])

    assert isinstance(response, ErrorResponse)
