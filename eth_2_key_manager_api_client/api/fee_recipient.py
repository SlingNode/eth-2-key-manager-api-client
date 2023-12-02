"""
Provides classes to interact with the set of endpoints for management of fee recipient.

API reference: https://ethereum.github.io/keymanager-APIs/#/Fee%20Recipient

Each class provides access to a specific endpoint. The classes are organized in the same way as the API documentation.

| Class               | API Endpoint                                          |
|---------------------|-------------------------------------------------------|
| DeleteFeeRecipient  | https://ethereum.github.io/keymanager-APIs/#/Fee%20Recipient/deleteFeeRecipient |
| ListFeeRecipient    | https://ethereum.github.io/keymanager-APIs/#/Fee%20Recipient/listFeeRecipient |
| SetFeeRecipient     | https://ethereum.github.io/keymanager-APIs/#/Fee%20Recipient/setFeeRecipient |
"""
from typing import Any, Optional, Union

import attr
import httpx

from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.helpers import _build_response, _get_kwargs
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.list_fee_recipient_response import ListFeeRecipientResponse
from eth_2_key_manager_api_client.models.set_fee_recipient_request import SetFeeRecipientRequest
from eth_2_key_manager_api_client.types import Response


@attr.s(auto_attribs=True)
class DeleteFeeRecipient:
    """Contains methods for accessing the DELETE method of the /eth/v1/validator/{pubkey}/feerecipient endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 204: No Content

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
        response = eth_2_key_manager.delete_fee_recipient.sync_detailed(pubkey=pubkey)
        if response.status_code == 204:
            print("Fee Recipient deleted successfully")
        else:
            print(f"Fee Recipient deletion failed with status code: {response.status_code}")
        assert response.status_code == 204
        ```
    """

    client: AuthenticatedClient
    METHOD: str = "DELETE"

    def sync_detailed(
        self,
        pubkey: str,
    ) -> httpx.Response:
        """Delete configured Fee Recipient (synchronous).

        Delete a configured fee recipient mapping for the specified public key.

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

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=f"validator/{pubkey}/feerecipient",
            method=self.METHOD,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response)

    def sync(
        self,
        pubkey: str,
    ) -> Optional[Union[Any, ErrorResponse]]:
        """Delete configured Fee Recipient (synchronous).

        Delete a configured fee recipient mapping for the specified public key.

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

    async def asyncio_detailed(self, pubkey: str) -> Response[Union[Any, ErrorResponse]]:
        """Delete configured Fee Recipient (asynchronous).

        Delete a configured fee recipient mapping for the specified public key.

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

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=f"validator/{pubkey}/feerecipient",
            method=self.METHOD,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(self, pubkey: str) -> Optional[Union[Any, ErrorResponse]]:
        """Delete configured Fee Recipient (asynchronous).

        Delete a configured fee recipient mapping for the specified public key.

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
class ListFeeRecipient:
    """Contains methods for accessing the GET method of the /eth/v1/validator/{pubkey}/feerecipient endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
        response = eth_2_key_manager.list_fee_recipient.sync_detailed(pubkey=pubkey)
        if response.status_code == 200:
            print(f"Fee recipient for pubkey {pubkey} is {response.parsed.data.ethaddress}")
        else:
            print(f"Fee Recipient listing failed with status code: {response.status_code}")
        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    METHOD: str = "GET"

    def sync_detailed(
        self,
        pubkey: str,
    ) -> Response[Union[ListFeeRecipientResponse, ErrorResponse]]:
        """List Fee Recipient (synchronous).

        List the validator public key to eth address mapping for fee recipient feature on a specific public
        key.
        The validator public key will return with the default fee recipient address if a specific one was
        not found.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

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

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=f"validator/{pubkey}/feerecipient",
            method=self.METHOD,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=ListFeeRecipientResponse)

    def sync(
        self,
        pubkey: str,
    ) -> Optional[Union[ListFeeRecipientResponse, ErrorResponse]]:
        """List Fee Recipient (synchronous).

            List the validator public key to eth address mapping for fee recipient feature on a specific public
        key.
        The validator public key will return with the default fee recipient address if a specific one was
        not found.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

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

    async def asyncio_detailed(self, pubkey: str) -> Response[Union[ListFeeRecipientResponse, ErrorResponse]]:
        """List Fee Recipient (asynchronous).

        List the validator public key to eth address mapping for fee recipient feature on a specific public
        key.
        The validator public key will return with the default fee recipient address if a specific one was
        not found.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

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

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/feerecipient", method=self.METHOD)

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(self, pubkey: str) -> Optional[Union[ListFeeRecipientResponse, ErrorResponse]]:
        """List Fee Recipient (asynchronous).

        List the validator public key to eth address mapping for fee recipient feature on a specific public
        key.
        The validator public key will return with the default fee recipient address if a specific one was
        not found.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

        Args:
            pubkey (str): The validator's BLS public key, uniquely identifying them. _48-bytes, hex
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
class SetFeeRecipient:
    """Contains methods for accessing the POST method of the /eth/v1/validator/{pubkey}/feerecipient endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 202: Accepted

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"
        response = eth_2_key_manager.set_fee_recipient.sync_detailed(pubkey=pubkey, ethaddress="0xabcf8e0d4e9587369b2301d0790347320302cc09")
        if response.status_code == 202:
            print("Fee Recipient set successfully")
        else:
            print(f"Fee Recipient set failed with status code: {response.status_code}")
        assert response.status_code == 202
        ```
    """

    client: AuthenticatedClient
    METHOD: str = "POST"

    def sync_detailed(self, pubkey: str, ethaddress: str) -> Response[Union[Any, ErrorResponse]]:
        """Set Fee Recipient (synchronous).

        Sets the validator client fee recipient mapping which will then update the beacon node.
        Existing mappings for the same validator public key will be overwritten.
        Specific Public keys not mapped will continue to use the default address for fee recipient in
        accordance to the startup of the validator client and beacon node.
        Cannot specify the 0x00 fee recipient address through the API.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            ethaddress: The fee recipient address to set for the validator.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        set_fee_recipient_body = SetFeeRecipientRequest(ethaddress=ethaddress)

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/feerecipient", method=self.METHOD, json_body=set_fee_recipient_body)

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response)

    def sync(self, pubkey: str, ethaddress: str) -> Optional[Union[Any, ErrorResponse]]:
        """Set Fee Recipient (synchronous).

        Sets the validator client fee recipient mapping which will then update the beacon node.
        Existing mappings for the same validator public key will be overwritten.
        Specific Public keys not mapped will continue to use the default address for fee recipient in
        accordance to the startup of the validator client and beacon node.
        Cannot specify the 0x00 fee recipient address through the API.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            ethaddress: The fee recipient address to set for the validator.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Returns parsed response from the server.
        """

        return self.sync_detailed(pubkey=pubkey, ethaddress=ethaddress).parsed

    async def asyncio_detailed(self, pubkey: str, ethaddress: str) -> Response[Union[Any, ErrorResponse]]:
        """Set Fee Recipient (asynchronous).

        Sets the validator client fee recipient mapping which will then update the beacon node.
        Existing mappings for the same validator public key will be overwritten.
        Specific Public keys not mapped will continue to use the default address for fee recipient in
        accordance to the startup of the validator client and beacon node.
        Cannot specify the 0x00 fee recipient address through the API.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            ethaddress: The fee recipient address to set for the validator.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers and status code.
        """

        set_fee_recipient_body = SetFeeRecipientRequest(ethaddress=ethaddress)

        kwargs = _get_kwargs(client=self.client, endpoint=f"validator/{pubkey}/feerecipient", method=self.METHOD, json_body=set_fee_recipient_body)

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(self, pubkey: str, ethaddress: str) -> Optional[Union[Any, ErrorResponse]]:
        """Set Fee Recipient (asynchronous).

        Sets the validator client fee recipient mapping which will then update the beacon node.
        Existing mappings for the same validator public key will be overwritten.
        Specific Public keys not mapped will continue to use the default address for fee recipient in
        accordance to the startup of the validator client and beacon node.
        Cannot specify the 0x00 fee recipient address through the API.

        WARNING: The fee_recipient is not used on Phase0 or Altair networks.

        Args:
            pubkey: The validator's BLS public key, uniquely identifying them. _48-bytes, hex
                encoded with 0x prefix, case insensitive._
                Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1c
                fe39b56f43611df74a.
            ethaddress: The fee recipient address to set for the validator.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Returns parsed response from the server.
        """

        return (await self.asyncio_detailed(pubkey=pubkey, ethaddress=ethaddress)).parsed
