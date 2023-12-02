# Standard Library
from typing import Dict

import pytest
from pytest_httpx import HTTPXMock

import eth_2_key_manager_api_client
from eth_2_key_manager_api_client.models.delete_remote_keys_response import DeleteRemoteKeysResponse
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.import_remote_keys_response import ImportRemoteKeysResponse
from eth_2_key_manager_api_client.models.import_remote_keys_response_data_item import ImportRemoteKeysResponseDataItem
from eth_2_key_manager_api_client.models.list_remote_keys_response import ListRemoteKeysResponse
from eth_2_key_manager_api_client.models.list_remote_keys_response_data_item import ListRemoteKeysResponseDataItem

from ..mocks import mock_response_401, mock_response_403, mock_response_500, mock_response_list_remote_keys_200

# list_remote_keys tests


def test_list_remote_keys_200(httpx_mock: HTTPXMock):
    """Test case for list_remote_keys"""

    httpx_mock.add_response(status_code=200, json=mock_response_list_remote_keys_200)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.list_remote_keys.sync()

    assert isinstance(response, ListRemoteKeysResponse)
    assert isinstance(response.data[0], ListRemoteKeysResponseDataItem)
    assert response.data[0].pubkey == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    assert response.data[0].url == "https://remote.signer"


test_data_error_responses = [
    (401, mock_response_401),
    (403, mock_response_403),
    (500, mock_response_500),
]


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_list_remote_keys_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for list_remote_keys with error responses"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.list_remote_keys.sync()

    assert isinstance(response, ErrorResponse)


# import_remote_keys tests


def test_import_remote_keys_200(httpx_mock: HTTPXMock):
    """Test case for import_remote_keys with 200 response"""

    remote_keys = [
        {
            "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
            "url": "https://remote.signer",
        }
    ]

    mock_response_200 = {"data": [{"status": "imported"}]}

    httpx_mock.add_response(status_code=200, json=mock_response_200)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.import_remote_keys.sync(remote_keys=remote_keys)

    assert isinstance(response, ImportRemoteKeysResponse)
    assert isinstance(response.data[0], ImportRemoteKeysResponseDataItem)


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_import_remote_keys_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for import_remote_keys with error responses"""

    remote_keys = [
        {
            "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
            "url": "https://remote.signer",
        }
    ]

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.import_remote_keys.sync(remote_keys=remote_keys)

    assert isinstance(response, ErrorResponse)


# test delete_remote_keys


def test_delete_remote_keys_200(httpx_mock: HTTPXMock):
    """Test case for delete_remote_keys with 200 response"""

    pub_keys = ["0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"]

    mock_response_200 = {"data": [{"status": "deleted"}]}

    httpx_mock.add_response(status_code=200, json=mock_response_200)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.delete_remote_keys.sync(pubkeys=pub_keys)

    assert isinstance(response, DeleteRemoteKeysResponse)


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_delete_remote_keys_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for delete_remote_keys with error responses"""
    pub_keys = ["0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"]

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.delete_remote_keys.sync(pubkeys=pub_keys)

    assert isinstance(response, ErrorResponse)
