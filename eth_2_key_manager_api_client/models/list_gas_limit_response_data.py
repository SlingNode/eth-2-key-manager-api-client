from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="ListGasLimitResponseData")


@attr.s(auto_attribs=True)
class ListGasLimitResponseData:
    """
    Attributes:
        gas_limit (str):  Example: 30000000.
        pubkey (Union[Unset, str]): The validator's BLS public key, uniquely identifying them. _48-bytes, hex encoded
            with 0x prefix, case insensitive._
             Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a.
    """

    gas_limit: str
    pubkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gas_limit = self.gas_limit
        pubkey = self.pubkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gas_limit": gas_limit,
            }
        )
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gas_limit = d.pop("gas_limit")

        pubkey = d.pop("pubkey", UNSET)

        list_gas_limit_response_data = cls(
            gas_limit=gas_limit,
            pubkey=pubkey,
        )

        list_gas_limit_response_data.additional_properties = d
        return list_gas_limit_response_data

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
