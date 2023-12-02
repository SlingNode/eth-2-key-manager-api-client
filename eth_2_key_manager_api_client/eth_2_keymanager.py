"""This module contains the Eth2KeyManager class, which is the main class of the eth-2-key-manager-api-client package.
"""
import os
import ssl
from typing import Dict, Union

import attr

from eth_2_key_manager_api_client.api.fee_recipient import DeleteFeeRecipient, ListFeeRecipient, SetFeeRecipient
from eth_2_key_manager_api_client.api.gas_limit import DeleteGasLimit, GetGasLimit, SetGasLimit
from eth_2_key_manager_api_client.api.local_key_manager import DeleteKeys, ImportKeystores, ListKeys
from eth_2_key_manager_api_client.api.remote_key_manager import DeleteRemoteKeys, ImportRemoteKeys, ListRemoteKeys
from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.errors import ConfigurationMissing


@attr.s(auto_attribs=True, init=False)
class Eth2KeyManager:
    """Eth2KeyManager class is the main class of the eth2-key-manager-api-client package.

    It provides a centralized way to manage keys for the Ethereum validators. It handles the following operations:

    * Importing keystores
    * Listing keys
    * Deleting keys
    * Setting fee recipients
    * Listing fee recipients
    * Deleting fee recipients
    * Setting gas limits
    * Getting gas limits
    * Deleting gas limits
    * Deleting remote keys
    * Importing remote keys
    * Listing remote keys

    Args:
        base_url (str | None): The base URL of the Eth2 Key Manager API.
        token (str | None): The API token to authenticate with the Eth2 Key Manager API.
        cookies (Dict[str, str]): Optional cookies to send with requests.
        headers (Dict[str, str]): Optional headers to send with requests.
        timeout (float): The timeout for requests.
        verify_ssl (Union[str, bool, ssl.SSLContext]): Whether to verify SSL certificates.
        raise_on_unexpected_status (bool): Whether to raise an exception if a request returns an unexpected status code.
        follow_redirects (bool): Whether to follow redirects.

    Raises:
        ConfigurationMissing: If the base_url or token is not provided.
    """

    def __init__(
        self,
        base_url: Union[str, None] = None,
        token: Union[str, None] = None,
        cookies: Dict[str, str] = {},
        headers: Dict[str, str] = {},
        timeout: float = 10.0,
        verify_ssl: Union[str, bool, ssl.SSLContext] = False,
        raise_on_unexpected_status: bool = False,
        follow_redirects: bool = False,
    ):
        if base_url is None:
            base_url = os.getenv("ETH_2_KEY_MANAGER_API_BASE_URL")
        if token is None:
            token = os.getenv("ETH_2_KEY_MANAGER_API_TOKEN")
        if base_url is None or token is None:
            raise ConfigurationMissing

        self.client = AuthenticatedClient(
            base_url=base_url,
            token=token,
            cookies=cookies,
            headers=headers,
            timeout=timeout,
            verify_ssl=verify_ssl,
            raise_on_unexpected_status=raise_on_unexpected_status,
            follow_redirects=follow_redirects,
        )
        self.import_keystores = ImportKeystores(self.client)
        self.list_keys = ListKeys(self.client)
        self.delete_keys = DeleteKeys(self.client)
        self.set_fee_recipient = SetFeeRecipient(self.client)
        self.list_fee_recipient = ListFeeRecipient(self.client)
        self.delete_fee_recipient = DeleteFeeRecipient(self.client)
        self.set_gas_limit = SetGasLimit(self.client)
        self.get_gas_limit = GetGasLimit(self.client)
        self.delete_gas_limit = DeleteGasLimit(self.client)
        self.delete_remote_keys = DeleteRemoteKeys(self.client)
        self.import_remote_keys = ImportRemoteKeys(self.client)
        self.list_remote_keys = ListRemoteKeys(self.client)
