import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
response = eth_2_key_manager.list_remote_keys.sync_detailed()

if response.status_code == 200:
    print(f"Validator: {eth_2_key_manager.client.base_url}")

    # Assert that the response is of the expected type to satisfy static type checking.
    # Ref: https://mypy.readthedocs.io/en/stable/error_code_list.html#check-that-attribute-exists-in-each-union-item-union-attr
    assert isinstance(response.parsed, eth_2_key_manager_api_client.models.list_remote_keys_response.ListRemoteKeysResponse)

    print(f"Number of remote keys: {len(response.parsed.data)}")
    if response.parsed.data:
        print("List of keys:")
        for key in response.parsed.data:
            print(f"    {key.pubkey}")
else:
    print(f"List remote keys failed with status code: {response.status_code}")
