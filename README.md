# Overview

This module is a wrapper for ETH 2 Key Manager API. The API enables users to manage Ethereum Validators' keys. The API is an open standard defined here https://ethereum.github.io/keymanager-APIs/. All validator clients including Web3Signer implement the API.

Validator clients' native key management is CLI based which does not work well with automation tools such as Ansible. Furthermore each client does it slightly differently and some need to be restarted in order to import or delete keys.

The ETH 2 Key Manager API (also referred to as Validator API) enables users to use a single interface to manage keys for all clients. The keystore operations performed using the API do not require the client to be restarted.

The module provides synchronous and asynchronous methods for all API endpoints. The synchronous methods are blocking and will return the response object when the request is complete. The asynchronous methods are implemented using AsyncIO and will return a coroutine object that can be awaited.


# Installation

The API client is available as a Python package. It can be installed using pip:

```bash
pip install eth_2_key_manager_api_client
```
# Getting started

## Specifying API endpoint and authentication token

By default the Eth2KyeManager class will read `base_url` and `token` values from the following environment variables.

```bash
ETH_2_KEY_MANAGER_API_BASE_URL
ETH_2_KEY_MANAGER_API_TOKEN
```

The ETH_2_KEY_MANAGER_API_BASE_URL environment variable must be set to the URL of the API endpoint. The ETH_2_KEY_MANAGER_API_TOKEN environment variable must be set to the authentication token.

For example:

```bash
ETH_2_KEY_MANAGER_API_BASE_URL=http://192.168.121.146:7500
ETH_2_KEY_MANAGER_API_TOKEN=api-token-0x02c21feda59e4759f558972e5038f21babb37e4e047f0a113a28bd1ad2f6263a16
```

All clients except Nimbus generate the bearer token automatically and save it to a file on the validator server. For the location of the file on each client refer to https://docs.slingnode.com/slingnode.ethereum/enabling-validator-client-api#bearer-token

### Creating class instance

Create class instance using the default values:

```python
import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
```

If the environment variables are not set, the values can be passed when creating the class instance using the `base_url` and `token` keyword arguments.

```python

import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(base_url="http://192.168.121.146:7500", token="token")
```

# Examples

For full list of examples refer to [examples](https://eth-2-key-manager-api-client.slingnode.com/).

## Import keystores

```python
import eth_2_key_manager_api_client

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

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager(timeout=10.0)

response = eth_2_key_manager.import_keystores.sync_detailed(list_of_keystore_strs, list_of_keystore_password_strs, slashing_protection_str)

if response.status_code == 200:
    print("Keystores imported successfully")
else:
    print(f"Keystores import failed with status code: {response.status_code}")
assert response.status_code == 200

```

## List keys

```python
import eth_2_key_manager_api_client

eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
response = eth_2_key_manager.list_keys.sync_detailed()

if response.status_code == 200:
    print(f"Validator: {eth_2_key_manager.client.base_url}")
    assert isinstance(response.parsed, eth_2_key_manager_api_client.models.list_keys_response.ListKeysResponse)
    print(f"Number of keys: {len(response.parsed.data)}")
    if response.parsed.data:
        print("List of keys:")
        for key in response.parsed.data:
            print(f"    {key.validating_pubkey}")
else:
    print(f"List keys failed with status code: {response.status_code}")

```
