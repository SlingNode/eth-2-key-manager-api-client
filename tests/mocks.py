mock_response_400 = {
    "code": 400,
    "message": "Bad request. Request was malformed and could not be processed",
    "stacktraces": [],
}
mock_response_401 = {
    "code": 401,
    "message": "UNAUTHORIZED: missing Authorization header",
    "stacktraces": [],
}
mock_response_403 = {
    "code": 403,
    "message": "FORBIDDEN: Invalid auth token: Bearer invalid_token",
    "stacktraces": [],
}
mock_response_500 = {"code": 500, "message": "Internal Server Error", "stacktraces": []}

mock_response_404 = {
    "code": 404,
    "message": "NOT_FOUND: no validator found with pubkey 0x88a471158d618a8f9997dcb2cc1921411392d82d00e339ccf912fd9335bd42f97c9de046280d9d5f681a8e73a7d3baad",
    "stacktraces": [],
}


mock_response_list_remote_keys_200 = {
    "data": [
        {
            "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a",
            "url": "https://remote.signer",
            "readonly": False,
        }
    ]
}
