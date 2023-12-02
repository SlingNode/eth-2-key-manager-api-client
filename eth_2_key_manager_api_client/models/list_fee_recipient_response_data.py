from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="ListFeeRecipientResponseData")


@attr.s(auto_attribs=True)
class ListFeeRecipientResponseData:
    """
    Attributes:
        ethaddress (str): An address on the execution (Ethereum 1) network. Example:
            0xabcf8e0d4e9587369b2301d0790347320302cc09.
        pubkey (Union[Unset, str]): The validator's BLS public key, uniquely identifying them. _48-bytes, hex encoded
            with 0x prefix, case insensitive._
             Example: 0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a.
    """

    ethaddress: str
    pubkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ethaddress = self.ethaddress
        pubkey = self.pubkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ethaddress": ethaddress,
            }
        )
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ethaddress = d.pop("ethaddress")

        pubkey = d.pop("pubkey", UNSET)

        list_fee_recipient_response_data = cls(
            ethaddress=ethaddress,
            pubkey=pubkey,
        )

        list_fee_recipient_response_data.additional_properties = d
        return list_fee_recipient_response_data

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
