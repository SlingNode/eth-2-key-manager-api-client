from attr import asdict

from eth_2_key_manager_api_client.client import AuthenticatedClient, Client

# TODO: remove


def test_client():
    c = Client(
        "http://192.168.121.93:7500",
        cookies={"cookie": "chocolate"},
        headers={"header": "value"},
        timeout=10.0,
        verify_ssl=False,
        raise_on_unexpected_status=True,
        follow_redirects=True,
    )

    assert asdict(c) == {
        "base_url": "http://192.168.121.93:7500",
        "cookies": {"cookie": "chocolate"},
        "headers": {"header": "value"},
        "timeout": 10.0,
        "verify_ssl": False,
        "raise_on_unexpected_status": True,
        "follow_redirects": True,
    }

    assert c.get_headers() == {"header": "value"}
    assert c.get_cookies() == {"cookie": "chocolate"}
    assert c.get_timeout() == 10.0
    assert isinstance(c.with_headers({"header2": "value2"}), Client)
    assert c.with_headers({"header2": "value2"}).get_headers() == {"header": "value", "header2": "value2"}
    assert isinstance(c.with_cookies({"cookie2": "chocolate2"}), Client)
    assert c.with_cookies({"cookie2": "chocolate2"}).get_cookies() == {"cookie": "chocolate", "cookie2": "chocolate2"}


def test_authenticated_client():
    ac = AuthenticatedClient("http://192.168.121.93:7500", token="api_token")
    assert ac.get_headers() == {"Authorization": "Bearer api_token"}
