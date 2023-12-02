from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from eth_2_key_manager_api_client.models.import_remote_keys_json_body_remote_keys_item import (
        ImportRemoteKeysJsonBodyRemoteKeysItem,
    )


T = TypeVar("T", bound="ImportRemoteKeysJsonBody")


@attr.s(auto_attribs=True)
class ImportRemoteKeysJsonBody:
    """
    Attributes:
        remote_keys (List['ImportRemoteKeysJsonBodyRemoteKeysItem']):
    """

    remote_keys: List["ImportRemoteKeysJsonBodyRemoteKeysItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remote_keys = []
        for remote_keys_item_data in self.remote_keys:
            remote_keys_item = remote_keys_item_data.to_dict()

            remote_keys.append(remote_keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remote_keys": remote_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from eth_2_key_manager_api_client.models.import_remote_keys_json_body_remote_keys_item import (
            ImportRemoteKeysJsonBodyRemoteKeysItem,
        )

        d = src_dict.copy()
        remote_keys = []
        _remote_keys = d.pop("remote_keys")
        for remote_keys_item_data in _remote_keys:
            remote_keys_item = ImportRemoteKeysJsonBodyRemoteKeysItem.from_dict(remote_keys_item_data)

            remote_keys.append(remote_keys_item)

        import_remote_keys_json_body = cls(
            remote_keys=remote_keys,
        )

        import_remote_keys_json_body.additional_properties = d
        return import_remote_keys_json_body

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
