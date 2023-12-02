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
