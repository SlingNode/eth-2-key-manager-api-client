import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
pubkey = "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
response = eth_2_key_manager.delete_remote_keys.sync_detailed(pubkeys=[pubkey])

if response.status_code == 200:
    print("Remote keys deleted successfully")
else:
    print(f"Remote keys delete failed with status code: {response.status_code}")
