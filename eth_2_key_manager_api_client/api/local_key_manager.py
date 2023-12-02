"""
Provides classes to interact with the set of endpoints for key management of local keys.

API reference: https://ethereum.github.io/keymanager-APIs/#/Local%20Key%20Manager

Each class provides access to a specific endpoint. The classes are organized in the same way as the API documentation.

| Class               | API Endpoint                                          |
|---------------------|-------------------------------------------------------|
| ImportKeystores  | https://ethereum.github.io/keymanager-APIs/#/Local%20Key%20Manager/importKeystores |
| ListKeys    | https://ethereum.github.io/keymanager-APIs/#/Local%20Key%20Manager/listKeys |
| DeleteKeys     | https://ethereum.github.io/keymanager-APIs/#/Local%20Key%20Manager/deleteKeys |
"""
from typing import List, Optional, Union

import attr
import httpx

from eth_2_key_manager_api_client.client import AuthenticatedClient
from eth_2_key_manager_api_client.helpers import _build_response, _get_kwargs
from eth_2_key_manager_api_client.models.delete_keys_json_body import DeleteKeysJsonBody
from eth_2_key_manager_api_client.models.delete_keys_response import DeleteKeysResponse
from eth_2_key_manager_api_client.models.error_response import ErrorResponse
from eth_2_key_manager_api_client.models.import_keystores_json_body import ImportKeystoresJsonBody
from eth_2_key_manager_api_client.models.import_keystores_response import ImportKeystoresResponse
from eth_2_key_manager_api_client.models.list_keys_response import ListKeysResponse
from eth_2_key_manager_api_client.types import UNSET, Response, Unset


@attr.s(auto_attribs=True)
class ImportKeystores:

    """Contains methods for accessing the POST method of the /eth/v1/keystores endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        keystore_str = '''{
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
        }'''

        keystore_password_str = "validatorkey123"

        slashing_protection_str = '''{
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
        }'''

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        response = eth_2_key_manager.import_keystores.sync_detailed([keystore_str], [keystore_password_str], slashing_protection_str)

        if response.status_code == 200:
            print("Keystores imported successfully")
        else:
            print(f"Keystores import failed with status code: {response.status_code}")
        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    ENDPOINT: str = "keystores"
    METHOD: str = "POST"

    def sync_detailed(
        self,
        keystores: List[str],
        passwords: List[str],
        slashing_protection_data: Union[Unset, str] = UNSET,
    ) -> Response[Union[ImportKeystoresResponse, ErrorResponse]]:
        """Import Keystores (synchronous).

        Import keystores generated by the Eth2.0 deposit CLI tooling.

        Users SHOULD send slashing_protection data associated with the imported pubkeys. MUST follow the
        format defined in EIP-3076: Slashing Protection Interchange Format.

        Args:
            keystores: List of keystores (strings) to import.
            passwords: List of passwords to unlock the keystores. `passwords[i]` must unlock `keystores[i]`.
            slashing_protection_data: Slashing protection data as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and ImportKeystoresResponse object if the request succeeds, otherwise an ErrorResponse object.
        """
        import_keystores_body = ImportKeystoresJsonBody(
            keystores=keystores,
            passwords=passwords,
            slashing_protection=slashing_protection_data,
        )

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=import_keystores_body,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=ImportKeystoresResponse)

    def sync(
        self,
        keystores: List[str],
        passwords: List[str],
        slashing_protection_data: Union[Unset, str] = UNSET,
    ) -> Optional[Union[ImportKeystoresResponse, ErrorResponse]]:
        """Import Keystores (synchronous).

        Import keystores generated by the Eth2.0 deposit CLI tooling.

        Users SHOULD send slashing_protection data associated with the imported pubkeys. MUST follow the
        format defined in EIP-3076: Slashing Protection Interchange Format.

        Args:
            keystores: List of keystores (strings) to import.
            passwords: List of passwords to unlock the keystores. `passwords[i]` must unlock `keystores[i]`.
            slashing_protection_data: Slashing protection data as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server. ImportKeystoresResponse if the request succeeds, otherwise ErrorResponse.
        """
        return self.sync_detailed(
            keystores=keystores,
            passwords=passwords,
            slashing_protection_data=slashing_protection_data,
        ).parsed

    async def asyncio_detailed(
        self,
        keystores: List[str],
        passwords: List[str],
        slashing_protection_data: Union[Unset, str] = UNSET,
    ) -> Response[Union[ImportKeystoresResponse, ErrorResponse]]:
        """Import Keystores (asynchronous).

        Import keystores generated by the Eth2.0 deposit CLI tooling.

        Users SHOULD send slashing_protection data associated with the imported pubkeys. MUST follow the
        format defined in EIP-3076: Slashing Protection Interchange Format.

        Args:
            keystores: List of keystores (strings) to import.
            passwords: List of passwords to unlock the keystores. `passwords[i]` must unlock `keystores[i]`.
            slashing_protection_data: Slashing protection data as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and ImportKeystoresResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        import_keystores_body = ImportKeystoresJsonBody(
            keystores=keystores,
            passwords=passwords,
            slashing_protection=slashing_protection_data,
        )

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=import_keystores_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(
        self,
        keystores: List[str],
        passwords: List[str],
        slashing_protection_data: Union[Unset, str] = UNSET,
    ) -> Optional[Union[ImportKeystoresResponse, ErrorResponse]]:
        """Import Keystores (asynchronous).

        Import keystores generated by the Eth2.0 deposit CLI tooling.

        Users SHOULD send slashing_protection data associated with the imported pubkeys. MUST follow the
        format defined in EIP-3076: Slashing Protection Interchange Format.

        Args:
            keystores: List of keystores (strings) to import.
            passwords: List of passwords to unlock the keystores. `passwords[i]` must unlock `keystores[i]`.
            slashing_protection_data: Slashing protection data as string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server. ImportKeystoresResponse if the request succeeds, otherwise ErrorResponse.
        """

        return (
            await self.asyncio_detailed(
                keystores=keystores,
                passwords=passwords,
                slashing_protection_data=slashing_protection_data,
            )
        ).parsed


