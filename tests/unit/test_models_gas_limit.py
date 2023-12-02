from eth_2_key_manager_api_client.models.set_gas_limit_request import SetGasLimitRequest


def test_set_gas_limit_request():
    """Test SetGasLimitRequest"""

    test_dict = {
        "gas_limit": "1000000000",
    }

    set_gas_limit_request_from_dict = SetGasLimitRequest.from_dict(test_dict)

    assert set_gas_limit_request_from_dict.gas_limit == "1000000000"
    assert set_gas_limit_request_from_dict.to_dict() == test_dict

    set_gas_limit_request = SetGasLimitRequest(gas_limit="9999")

    assert set_gas_limit_request.gas_limit == "9999"
    assert set_gas_limit_request.to_dict() == {"gas_limit": "9999"}
