from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from eth_2_key_manager_api_client.types import UNSET, Unset

T = TypeVar("T", bound="ImportKeystoresJsonBody")


@attr.s(auto_attribs=True)
class ImportKeystoresJsonBody:
    """
    Attributes:
        keystores (List[str]): JSON-encoded keystore files generated with the Launchpad.
        passwords (List[str]): Passwords to unlock imported keystore files. `passwords[i]` must unlock `keystores[i]`.
        slashing_protection (Union[Unset, str]): JSON serialized representation of the slash protection data in format
            defined in EIP-3076: Slashing Protection Interchange Format.
             Example: {"metadata":{"interchange_format_version":"5","genesis_validators_root":"0xcf8e0d4e9587369b2301d079034
            7320302cc0943d5a1884560367e8208d920f2"},"data":[{"pubkey":"0x93247f2209abcacf57b75a51dafae777f9dd38ListKeysResponsebc7053d1af526
            f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a","signed_blocks":[],"signed_attestations":[]}]}.
    """

    keystores: List[str]
    passwords: List[str]
    slashing_protection: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keystores = self.keystores

        passwords = self.passwords

        slashing_protection = self.slashing_protection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keystores": keystores,
                "passwords": passwords,
            }
        )
        if slashing_protection is not UNSET:
            field_dict["slashing_protection"] = slashing_protection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keystores = cast(List[str], d.pop("keystores"))

        passwords = cast(List[str], d.pop("passwords"))

        slashing_protection = d.pop("slashing_protection", UNSET)

        import_keystores_json_body = cls(
            keystores=keystores,
            passwords=passwords,
            slashing_protection=slashing_protection,
        )

        import_keystores_json_body.additional_properties = d
        return import_keystores_json_body

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
