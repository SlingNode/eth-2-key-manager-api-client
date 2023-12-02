import pytest
from attr import asdict

import eth_2_key_manager_api_client
from eth_2_key_manager_api_client.api.fee_recipient import DeleteFeeRecipient, ListFeeRecipient, SetFeeRecipient
from eth_2_key_manager_api_client.api.gas_limit import DeleteGasLimit, GetGasLimit, SetGasLimit
from eth_2_key_manager_api_client.api.local_key_manager import ImportKeystores, ListKeys
from eth_2_key_manager_api_client.api.remote_key_manager import DeleteRemoteKeys, ImportRemoteKeys, ListRemoteKeys
from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.errors import ConfigurationMissing


def test_class_instance():

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(
        "http://localhost:7500",
        "token",
        cookies={"cookie": "chocolate"},
        headers={"header": "value"},
        timeout=10.0,
        verify_ssl=False,
        raise_on_unexpected_status=True,
        follow_redirects=True,
    )
    assert eth_2_key_manager.client.base_url == "http://localhost:7500"
    assert eth_2_key_manager.client.token == "token"
    assert isinstance(eth_2_key_manager.client, eth_2_key_manager_api_client.client.AuthenticatedClient)
    assert isinstance(eth_2_key_manager.import_keystores, ImportKeystores)
    assert isinstance(eth_2_key_manager.list_keys, ListKeys)
    assert isinstance(eth_2_key_manager.delete_fee_recipient, DeleteFeeRecipient)
    assert isinstance(eth_2_key_manager.list_fee_recipient, ListFeeRecipient)
    assert isinstance(eth_2_key_manager.set_fee_recipient, SetFeeRecipient)
    assert isinstance(eth_2_key_manager.set_gas_limit, SetGasLimit)
    assert isinstance(eth_2_key_manager.get_gas_limit, GetGasLimit)
    assert isinstance(eth_2_key_manager.delete_gas_limit, DeleteGasLimit)
    assert isinstance(eth_2_key_manager.delete_remote_keys, DeleteRemoteKeys)
    assert isinstance(eth_2_key_manager.import_remote_keys, ImportRemoteKeys)
    assert isinstance(eth_2_key_manager.list_remote_keys, ListRemoteKeys)

    print(asdict(eth_2_key_manager.client))

    assert asdict(eth_2_key_manager.client) == {
        "base_url": "http://localhost:7500",
        "cookies": {"cookie": "chocolate"},
        "headers": {"header": "value"},
        "timeout": 10.0,
        "verify_ssl": False,
        "raise_on_unexpected_status": True,
        "follow_redirects": True,
        "token": "token",
        "prefix": "Bearer",
        "auth_header_name": "Authorization",
    }

    assert eth_2_key_manager.client.get_headers() == {"header": "value", "Authorization": "Bearer token"}
    assert eth_2_key_manager.client.get_cookies() == {"cookie": "chocolate"}
    assert eth_2_key_manager.client.get_timeout() == 10.0
    assert isinstance(eth_2_key_manager.client.with_headers({"header2": "value2"}), AuthenticatedClient)
    assert eth_2_key_manager.client.with_headers({"header2": "value2"}).get_headers() == {
        "header": "value",
        "header2": "value2",
        "Authorization": "Bearer token",
    }
    assert isinstance(eth_2_key_manager.client.with_cookies({"cookie2": "chocolate2"}), AuthenticatedClient)
    assert eth_2_key_manager.client.with_cookies({"cookie2": "chocolate2"}).get_cookies() == {"cookie": "chocolate", "cookie2": "chocolate2"}


def test_class_raise_configuration_missing():

    with pytest.raises(ConfigurationMissing):
        eth_2_key_manager_api_client.Eth2KeyManager()


def test_class_configuration_env_vars(set_mock_client_config_env_vars):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()

    assert eth_2_key_manager.client.base_url == "http://localhost:7501"
    assert eth_2_key_manager.client.token == "token1"


def test_class_configuration_params():

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://localhost:7500", token="token")
    assert eth_2_key_manager.client.base_url == "http://localhost:7500"
    assert eth_2_key_manager.client.token == "token"


# def test_class_configuration_params_overwrite_env_vars(set_valid_client_config_env_vars):

#     eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
#     assert eth_2_key_manager.client.base_url == "http://localhost:7501"
#     assert eth_2_key_manager.client.token == "token1"
