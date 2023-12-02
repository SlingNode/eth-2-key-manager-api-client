import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
response = eth_2_key_manager.list_fee_recipient.sync_detailed(pubkey=pubkey)
if response.status_code == 200:
    assert isinstance(response.parsed, eth_2_key_manager_api_client.models.list_fee_recipient_response.ListFeeRecipientResponse)
    print(f"Fee recipient for pubkey {pubkey} is {response.parsed.data.ethaddress}")
else:
    print(f"Fee Recipient listing failed with status code: {response.status_code}")
assert response.status_code == 200
