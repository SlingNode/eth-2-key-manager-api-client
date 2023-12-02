"""
Provides classes to interact with the set of endpoints for management of gas limits.

API reference: https://ethereum.github.io/keymanager-APIs/#/Gas%20Limit

Each class provides access to a specific endpoint. The classes are organized in the same way as the API documentation.

| Class         | API Endpoint                                          |
|---------------|-------------------------------------------------------|
| DeleteGasLimit| https://ethereum.github.io/keymanager-APIs/#/Gas%20Limit/deleteGasLimit |
| GetGasLimit   | https://ethereum.github.io/keymanager-APIs/#/Gas%20Limit/getGasLimit|
| SetGasLimit   | https://ethereum.github.io/keymanager-APIs/#/Gas%20Limit/setGasLimit |
"""
from typing import Any, Optional, Union

import attr
import httpx

from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.helpers import _build_response, _get_kwargs
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.list_gas_limit_response import ListGasLimitResponse
from eth_2_key_manager_api_client.models.set_gas_limit_request import SetGasLimitRequest
from eth_2_key_manager_api_client.types import Response


@attr.s(auto_attribs=True)
class DeleteGasLimit:
    """Contains methods for accessing the DELETE method of the /eth/v1/validator/{pubkey}/gas_limit endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 204: No Content

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
        response = eth_2_key_manager.delete_gas_limit.sync_detailed(pubkey=pubkey)
        if response.status_code == 204:
            print("Gas limit deleted successfully")
        else:
            print(f"Gas limit deletion failed with status code: {response.status_code}")
        assert response.status_code == 204
        ```
    """

    client: AuthenticatedClient
    METHOD: str = "DELETE"

    def sync_detailed(
        self,
        pubkey: str,
    ) -> Response[Union[Any, ErrorResponse]]:
        """Delete Configured Gas Limit (synchronous).

        Delete a configured gas limit for the specified public key.

        The server may return a 400 status code if no external builder is configured.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/gas_limit", method=self.METHOD)

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response)

    def sync(
        self,
        pubkey: str,
    ) -> Optional[Union[Any, ErrorResponse]]:
        """Delete Configured Gas Limit (synchronous).

        Delete a configured gas limit for the specified public key.

        The server may return a 400 status code if no external builder is configured.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server.
        """

        return self.sync_detailed(pubkey=pubkey).parsed

    async def asyncio_detailed(
        self,
        pubkey: str,
    ) -> Response[Union[Any, ErrorResponse]]:
        """Delete Configured Gas Limit (asynchronous).

        Delete a configured gas limit for the specified public key.

        The server may return a 400 status code if no external builder is configured.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/gas_limit", method=self.METHOD)

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(
        self,
        pubkey: str,
    ) -> Optional[Union[Any, ErrorResponse]]:
        """Delete Configured Gas Limit (asynchronous).

        Delete a configured gas limit for the specified public key.

        The server may return a 400 status code if no external builder is configured.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server.
        """

        return (await self.asyncio_detailed(pubkey=pubkey)).parsed


