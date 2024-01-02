import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")

pubkeys = [
    "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d",
    "0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad",
    "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b",
]


async def delete_keys_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.delete_keys.asyncio_detailed(pubkeys=pubkeys)

    if response.status_code == 200:
        print(f"{validator[0]} - {validator[1]} - Keystore deleted successfully")
    else:
        print(f"{validator[0]} - {validator[1]} - Keystore delete failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(delete_keys_async(validator) for validator in validators))


asyncio.run(main())
