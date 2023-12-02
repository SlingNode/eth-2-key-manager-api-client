from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from eth_2_key_manager_api_client.models.delete_keys_response_data_item import DeleteKeysResponseDataItem


T = TypeVar("T", bound="DeleteKeysResponse")


@attr.s(auto_attribs=True)
class DeleteKeysResponse:
    """
    Attributes:
        data (List['DeleteKeysResponseDataItem']): Deletion status of all keys in `request.pubkeys` in the same order.
        slashing_protection (str): JSON serialized representation of the slash protection data in format defined in
            EIP-3076: Slashing Protection Interchange Format.
             Example: {"metadata":{"interchange_format_version":"5","genesis_validators_root":"0xcf8e0d4e9587369b2301d079034
            7320302cc0943d5a1884560367e8208d920f2"},"data":[{"pubkey":"0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526
            f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a","signed_blocks":[],"signed_attestations":[]}]}.
    """

    data: List["DeleteKeysResponseDataItem"]
    slashing_protection: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        slashing_protection = self.slashing_protection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "slashing_protection": slashing_protection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from eth_2_key_manager_api_client.models.delete_keys_response_data_item import DeleteKeysResponseDataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = DeleteKeysResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        slashing_protection = d.pop("slashing_protection")

        delete_keys_response = cls(
            data=data,
            slashing_protection=slashing_protection,
        )

        delete_keys_response.additional_properties = d
        return delete_keys_response

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
