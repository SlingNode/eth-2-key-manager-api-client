from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="SignerDefinition")


@attr.s(auto_attribs=True)
class SignerDefinition:
    """
    Attributes:
        pubkey (str): The validator's BLS public key, uniquely identifying them. _48-bytes, hex encoded with 0x prefix,
            case insensitive._
             Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a.
        url (Union[Unset, str]): URL to API implementing EIP-3030: BLS Remote Signer HTTP API Example:
            https://remote.signer.
        readonly (Union[Unset, bool]): The signer associated with this pubkey cannot be deleted from the API
    """

    pubkey: str
    url: Union[Unset, str] = UNSET
    readonly: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pubkey = self.pubkey
        url = self.url
        readonly = self.readonly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pubkey": pubkey,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pubkey = d.pop("pubkey")

        url = d.pop("url", UNSET)

        readonly = d.pop("readonly", UNSET)

        signer_definition = cls(
            pubkey=pubkey,
            url=url,
            readonly=readonly,
        )

        signer_definition.additional_properties = d
        return signer_definition

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
