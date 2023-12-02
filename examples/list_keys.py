import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
response = eth_2_key_manager.list_keys.sync_detailed()

if response.status_code == 200:
    print(f"Validator: {eth_2_key_manager.client.base_url}")
    assert isinstance(response.parsed, eth_2_key_manager_api_client.models.list_keys_response.ListKeysResponse)
    print(f"Number of keys: {len(response.parsed.data)}")
    if response.parsed.data:
        print("List of keys:")
        for key in response.parsed.data:
            print(f"    {key.validating_pubkey}")
else:
    print(f"List keys failed with status code: {response.status_code}")
