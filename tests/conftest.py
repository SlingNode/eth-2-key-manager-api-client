# Standard Library
import os
from typing import List, Tuple

import pytest

import eth_2_key_manager_api_client


def parse_file(filename=".env") -> List[Tuple[str, str, str]]:
    with open(filename, "r") as file:
        lines = file.readlines()

    result = []
    for line in lines:
        parts = line.strip().split(" ")
        if len(parts) == 3:
            result.append((parts[0], parts[1], parts[2]))

    return result


@pytest.fixture
def get_client_configs():
    return parse_file()


@pytest.fixture
def set_valid_client_config_env_vars(request):
    print(f"\nValidator client -> {request.param[0]}")
    os.environ["ETH_2_KEY_MANAGER_API_BASE_URL"] = request.param[1]
    os.environ["ETH_2_KEY_MANAGER_API_TOKEN"] = request.param[2]
    return request.param[0]


@pytest.fixture
def set_mock_client_config_env_vars():
    os.environ["ETH_2_KEY_MANAGER_API_BASE_URL"] = "http://localhost:7501"
    os.environ["ETH_2_KEY_MANAGER_API_TOKEN"] = "token1"


@pytest.fixture
def keystore_str():
    """Fixture for keystore_dict"""
    json_str = """{
    "crypto": {
        "kdf": {
            "function": "scrypt",
            "params": {
                "dklen": 32,
                "n": 262144,
                "r": 8,
                "p": 1,
                "salt": "1c4a91c48175d4742b88c0c3cca7321ba8e3127906678a0f0195321234b2f61d"
            },
            "message": ""
        },
        "checksum": {
            "function": "sha256",
            "params": {},
            "message": "8f260d986ba4cf13dd75998d8b0f10bef6a5e60fdcec3fc0d606b082077c1b24"
        },
        "cipher": {
            "function": "aes-128-ctr",
            "params": {
                "iv": "77495a6ef36049d4edb83dd02bbe419b"
            },
            "message": "d28fd393f4ee8b2516e4f8287245a2ccf1e42816b684becfca6c56c3b56d6ae5"
        }
    },
    "description": "",
    "pubkey": "99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b",
    "path": "m/12381/3600/2/0/0",
    "uuid": "6d4913af-4cc2-457f-a962-39eca6d0dd37",
    "version": 4
    }"""

    return json_str


@pytest.fixture
def keystore_password_str():
    """Fixture for keystore_password"""
    return "validatorkey123"


@pytest.fixture
def slashing_protection_str():

    json_str = """{
    "metadata": {
        "interchange_format_version": "5",
        "genesis_validators_root": "0x043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb"
    },
    "data": [
        {
            "pubkey": "0x876a9a7fadb5b9d2114a5180f9fe50b451cbab5f241b42e476b724a3575e5a8277767bc5a7c831c63f066a9a725c53d6",
            "signed_blocks": [
                {
                    "slot": "4866645",
                    "signing_root": "0xc24c384a4b9ecef533b6d838691d83ac3e4b06c2903fb09200957583ea291c3d"
                }
            ],
            "signed_attestations": [
                {
                    "source_epoch": "154315",
                    "target_epoch": "154316",
                    "signing_root": "0x04ec24fb31df03f65b7af9a74a62bf3c8e44817ae1f976b1d9c81af277f3ddfa"
                },
                {
                    "source_epoch": "154316",
                    "target_epoch": "154317",
                    "signing_root": "0x9d731a700e06f0999b6964d65b6858022690387a47d25919f6e01daa6173dfc9"
                }
            ]
        }
    ]
    }"""

    return json_str


@pytest.fixture
def setup_test_import_keystore(keystore_str, keystore_password_str, slashing_protection_str, set_valid_client_config_env_vars):

    client = eth_2_key_manager_api_client.Eth2KeyManager()
    response = client.import_keystores.sync_detailed([keystore_str], [keystore_password_str], slashing_protection_str)

    if response.status_code != 200:
        raise Exception("Error importing keystore")


@pytest.fixture
def teardown_test_delete_keys():

    client = eth_2_key_manager_api_client.Eth2KeyManager()
    pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"

    response = client.delete_keys.sync(pubkeys=[pubkey])
    if response.data[0].status != "deleted":
        raise Exception("Error deleting keystore")


@pytest.fixture
def setup_and_teardown_test(keystore_str, keystore_password_str, slashing_protection_str, set_valid_client_config_env_vars):
    pubkey: str = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
    client = eth_2_key_manager_api_client.Eth2KeyManager()
    response = client.import_keystores.sync_detailed([keystore_str], [keystore_password_str], slashing_protection_str)
    if response.status_code != 200:
        raise Exception("Error importing keystore")
    yield client
    client = eth_2_key_manager_api_client.Eth2KeyManager()
    response = client.delete_keys.sync(pubkeys=[pubkey])
    if response.data[0].status != "deleted":
        raise Exception("Error deleting keystore")