@attr.s(auto_attribs=True)
class GetGasLimit:

    """Contains methods for accessing the GET method of the /eth/v1/validator/{pubkey}/gas_limit endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
        response = eth_2_key_manager.get_gas_limit.sync_detailed(pubkey=pubkey)
        if response.status_code == 200:
            print(f"Gas limit for pubkey {pubkey} is {response.parsed.data.gas_limit}")
        else:
            print(f"Gas limit listing failed with status code: {response.status_code}")
        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    METHOD: str = "GET"

    def sync_detailed(
        self,
        pubkey: str,
    ) -> Response[Union[ErrorResponse, ListGasLimitResponse]]:
        """Get Gas Limit (synchronous).

        Get the execution gas limit for an individual validator. This gas limit is the one used by the
        validator when proposing blocks via an external builder. If no limit has been set explicitly for
        a key then the process-wide default will be returned.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/gas_limit", method=self.METHOD)

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=ListGasLimitResponse)

    def sync(
        self,
        pubkey: str,
    ) -> Optional[Union[ErrorResponse, ListGasLimitResponse]]:
        """Get Gas Limit (synchronous).

        Get the execution gas limit for an individual validator. This gas limit is the one used by the
        validator when proposing blocks via an external builder. If no limit has been set explicitly for
        a key then the process-wide default will be returned.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server.
        """

        return self.sync_detailed(
            pubkey=pubkey,
        ).parsed

    async def asyncio_detailed(
        self,
        pubkey: str,
    ) -> Response[Union[ErrorResponse, ListGasLimitResponse]]:
        """Get Gas Limit (asynchronous).

        Get the execution gas limit for an individual validator. This gas limit is the one used by the
        validator when proposing blocks via an external builder. If no limit has been set explicitly for
        a key then the process-wide default will be returned.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/gas_limit", method=self.METHOD)

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(
        self,
        pubkey: str,
    ) -> Optional[Union[ErrorResponse, ListGasLimitResponse]]:
        """Get Gas Limit (asynchronous).

        Get the execution gas limit for an individual validator. This gas limit is the one used by the
        validator when proposing blocks via an external builder. If no limit has been set explicitly for
        a key then the process-wide default will be returned.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server.
        """

        return (await self.asyncio_detailed(pubkey=pubkey)).parsed


@attr.s(auto_attribs=True)
class SetGasLimit:
    """Contains methods for accessing the POST method of the /eth/v1/validator/{pubkey}/gas_limit endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 202: Accepted

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
        response = eth_2_key_manager.set_gas_limit.sync_detailed(pubkey=pubkey, gas_limit="999999")
        if response.status_code == 202:
            print("Gas limit set successfully")
        else:
            print(f"Gas limit set failed with status code: {response.status_code}")
        assert response.status_code == 202
        ```
    """

    client: AuthenticatedClient
    METHOD: str = "POST"

    def sync_detailed(self, pubkey: str, gas_limit: str) -> Response[Union[Any, ErrorResponse]]:
        """Set Gas Limit (synchronous).

        Set the gas limit for an individual validator. This limit will be propagated to the beacon
        node for use on future block proposals. The beacon node is responsible for informing external
        block builders of the change.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            gas_limit: The gas limit to set for the validator as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        json_body = SetGasLimitRequest(gas_limit=gas_limit)

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=f"validator/{pubkey}/gas_limit",
            method=self.METHOD,
            json_body=json_body,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response)

    def sync(self, pubkey: str, gas_limit: str) -> Optional[Union[Any, ErrorResponse]]:
        """Set Gas Limit (synchronous).

        Set the gas limit for an individual validator. This limit will be propagated to the beacon
        node for use on future block proposals. The beacon node is responsible for informing external
        block builders of the change.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            gas_limit: The gas limit to set for the validator as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server.
        """

        return self.sync_detailed(pubkey=pubkey, gas_limit=gas_limit).parsed

    async def asyncio_detailed(self, pubkey: str, gas_limit: str) -> Response[Union[Any, ErrorResponse]]:
        """Set Gas Limit (asynchronous).

        Set the gas limit for an individual validator. This limit will be propagated to the beacon
        node for use on future block proposals. The beacon node is responsible for informing external
        block builders of the change.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            gas_limit: The gas limit to set for the validator as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        json_body = SetGasLimitRequest(gas_limit=gas_limit)

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=f"validator/{pubkey}/gas_limit",
            method=self.METHOD,
            json_body=json_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(self, pubkey: str, gas_limit: str) -> Optional[Union[Any, ErrorResponse]]:
        """Set Gas Limit (asynchronous).

        Set the gas limit for an individual validator. This limit will be propagated to the beacon
        node for use on future block proposals. The beacon node is responsible for informing external
        block builders of the change.

        The server may return a 400 status code if no external builder is configured.

        WARNING: The gas_limit is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            gas_limit: The gas limit to set for the validator as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server.
        """

        return (await self.asyncio_detailed(pubkey=pubkey, gas_limit=gas_limit)).parsed
