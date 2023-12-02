""" Contains shared error types that can be raised from API functions """


class UnexpectedStatus(Exception):
    """Raised by api functions when the response status an undocumented status and Client.raise_on_unexpected_status is True."""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(f"Unexpected status code: {status_code}")


class ModelClassUnspecified(Exception):
    """Raised by _parse_response when the response status is 200 but no response model is specified."""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(f"Response body received but no response model specified: {status_code}")


class ConfigurationMissing(Exception):
    """Raised by Eth2KeyManager class when base_url or token is not specified."""

    def __init__(self):
        super().__init__(
            "Both base_url and token must be specified. By default ETH_2_KEY_MANAGER_API_BASE_URL and ETH_2_KEY_MANAGER_API_TOKEN environment variables are read. Alternatively specify base_url and token when instantiating Eth2KeyManager class."
        )


__all__ = ["UnexpectedStatus", "ModelClassUnspecified", "ConfigurationMissing"]
