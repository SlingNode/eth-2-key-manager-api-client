# Overview

This module is a wrapper for ETH 2 Key Manager API. The API enables users to manage Ethereum Validators' keys. It is an open standard defined at [https://ethereum.github.io/keymanager-APIs/](https://ethereum.github.io/keymanager-APIs/). All validator clients including Web3Signer implement the API.

Validator clients' native key management is CLI based which does not work well with automation tools such as Ansible. Furthermore each client does it slightly differently and some need to be restarted in order to import or delete keys.

The ETH 2 Key Manager API (also referred to as Validator API) enables users to use a single interface to manage keys for all clients. The keystore operations performed using the API do not require the client to be restarted.

## Asynchronous and synchronous methods

The API client provides both asynchronous and synchronous methods. Both methods are implemented using the [httpx](https://www.python-httpx.org/) library, which uses AsyncIO under the hood. The asynchronous methods let you perform operation on multiple validators in non-blocking manner. This is significantly faster when managing large number of validators. Refer to [examples](https://eth-2-key-manager-api-client.slingnode.com/) for sample scripts.


## Resources

The Full documentation is available at [https://eth-2-key-manager-api-client.slingnode.com/](https://eth-2-key-manager-api-client.slingnode.com/)

PyPi package: [https://pypi.org/project/eth-2-key-manager-api-client/](https://pypi.org/project/eth-2-key-manager-api-client/)

GitHub repository: [https://github.com/SlingNode/eth-2-key-manager-api-client/](https://github.com/SlingNode/eth-2-key-manager-api-client/)

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

All clients except Nimbus generate the bearer token automatically and save it to a file on the validator server. For the location of the file on each client refer to [https://docs.slingnode.com/slingnode.ethereum/enabling-validator-client-api#bearer-token](https://docs.slingnode.com/slingnode.ethereum/enabling-validator-client-api#bearer-token)

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


For full list of examples refer to [examples](examples.md)


## Import keystores - synchronous

```python
--8<--
examples/import_keystores.py
--8<--
```

## List keys - synchronous

```python
--8<--
examples/list_keys.py
--8<--
```

## Import remote keys - asynchronous

```python
--8<--
examples/import_remote_keys_async.py
--8<--
```

## List keys - asynchronous

```python
--8<--
examples/list_keys_async.py
--8<--
```
