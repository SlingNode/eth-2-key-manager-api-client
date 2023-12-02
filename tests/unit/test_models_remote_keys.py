from typing import Dict, List

from eth_2_key_manager_api_client.models.import_remote_keys_json_body import ImportRemoteKeysJsonBody
from eth_2_key_manager_api_client.models.import_remote_keys_json_body_remote_keys_item import (
    ImportRemoteKeysJsonBodyRemoteKeysItem,
)


def test_import_remote_keys_json_body_rempote_keys_item():
    import_remote_keys_json_body_remote_keys_item = ImportRemoteKeysJsonBodyRemoteKeysItem(
        pubkey="0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
        url="https://remote.signer",
    )

    assert (
        import_remote_keys_json_body_remote_keys_item.pubkey
        == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    )
    assert import_remote_keys_json_body_remote_keys_item.url == "https://remote.signer"


def test_import_remote_keys_json_body_rempote_keys_item_from_dict():
    import_remote_keys_json_body_remote_keys_item = ImportRemoteKeysJsonBodyRemoteKeysItem.from_dict(
        {
            "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
            "url": "https://remote.signer",
        }
    )

    assert (
        import_remote_keys_json_body_remote_keys_item.pubkey
        == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    )
    assert import_remote_keys_json_body_remote_keys_item.url == "https://remote.signer"


def test_import_remote_keys_json_body():
    import_remote_keys_json_body = ImportRemoteKeysJsonBody(
        remote_keys=[
            ImportRemoteKeysJsonBodyRemoteKeysItem(
                pubkey="0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
                url="https://remote.signer",
            )
        ]
    )

    assert len(import_remote_keys_json_body.remote_keys) == 1
    assert (
        import_remote_keys_json_body.remote_keys[0].pubkey
        == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    )
    assert import_remote_keys_json_body.remote_keys[0].url == "https://remote.signer"


def test_import_remote_keys_json_body_multiple_keys():

    remote_keys: List[Dict] = [
        {"pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a", "url": "https://remote1.signer"},
        {"pubkey": "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d", "url": "https://remote2.signer"},
    ]

    import_remote_keys_json_body = ImportRemoteKeysJsonBody(
        remote_keys=[remote_keys_item for remote_keys_item in map(ImportRemoteKeysJsonBodyRemoteKeysItem.from_dict, remote_keys)]
    )

    assert len(import_remote_keys_json_body.remote_keys) == 2
    assert (
        import_remote_keys_json_body.remote_keys[0].pubkey
        == "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    )
    assert import_remote_keys_json_body.remote_keys[0].url == "https://remote1.signer"
    assert (
        import_remote_keys_json_body.remote_keys[1].pubkey
        == "0x874bed7931ba14832198a4070b881f89e7ddf81898dd800446ef382344e9726a5e6265acb21f5c8ee2759c313ec6ca0d"
    )
    assert import_remote_keys_json_body.remote_keys[1].url == "https://remote2.signer"
