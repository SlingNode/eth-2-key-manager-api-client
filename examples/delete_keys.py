import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
pubkey = "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d"

response = eth_2_key_manager.delete_keys.sync_detailed(pubkeys=[pubkey])
if response.status_code == 200:
    print("Keystore deleted successfully")
else:
    print(f"Keystore delete failed with status code: {response.status_code}")
assert response.status_code == 200
