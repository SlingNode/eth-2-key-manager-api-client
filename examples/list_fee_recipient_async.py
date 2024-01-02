import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")

pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"


async def list_fee_recipient_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.list_fee_recipient.asyncio_detailed(pubkey=pubkey)

    if response.status_code == 200:
        assert isinstance(response.parsed, eth_2_key_manager_api_client.models.list_fee_recipient_response.ListFeeRecipientResponse)
        print(f"{validator[0]} - {validator[1]} - Fee recipient for pubkey {pubkey} is {response.parsed.data.ethaddress}")
    else:
        print(f"{validator[0]} - {validator[1]} - Fee Recipient listing failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(list_fee_recipient_async(validator) for validator in validators))


asyncio.run(main())
