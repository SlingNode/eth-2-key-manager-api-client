import asyncio

import eth_2_key_manager_api_client
from tests.conftest import parse_file

validators = parse_file("../.env")

# Create lists of keystore and password strings, note: the order of the lists must match `passwords[i]` must unlock `keystores[i]`
list_of_keystore_strs: list[str] = []
list_of_keystore_password_strs: list[str] = []

keystore_files = [
    "mock_validator_keystores/keystore-m_12381_3600_0_0_0-1669980799.json",
    "mock_validator_keystores/keystore-m_12381_3600_1_0_0-1680087924.json",
    "mock_validator_keystores/keystore-m_12381_3600_2_0_0-1680087924.json",
]

# Read the keystores as strings
for keystore_file in keystore_files:
    with open(keystore_file, "r") as f:
        list_of_keystore_strs.append(f.read())

# Read the passwords as strings
keystore_password_files = [
    "mock_validator_keystores/keystore-m_12381_3600_0_0_0-1669980799.txt",
    "mock_validator_keystores/keystore-m_12381_3600_1_0_0-1680087924.txt",
    "mock_validator_keystores/keystore-m_12381_3600_2_0_0-1680087924.txt",
]

for keystore_password_file in keystore_password_files:
    with open(keystore_password_file, "r") as f:
        list_of_keystore_password_strs.append(f.read())

with open("mock_validator_keystores/slashing_protection_db.json", "r") as f:
    slashing_protection_str = f.read()


async def import_keystores_async(validator):

    eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url=validator[1], token=validator[2])

    response = await eth_2_key_manager.import_keystores.asyncio_detailed(list_of_keystore_strs, list_of_keystore_password_strs, slashing_protection_str)

    if response.status_code == 200:
        print(f"{validator[0]} - {validator[1]} - Keystores imported successfully")
    else:
        print(f"{validator[0]} - {validator[1]} - Keystores import failed with status code: {response.status_code}")


async def main():
    await asyncio.gather(*(import_keystores_async(validator) for validator in validators))


asyncio.run(main())
