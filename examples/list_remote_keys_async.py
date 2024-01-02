import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")


async def list_remote_keys_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.list_remote_keys.asyncio_detailed()

    if response.status_code == 200:
        print(f"\n\n{validator[0]} - {validator[1]}")
        # Assert that the response is of the expected type to satisfy static type checking.
        # Ref: https://mypy.readthedocs.io/en/stable/error_code_list.html#check-that-attribute-exists-in-each-union-item-union-attr
        assert isinstance(response.parsed, eth_2_key_manager_api_client.models.list_remote_keys_response.ListRemoteKeysResponse)

        print(f"Number of remote keys: {len(response.parsed.data)}")
        if response.parsed.data:
            print("List of keys:")
            for key in response.parsed.data:
                print(f"    {key.pubkey}")
    else:
        print(f"{validator[0]} - {validator[1]} - Remote keys listing failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(list_remote_keys_async(validator) for validator in validators))


asyncio.run(main())
