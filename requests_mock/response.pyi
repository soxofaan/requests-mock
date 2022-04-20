# Stubs for requests_mock.response

from typing import Any, Dict, Optional

import six

from requests import Request, Response
from requests.cookies import RequestsCookieJar

class CookieJar(RequestsCookieJar):
    def set(self, name: Any, value: Any, **kwargs: Any) -> Any: ...

class _FakeConnection:
    def send(self, request: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...

class _IOReader(six.BytesIO):
    def read(self, *args: Any, **kwargs: Any) -> Any: ...

def create_response(request: Any, **kwargs: Any) -> Response: ...

class _Context:
    headers: Dict[str,str] = ...
    status_code: int = ...
    reason: str = ...
    cookies: Any = ...

    def __init__(self,
                 headers: Dict[str, str],
                 status_code: int,
                 reason: str,
                 cookies: Any) -> None: ...

class _MatcherResponse:
    def __init__(self, **kwargs: Any) -> None: ...
    def get_response(self, request: Request) -> Response: ...
