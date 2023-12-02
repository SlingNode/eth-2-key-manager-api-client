from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from eth_2_key_manager_api_client.models.delete_remote_keys_response_data_item_status import (
    DeleteRemoteKeysResponseDataItemStatus,
)
from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="DeleteRemoteKeysResponseDataItem")


@attr.s(auto_attribs=True)
class DeleteRemoteKeysResponseDataItem:
    """
    Attributes:
        status (DeleteRemoteKeysResponseDataItemStatus): - deleted: key was active and removed
            - not_found: key was not found to be removed
            - error: unexpected condition meant the key could not be removed (the key was actually found,
              but we couldn't stop using it) - this would be a sign that making it active elsewhere would
              almost certainly cause you headaches / slashing conditions etc.
             Example: deleted.
        message (Union[Unset, str]): error message if status == error
    """

    status: DeleteRemoteKeysResponseDataItemStatus
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
        status = DeleteRemoteKeysResponseDataItemStatus(d.pop("status"))

        message = d.pop("message", UNSET)

        delete_remote_keys_response_data_item = cls(
            status=status,
            message=message,
        )

        delete_remote_keys_response_data_item.additional_properties = d
        return delete_remote_keys_response_data_item

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
