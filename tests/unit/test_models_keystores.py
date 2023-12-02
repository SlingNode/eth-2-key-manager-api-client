# tests for models
from eth_2_key_manager_api_client.models.delete_keys_json_body import DeleteKeysJsonBody
from eth_2_key_manager_api_client.models.import_keystores_json_body import ImportKeystoresJsonBody


def test_delete_keys_json_body():
    """Test DeleteKeysJsonBody"""

    test_dict = {
        "pubkeys": ["0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d"],
    }

    delete_keys_json_body = DeleteKeysJsonBody.from_dict(test_dict)

    assert delete_keys_json_body.pubkeys == ["0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d"]

    assert delete_keys_json_body.to_dict() == test_dict


def test_import_keystores_json_body(keystore_str, keystore_password_str, slashing_protection_str):
    """Test case for ImportKeystoresJsonBody"""
    # From eth-2-key-manager-api-client/eth_2_key_manager_api_client/models/import_keystores_json_body.py:ImportKeystoresJsonBody.from_dict

    src_dict = {
        "keystores": [keystore_str],
        "passwords": [keystore_password_str],
        "slashing_protection": slashing_protection_str,
    }
    import_keystores_json_body = ImportKeystoresJsonBody.from_dict(src_dict)

    assert import_keystores_json_body.keystores == [keystore_str]
    assert import_keystores_json_body.passwords == [keystore_password_str]
    assert import_keystores_json_body.slashing_protection == slashing_protection_str

    assert import_keystores_json_body.to_dict() == src_dict
