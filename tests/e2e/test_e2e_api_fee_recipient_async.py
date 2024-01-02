import pytest

from ..conftest import parse_file


@pytest.mark.asyncio
@pytest.mark.parametrize("set_valid_client_config_env_vars", parse_file(), indirect=True)
async def test_e2e_fee_recipient_docstrings_code(setup_and_teardown_test, set_valid_client_config_env_vars):

    import eth_2_key_manager_api_client

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
    pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
    response = await eth_2_key_manager.set_fee_recipient.asyncio_detailed(pubkey=pubkey, ethaddress="0xabcf8e0d4e9587369b2301d0790347320302cc09")
    if response.status_code == 202:
        print("Fee Recipient set successfully")
    else:
        print(f"Fee Recipient set failed with status code: {response.status_code}")
    assert response.status_code == 202

    import eth_2_key_manager_api_client

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
    pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
    response = await eth_2_key_manager.list_fee_recipient.asyncio_detailed(pubkey=pubkey)
    if response.status_code == 200:
        print(f"Fee recipient for pubkey {pubkey} is {response.parsed.data.ethaddress}")
    else:
        print(f"Fee Recipient listing failed with status code: {response.status_code}")
    assert response.status_code == 200

    import eth_2_key_manager_api_client

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
    pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
    response = await eth_2_key_manager.delete_fee_recipient.asyncio_detailed(pubkey=pubkey)
    if response.status_code == 204:
        print("Fee Recipient deleted successfully")
    else:
        print(f"Fee Recipient deletion failed with status code: {response.status_code}")
    assert response.status_code == 204
