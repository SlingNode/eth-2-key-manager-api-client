from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from eth_2_key_manager_api_client.models.import_remote_keys_response_data_item import (
        ImportRemoteKeysResponseDataItem,
    )


T = TypeVar("T", bound="ImportRemoteKeysResponse")


@attr.s(auto_attribs=True)
class ImportRemoteKeysResponse:
    """
    Attributes:
        data (List['ImportRemoteKeysResponseDataItem']): Status result of each `request.remote_keys` with same length
            and order of `request.remote_keys`
    """

    data: List["ImportRemoteKeysResponseDataItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from eth_2_key_manager_api_client.models.import_remote_keys_response_data_item import (
            ImportRemoteKeysResponseDataItem,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ImportRemoteKeysResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        import_remote_keys_response = cls(
            data=data,
        )

        import_remote_keys_response.additional_properties = d
        return import_remote_keys_response

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