@attr.s(auto_attribs=True)
class ListKeys:
    """Contains methods for accessing the GET method of the /eth/v1/keystores endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 200: OK

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        response = eth_2_key_manager.list_keys.sync_detailed()

        if response.status_code == 200:
            print(f"List of keys: {response.parsed.data}")
        else:
            print(f"List keys failed with status code: {response.status_code}")
        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    ENDPOINT: str = "keystores"
    METHOD: str = "GET"

    def sync_detailed(
        self,
    ) -> Response[Union[ListKeysResponse, ErrorResponse]]:
        """List Keys (synchronous).

        List all validating pubkeys known to and decrypted by this keymanager binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and ListKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=self.ENDPOINT, method=self.METHOD)

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=ListKeysResponse)

    def sync(
        self,
    ) -> Optional[Union[ListKeysResponse, ErrorResponse]]:
        """List Keys (synchronous).

        List all validating pubkeys known to and decrypted by this keymanager binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server. ListKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """
        return self.sync_detailed().parsed

    async def asyncio_detailed(
        self,
    ) -> Response[Union[ListKeysResponse, ErrorResponse]]:
        """List Keys (asynchronous).

        List all validating pubkeys known to and decrypted by this keymanager binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and ListKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        kwargs = _get_kwargs(client=self.client, endpoint=self.ENDPOINT, method=self.METHOD)

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response, cls=ListKeysResponse)

    async def asyncio(
        self,
    ) -> Optional[Union[ListKeysResponse, ErrorResponse]]:
        """List Keys (asynchronous).

        List all validating pubkeys known to and decrypted by this keymanager binary

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server. ListKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """
        return (await self.asyncio_detailed()).parsed


@attr.s(auto_attribs=True)
class DeleteKeys:

    """Contains methods for accessing the POST method of the /eth/v1/keystores endpoint.

    The endpoint returns the following HTTP status code if successful:
        - 204: No Content

    Typical usage example:
        ```python
        import eth_2_key_manager_api_client

        eth_2_key_manager = eth_2_key_manager_api_client.Eth2KeyManager()
        pubkey = "0x99c4c42fac7d1393956bd9e2785ed67cf5aaca4bf56d2fcda94c42d6042aebb1723ce6bac6f0216ff8c5d4f9f013008b"

        response = eth_2_key_manager.delete_keys.sync_detailed(pubkeys=[pubkey])
        if response.status_code == 200:
            print("Keystores deleted successfully")
        else:
            print(f"Keystores delete failed with status code: {response.status_code}")
        assert response.status_code == 200
        ```
    """

    client: AuthenticatedClient
    ENDPOINT: str = "keystores"
    METHOD: str = "DELETE"

    def sync_detailed(
        self,
        pubkeys: List[str],
    ) -> Response[Union[DeleteKeysResponse, ErrorResponse]]:
        """Delete Keys (synchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the keymanager and exist in its
        persistent storage. Additionally, DELETE must fetch the slashing protection data for the requested
        keys from persistent storage, which must be retained (and not deleted) after the response has been sent.
        Therefore in the case of two identical delete requests being made, both will have access to slashing protection data.

        In a single atomic sequential operation the keymanager must:
        1. Guarantee that key(s) can not produce any more signature; only then
        2. Delete key(s) and serialize its associated slashing protection data

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no extant
        keystores nor slashing protection data.

        Slashing protection data must only be returned for keys from `request.pubkeys` for which a
        `deleted` or `not_active` status is returned.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and DeleteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        delete_keys_body = DeleteKeysJsonBody(pubkeys=pubkeys)

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=delete_keys_body,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )

        return _build_response(client=self.client, response=response, cls=DeleteKeysResponse)

    def sync(
        self,
        pubkeys: List[str],
    ) -> Optional[Union[DeleteKeysResponse, ErrorResponse]]:
        """Delete Keys (synchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the keymanager and exist in its
        persistent storage. Additionally, DELETE must fetch the slashing protection data for the requested
        keys from persistent storage, which must be retained (and not deleted) after the response has been sent.
        Therefore in the case of two identical delete requests being made, both will have access to slashing protection data.

        In a single atomic sequential operation the keymanager must:
        1. Guarantee that key(s) can not produce any more signature; only then
        2. Delete key(s) and serialize its associated slashing protection data

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no extant
        keystores nor slashing protection data.

        Slashing protection data must only be returned for keys from `request.pubkeys` for which a
        `deleted` or `not_active` status is returned.

        Args:
            pubkeys: List of public keys to delete.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server. DeleteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return self.sync_detailed(
            pubkeys=pubkeys,
        ).parsed

    async def asyncio_detailed(
        self,
        pubkeys: List[str],
    ) -> Response[Union[DeleteKeysResponse, ErrorResponse]]:
        """Delete Keys (asynchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the keymanager and exist in its
        persistent storage. Additionally, DELETE must fetch the slashing protection data for the requested
        keys from persistent storage, which must be retained (and not deleted) after the response has been sent.
        Therefore in the case of two identical delete requests being made, both will have access to slashing protection data.

        In a single atomic sequential operation the keymanager must:
        1. Guarantee that key(s) can not produce any more signature; only then
        2. Delete key(s) and serialize its associated slashing protection data

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no extant
        keystores nor slashing protection data.

        Slashing protection data must only be returned for keys from `request.pubkeys` for which a
        `deleted` or `not_active` status is returned.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response object containing the response from the server, response headers, status code and DeleteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        delete_keys_body = DeleteKeysJsonBody(pubkeys=pubkeys)

        kwargs = _get_kwargs(
            client=self.client,
            endpoint=self.ENDPOINT,
            method=self.METHOD,
            json_body=delete_keys_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)

        return _build_response(client=self.client, response=response)

    async def asyncio(
        self,
        pubkeys: List[str],
    ) -> Optional[Union[DeleteKeysResponse, ErrorResponse]]:
        """Delete Keys (asynchronous).

        DELETE must delete all keys from `request.pubkeys` that are known to the keymanager and exist in its
        persistent storage. Additionally, DELETE must fetch the slashing protection data for the requested
        keys from persistent storage, which must be retained (and not deleted) after the response has been sent.
        Therefore in the case of two identical delete requests being made, both will have access to slashing protection data.

        In a single atomic sequential operation the keymanager must:
        1. Guarantee that key(s) can not produce any more signature; only then
        2. Delete key(s) and serialize its associated slashing protection data

        DELETE should never return a 404 response, even if all pubkeys from request.pubkeys have no extant
        keystores nor slashing protection data.

        Slashing protection data must only be returned for keys from `request.pubkeys` for which a
        `deleted` or `not_active` status is returned.

        Args:
            pubkeys: List of public keys to delete.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Parsed response from the server. DeleteKeysResponse object if the request succeeds, otherwise an ErrorResponse object.
        """

        return (
            await self.asyncio_detailed(
                pubkeys=pubkeys,
            )
        ).parsed
