import pytest

from eth_2_key_manager_api_client.models.fee_recipient import FeeRecipient
from eth_2_key_manager_api_client.models.list_fee_recipient_response import ListFeeRecipientResponse
from eth_2_key_manager_api_client.models.list_fee_recipient_response_data import ListFeeRecipientResponseData
from eth_2_key_manager_api_client.models.set_fee_recipient_request import SetFeeRecipientRequest

test_data_source_dict_response = {"message": "test_message", "test_key": "test_value"}


test_data_fee_recipient = [FeeRecipient, ListFeeRecipientResponseData]


@pytest.mark.parametrize("fee_recipient_class", test_data_fee_recipient)
def test_fee_recipient(fee_recipient_class):
    """Test case for FeeRecipient and ListFeeRecipientResponseData model"""

    source_dict = {
        "ethaddress": "0xabcf8e0d4e9587369b2301d0790347320302cc09",
        "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
        "test_key": "test_value",
    }

    f_recipient = fee_recipient_class.from_dict(source_dict)

    assert f_recipient.ethaddress == "0xabcf8e0d4e9587369b2301d0790347320302cc09"
    assert f_recipient.pubkey == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    assert f_recipient.to_dict() == source_dict

    f_recipient["added_test_key"] = "added_test_value"
    assert f_recipient.additional_keys == ["test_key", "added_test_key"]
    assert f_recipient["added_test_key"] == "added_test_value"
    del f_recipient["added_test_key"]
    assert "added_test_key" not in f_recipient


def test_list_fee_recipient_response():
    """Test case for ListFeeRecipientResponse response"""

    source_dict = {
        "data": {
            "ethaddress": "0xabcf8e0d4e9587369b2301d0790347320302cc09",
            "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
            "test_key": "test_value",
        },
        "test_key": "test_value",
    }

    response = ListFeeRecipientResponse.from_dict(source_dict)

    assert response.data.ethaddress == "0xabcf8e0d4e9587369b2301d0790347320302cc09"
    assert response.data.pubkey == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    assert response.to_dict() == source_dict

    response["added_test_key"] = "added_test_value"
    assert response.additional_keys == ["test_key", "added_test_key"]
    assert response["added_test_key"] == "added_test_value"
    del response["added_test_key"]
    assert "added_test_key" not in response


def test_set_fee_recipient_request():
    """Test case for SetFeeRecipientRequest request"""

    source_dict = {
        "ethaddress": "0xabcf8e0d4e9587369b2301d0790347320302cc09",
        "test_key": "test_value",
    }

    request = SetFeeRecipientRequest.from_dict(source_dict)

    assert request.ethaddress == "0xabcf8e0d4e9587369b2301d0790347320302cc09"
    assert request.to_dict() == source_dict

    assert request.additional_keys == ["test_key"]
    request["added_test_key"] = "added_test_value"
    assert request.additional_keys == ["test_key", "added_test_key"]
    assert request["added_test_key"] == "added_test_value"
    del request["added_test_key"]
    assert "added_test_key" not in request
