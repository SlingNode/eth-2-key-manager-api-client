"""Unit tests for the fee recipient API endpoint."""

# Standard Library
from typing import Dict

import pytest
from pytest_httpx import HTTPXMock

import eth_2_key_manager_api_client
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.list_fee_recipient_response import ListFeeRecipientResponse
from eth_2_key_manager_api_client.models.list_fee_recipient_response_data import ListFeeRecipientResponseData

from ..mocks import mock_response_400, mock_response_401, mock_response_403, mock_response_404, mock_response_500

# set_fee_recipient tests


def test_set_fee_recipient_202(httpx_mock: HTTPXMock):
    """Test case for set_fee_recipient with 202 response"""

    httpx_mock.add_response(status_code=202)

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.set_fee_recipient.sync_detailed(pubkey=pubkey, ethaddress="0xabcf8e0d4e9587369b2301d0790347320302cc09")

    assert response.status_code == 202


test_data_error_responses = [
    (401, mock_response_401),
    (403, mock_response_403),
    (404, mock_response_404),
    (500, mock_response_500),
]


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses + [(400, mock_response_400)])
def test_set_fee_recipient_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for set_fee_recipient with error responses"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    response = client.set_fee_recipient.sync(pubkey=pubkey, ethaddress="0xabcf8e0d4e9587369b2301d0790347320302cc09")

    assert isinstance(response, ErrorResponse)


# list_fee_recipient tests


def test_list_fee_recipient_200(httpx_mock: HTTPXMock):
    """Test case for list_fee_recipient with 200 response"""

    mock_list_fee_recipient_200 = {
        "data": {
            "pubkey": "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad",
            "ethaddress": "0xabcf8e0d4e9587369b2301d0790347320302cc09",
        }
    }
    httpx_mock.add_response(status_code=200, json=mock_list_fee_recipient_200)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.list_fee_recipient.sync(pubkey=pubkey)

    assert isinstance(response, ListFeeRecipientResponse)
    assert isinstance(response.data, ListFeeRecipientResponseData)
    assert response.data.pubkey == "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"
    assert response.data.ethaddress == "0xabcf8e0d4e9587369b2301d0790347320302cc09"


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_list_fee_recipient_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for list_fee_recipient with error responses"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.list_fee_recipient.sync(pubkey=pubkey)

    assert isinstance(response, ErrorResponse)


# delete fee recipient tests


def test_delete_fee_recipient_204(httpx_mock: HTTPXMock):
    """Test case for delete_fee_recipient with 204 response"""

    httpx_mock.add_response(status_code=204)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.delete_fee_recipient.sync_detailed(pubkey=pubkey)

    assert response.status_code == 204


@pytest.mark.parametrize("status_code, mock_response", test_data_error_responses)
def test_delete_fee_recipient_errors(status_code: int, mock_response: Dict, httpx_mock: HTTPXMock):
    """Test case for delete_fee_recipient with error responses"""

    httpx_mock.add_response(status_code=status_code, json=mock_response)
    client = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:8080", token="test_token")

    pubkey: str = "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad"

    response = client.delete_fee_recipient.sync(pubkey=pubkey)

    assert isinstance(response, ErrorResponse)
