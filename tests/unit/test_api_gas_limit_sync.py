"""Unit tests for the gas limit sync API endpoint."""

# Standard Library
from typing import Dict

import pytest
from pytest_httpx import HTTPXMock

import eth_2_key_manager_api_client
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.list_gas_limit_response import ListGasLimitResponse
from eth_2_key_manager_api_client.models.list_gas_limit_response_data import ListGasLimitResponseData

from ..mocks import mock_response_400, mock_response_401, mock_response_403, mock_response_404, mock_response_500

# set_gas_limit tests


def test_set_gas_limit_202(httpx_mock: HTTPXMock):
    """Test case for set_gas_limit with 202 response"""

    httpx_mock.add_response(status_code=202)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    # .sync method returns None
    response = client.set_gas_limit.sync_detailed(pubkey=pubkey, gas_limit="999999")

    assert response.status_code == 202


test_data_error_responses = [
    (400, mock_response_400),
    (401, mock_response_401),
    (403, mock_response_403),
    (404, mock_response_404),
    (500, mock_response_500),
]


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_set_gas_limit_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for set_gas_limit errors"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    # .sync method returns None
    response = client.set_gas_limit.sync(pubkey=pubkey, gas_limit="999999")

    assert isinstance(response, ErrorResponse)


# get_gas_limit tests


def test_get_gas_limit_200(httpx_mock: HTTPXMock):
    """Test case fpr get_gas_limit with 200 response"""

    mock_get_gas_limit_200 = {
        "data": {
            "pubkey": "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad",
            "gas_limit": "3456",
        }
    }

    httpx_mock.add_response(status_code=200, json=mock_get_gas_limit_200)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.get_gas_limit.sync(pubkey=pubkey)

    assert isinstance(response, ListGasLimitResponse)
    assert isinstance(response.data, ListGasLimitResponseData)
    assert response.data.gas_limit == "3456"


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_get_gas_limit_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for get_gas_limit errors"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.get_gas_limit.sync(pubkey=pubkey)

    assert isinstance(response, ErrorResponse)


# delete_gas_limit tests


def test_delete_gas_limit_204(httpx_mock: HTTPXMock):
    """Test case for delete_gas_limit with 204 response"""

    httpx_mock.add_response(status_code=204)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    # .sync returns None
    # Response(status_code=<HTTPStatus.NO_CONTENT: 204>, content=b'', headers=Headers({'content-type': 'application/json', 'signature': '0x3045022100b927a28403be4d3e87dac35629207636d708950a567da476882ede45d7589bfe02206193d6ec3bd606281ee58a34bcd33fa73c2741e577955609396c88342d44b0d3', 'server': 'Lighthouse/v4.3.0-dfcb336/x86_64-linux', 'date': 'Sun, 20 Aug 2023 07:30:10 GMT'}), parsed=None)
    response = client.delete_gas_limit.sync_detailed(pubkey=pubkey)

    assert response.status_code == 204


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_delete_gas_limit_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for delete_gas_limit errors"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.delete_gas_limit.sync(pubkey=pubkey)

    assert isinstance(response, ErrorResponse)
