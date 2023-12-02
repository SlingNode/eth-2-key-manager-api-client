"""
Provides classes to interact with the set of endpoints for key management of local keys.

API reference: https://ethereum.github.io/keymanager-APIs/#/Remote%20Key%20Manager

Each class provides access to a specific endpoint. The classes are organized in the same way as the API documentation.

| Class               | API Endpoint                                          |
|---------------------|-------------------------------------------------------|
| DeleteRemoteKeys  | https://ethereum.github.io/keymanager-APIs/#/Remote%20Key%20Manager/deleteRemoteKeys |
| ListRemoteKeys    | https://ethereum.github.io/keymanager-APIs/#/Remote%20Key%20Manager/listRemoteKeys |
| ImportRemoteKeys     | https://ethereum.github.io/keymanager-APIs/#/Remote%20Key%20Manager/importRemoteKeys |
"""
from typing import Dict, List, Optional, Union

import attr
import httpx

from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.helpers import _build_response, _get_kwargs
from eth_2_key_manager_api_client.models.delete_remote_keys_json_body import DeleteRemoteKeysJsonBody
from eth_2_key_manager_api_client.models.delete_remote_keys_response import DeleteRemoteKeysResponse
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.import_remote_keys_json_body import ImportRemoteKeysJsonBody
from eth_2_key_manager_api_client.models.import_remote_keys_json_body_remote_keys_item import (
    ImportRemoteKeysJsonBodyRemoteKeysItem,
)
from eth_2_key_manager_api_client.models.import_remote_keys_response import ImportRemoteKeysResponse
from eth_2_key_manager_api_client.models.list_remote_keys_response import ListRemoteKeysResponse
from eth_2_key_manager_api_client.types import Response


