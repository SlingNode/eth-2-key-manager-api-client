from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="ListKeysResponseDataItem")


@attr.s(auto_attribs=True)
class ListKeysResponseDataItem:
    """
    Attributes:
        validating_pubkey (str): The validator's BLS public key, uniquely identifying them. _48-bytes, hex encoded with
            0x prefix, case insensitive._
             Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a.
        derivation_path (Union[Unset, str]): The derivation path (if present in the imported keystore). Example:
            m/12381/3600/0/0/0.
        readonly (Union[Unset, bool]): The key associated with this pubkey cannot be deleted from the API
    """

    validating_pubkey: str
    derivation_path: Union[Unset, str] = UNSET
    readonly: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validating_pubkey = self.validating_pubkey
        derivation_path = self.derivation_path
        readonly = self.readonly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "validating_pubkey": validating_pubkey,
            }
        )
        if derivation_path is not UNSET:
            field_dict["derivation_path"] = derivation_path
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validating_pubkey = d.pop("validating_pubkey")

        derivation_path = d.pop("derivation_path", UNSET)

        readonly = d.pop("readonly", UNSET)

        list_keys_response_data_item = cls(
            validating_pubkey=validating_pubkey,
            derivation_path=derivation_path,
            readonly=readonly,
        )

        list_keys_response_data_item.additional_properties = d
        return list_keys_response_data_item

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
