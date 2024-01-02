import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")


async def list_keys_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.list_keys.asyncio_detailed()

    if response.status_code == 200:
        print(f"{validator[0]} - {validator[1]} - Number of keys: {len(response.parsed.data)}")
        if response.parsed.data:
            print("List of keys:")
            for key in response.parsed.data:
                print(f"    {key.validating_pubkey}")
    else:
        print(f"{validator[0]} - {validator[1]} - List keys failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(list_keys_async(validator) for validator in validators))


asyncio.run(main())