@attr.s(auto_attribs=True)
class DeleteRemoteKeys:
    """Contains methods for accessing the DELETE method of the /eth/v1/remotekeys endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
        response = eth_2_key_manager.delete_remote_keys.sync_detailed(pubkeys=[pubkey])

        if response.status_code == 200:
            print("Remote keys deleted successfully")
        else:
            print(f"Remote keys delete failed with status code: {response.status_code}")
        ```
    """

    client: AuthenticatedClient
    ENDPOINT: str = "remotekeys"
    METHOD: str = "DELETE"

    def sync_detailed(self, pubkeys: List[str]) -> Response[Union[DeleteRemoteKeysResponse, ErrorResponse]]:
        """Delete Remote Keys (synchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the validator client and exist
        in its
        persistent storage.

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no existing
        keystores.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and DeleteRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        json_body = DeleteRemoteKeysJsonBody(pubkeys=pubkeys)

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=json_body,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=DeleteRemoteKeysResponse)

    def sync(self, pubkeys: List[str]) -> Optional[Union[DeleteRemoteKeysResponse, ErrorResponse]]:
        """Delete Remote Keys (synchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the validator client and exist
        in its
        persistent storage.

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no existing
        keystores.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server, DeleteRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return self.sync_detailed(pubkeys=pubkeys).parsed

    async def asyncio_detailed(self, pubkeys: List[str]) -> Response[Union[DeleteRemoteKeysResponse, ErrorResponse]]:
        """Delete Remote Keys (asynchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the validator client and exist
        in its
        persistent storage.

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no existing
        keystores.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and DeleteRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        json_body = DeleteRemoteKeysJsonBody(pubkeys=pubkeys)

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=json_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(self, pubkeys: List[str]) -> Optional[Union[DeleteRemoteKeysResponse, ErrorResponse]]:
        """Delete Remote Keys (asynchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the validator client and exist
        in its
        persistent storage.

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no existing
        keystores.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server, DeleteRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return (await self.asyncio_detailed(pubkeys=pubkeys)).parsed


@attr.s(auto_attribs=True)
class ImportRemoteKeys:
    """Contains methods for accessing the POST method of the /eth/v1/remotekeys endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        remote_keys = [
            {
                "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
                "url": "https://remote.signer",
            }
        ]

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        response = eth_2_key_manager.import_remote_keys.sync_detailed(remote_keys=remote_keys)

        if response.status_code == 200:
            print("Remote keys imported successfully")
        else:
            print(f"Remote keys import failed with status code: {response.status_code}")

        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    ENDPOINT: str = "remotekeys"
    METHOD: str = "POST"

    def sync_detailed(self, remote_keys: List[Dict]) -> Response[Union[ImportRemoteKeysResponse, ErrorResponse]]:
        """Import Remote Keys (synchronous).

        Import remote keys for the validator client to request duties for.

        Args:
            remote_keys: List of remote keys to import. Each item must contain a pubkey and optional remote signer url.
                For example:
                [
                    {
                        "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
                        "url": "https://remote.signer"
                    },
                    {
                        "pubkey": "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d",
                        "url": "https://remote1.signer"
                    }
                ]
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
             Response object containing the response from the server, response headers, status code and ImportKeystoresResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        json_body = ImportRemoteKeysJsonBody(
            remote_keys=[remote_keys_item for remote_keys_item in map(ImportRemoteKeysJsonBodyRemoteKeysItem.from_dict, remote_keys)]  # type: ignore
        )

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=json_body,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=ImportRemoteKeysResponse)

    def sync(self, remote_keys: List[Dict]) -> Optional[Union[ImportRemoteKeysResponse, ErrorResponse]]:
        """Import Remote Keys (synchronous).

        Import remote keys for the validator client to request duties for.

        Args:
            remote_keys: List of remote keys to import. Each item must contain a pubkey and optional remote signer url.
                For example:
                [
                    {
                        "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
                        "url": "https://remote.signer"
                    },
                    {
                        "pubkey": "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d",
                        "url": "https://remote1.signer"
                    }
                ]
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server, ImportRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return self.sync_detailed(remote_keys=remote_keys).parsed

    async def asyncio_detailed(self, remote_keys: List[Dict]) -> Response[Union[ImportRemoteKeysResponse, ErrorResponse]]:
        """Import Remote Keys (asynchronous).

        Import remote keys for the validator client to request duties for.

        Args:
            remote_keys: List of remote keys to import. Each item must contain a pubkey and optional remote signer url.
                For example:
                [
                    {
                        "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
                        "url": "https://remote.signer"
                    },
                    {
                        "pubkey": "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d",
                        "url": "https://remote1.signer"
                    }
                ]
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
             Response object containing the response from the server, response headers, status code and ImportKeystoresResponse object if the request succeeds, otherwise an ErrorResponse object.
        """
        json_body = ImportRemoteKeysJsonBody(
            remote_keys=[remote_keys_item for remote_keys_item in map(ImportRemoteKeysJsonBodyRemoteKeysItem.from_dict, remote_keys)]  # type: ignore
        )

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=json_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(self, remote_keys: List[Dict]) -> Optional[Union[ImportRemoteKeysResponse, ErrorResponse]]:
        """Import Remote Keys (asynchronous).

        Import remote keys for the validator client to request duties for.

        Args:
            remote_keys: List of remote keys to import. Each item must contain a pubkey and optional remote signer url.
                For example:
                [
                    {
                        "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
                        "url": "https://remote.signer"
                    },
                    {
                        "pubkey": "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d",
                        "url": "https://remote1.signer"
                    }
                ]
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server, ImportRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return (await self.asyncio_detailed(remote_keys=remote_keys)).parsed


@attr.s(auto_attribs=True)
class ListRemoteKeys:
    """Contains methods for accessing the GET method of the /eth/v1/remotekeys endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        response = eth_2_key_manager.list_remote_keys.sync_detailed()

        if response.status_code == 200:
            print(f"List of remote keys: {response.parsed.data}")
        else:
            print(f"List remote keys failed with status code: {response.status_code}")

        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    ENDPOINT: str = "remotekeys"
    METHOD: str = "GET"

    def sync_detailed(
        self,
    ) -> Response[Union[ListRemoteKeysResponse, ErrorResponse]]:
        """List Remote Keys (synchronous).

        List all remote validating pubkeys known to this validator client binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and ListRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=self.ENDPOINT, method=self.METHOD)

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=ListRemoteKeysResponse)

    def sync(
        self,
    ) -> Optional[Union[ListRemoteKeysResponse, ErrorResponse]]:
        """List Remote Keys (synchronous).

        List all remote validating pubkeys known to this validator client binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server, ListRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return self.sync_detailed().parsed

    async def asyncio_detailed(
        self,
    ) -> Response[Union[ListRemoteKeysResponse, ErrorResponse]]:
        """List Remote Keys (asynchronous).

        List all remote validating pubkeys known to this validator client binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and ListRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=self.ENDPOINT, method=self.METHOD)

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(
        self,
    ) -> Optional[Union[ListRemoteKeysResponse, ErrorResponse]]:
        """List Remote Keys (asynchronous).

        List all remote validating pubkeys known to this validator client binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server, ListRemoteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return (await self.asyncio_detailed()).parsed
