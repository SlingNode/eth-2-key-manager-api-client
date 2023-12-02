from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SetGasLimitRequest")


@attr.s(auto_attribs=True)
class SetGasLimitRequest:
    """
    Attributes:
        gas_limit (str):  Example: 30000000.
    """

    gas_limit: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gas_limit = self.gas_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gas_limit": gas_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gas_limit = d.pop("gas_limit")

        set_gas_limit_request = cls(
            gas_limit=gas_limit,
        )

        set_gas_limit_request.additional_properties = d
        return set_gas_limit_request

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
