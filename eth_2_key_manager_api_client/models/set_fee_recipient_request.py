from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SetFeeRecipientRequest")


@attr.s(auto_attribs=True)
class SetFeeRecipientRequest:
    """
    Attributes:
        ethaddress (str): An address on the execution (Ethereum 1) network. Example:
            0xabcf8e0d4e9587369b2301d0790347320302cc09.
    """

    ethaddress: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ethaddress = self.ethaddress

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ethaddress": ethaddress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ethaddress = d.pop("ethaddress")

        set_fee_recipient_request = cls(
            ethaddress=ethaddress,
        )

        set_fee_recipient_request.additional_properties = d
        return set_fee_recipient_request

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
