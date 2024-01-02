import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")

pubkey = "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"


async def delete_remote_keys_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.delete_remote_keys.asyncio_detailed(pubkeys=[pubkey])

    if response.status_code == 200:
        print(f"{validator[0]} - {validator[1]} - Remote keys deleted successfully")
    else:
        print(f"{validator[0]} - {validator[1]} - Remote keys delete failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(delete_remote_keys_async(validator) for validator in validators))


asyncio.run(main())
