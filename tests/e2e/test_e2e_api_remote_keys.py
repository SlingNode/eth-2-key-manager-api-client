import pytest

from ..conftest import parse_file


@pytest.mark.parametrize("set_valid_client_config_env_vars", parse_file(), indirect=True)
def test_e2e_api_remote_keys_docstrings_code(set_valid_client_config_env_vars):

    import eth_2_key_manager_api_client

    remote_keys = [
        {
            "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
            "url": "https://remote.signer",
        }
    ]

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
    response = eth_2_key_manager.import_remote_keys.sync_detailed(remote_keys=remote_keys)

    if response.status_code == 200:
        print("Remote keys imported successfully")
    else:
        print(f"Remote keys import failed with status code: {response.status_code}")

    assert response.status_code == 200

    # list remote keys
    import eth_2_key_manager_api_client

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
    response = eth_2_key_manager.list_remote_keys.sync_detailed()

    if response.status_code == 200:
        print(f"List of remote keys: {response.parsed.data}")
    else:
        print(f"List remote keys failed with status code: {response.status_code}")

    assert response.status_code == 200

    # delete remote keys
    import eth_2_key_manager_api_client

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
    pubkey = "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    response = eth_2_key_manager.delete_remote_keys.sync_detailed(pubkeys=[pubkey])

    if response.status_code == 200:
        print("Remote keys deleted successfully")
    else:
        print(f"Remote keys delete failed with status code: {response.status_code}")
