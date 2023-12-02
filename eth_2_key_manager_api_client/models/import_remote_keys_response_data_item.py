from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from eth_2_key_manager_api_client.models.import_remote_keys_response_data_item_status import (
    ImportRemoteKeysResponseDataItemStatus,
)
from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="ImportRemoteKeysResponseDataItem")


@attr.s(auto_attribs=True)
class ImportRemoteKeysResponseDataItem:
    """
    Attributes:
        status (ImportRemoteKeysResponseDataItemStatus): - imported: Remote key successfully imported to validator
            client permanent storage
            - duplicate: Remote key's pubkey is already known to the validator client
            - error: Any other status different to the above: I/O errors, etc.
             Example: imported.
        message (Union[Unset, str]): error message if status == error
    """

    status: ImportRemoteKeysResponseDataItemStatus
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = ImportRemoteKeysResponseDataItemStatus(d.pop("status"))

        message = d.pop("message", UNSET)

        import_remote_keys_response_data_item = cls(
            status=status,
            message=message,
        )

        import_remote_keys_response_data_item.additional_properties = d
        return import_remote_keys_response_data_item

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
