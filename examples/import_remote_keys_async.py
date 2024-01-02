import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")

# validators = [
#     (
#         "LIGHTHOUSE",
#         "http://192.168.121.71:7500",
#         "api-token-0x024fa0a0c597e83a970e689866703a89a555c9ee602d08cf848ee7935509a62f33"
#     ),
#     (
#         "TEKU",
#         "https://192.168.121.245:7500",
#         "5b874584cecab7eadfc3a224f177272f"
#     ),
#     (
#         "NIMBUS",
#         "http://192.168.121.61:7500",
#         "fcb4869b587a71b6d7ff25c85ac312201e53"
#     ),
#     (
#         "LODESTAR",
#         "http://192.168.121.118:7500",
#         "api-token-0xff6b738e030ee41e6bc317c204e2dae8965f6d666dc158e5690940936eeb35d9"
#     )
# ]

remote_keys = [{"pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a", "url": "https://remote.signer"}]


async def import_remote_keys_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.import_remote_keys.asyncio_detailed(remote_keys=remote_keys)

    if response.status_code == 200:
        print(f"{validator[0]} - {validator[1]} - Remote keys imported successfully")
    else:
        print(f"{validator[0]} - {validator[1]} - Remote keys import failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(import_remote_keys_async(validator) for validator in validators))


asyncio.run(main())
