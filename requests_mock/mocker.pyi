# Stubs for requests_mock.mocker

from http.cookiejar import CookieJar
from io import IOBase
from typing import Any, Callable, Dict, List, Optional, Pattern, Type, TypeVar, Union

from requests import Response
from requests.packages.urllib3.response import HTTPResponse

from requests_mock.adapter import AnyMatcher
from requests_mock.request import _RequestObjectProxy
from requests_mock.response import _Context

DELETE: str
GET: str
HEAD: str
OPTIONS: str
PATCH: str
POST: str
PUT: str

class MockerCore:
    case_sensitive: bool = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_matcher(self, matcher: Any) -> None: ...
    @property
    def request_history(self) -> List[_RequestObjectProxy]: ...
    @property
    def last_request(self) -> Optional[_RequestObjectProxy]: ...
    @property
    def called(self) -> bool: ...
    @property
    def called_once(self) -> bool: ...
    @property
    def call_count(self) -> int: ...
    def reset(self) -> None: ...
    def reset_mock(self) -> None: ...
    def register_uri(
      self,
      method: Union[str, AnyMatcher],
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def request(
      self,
      method: Union[str, AnyMatcher],
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def get(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def head(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def options(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def post(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def put(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def patch(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...
    def delete(
      self,
      url: Union[str, Pattern[str], AnyMatcher],
      response_list: Optional[List[Dict[str, Any]]] = ...,
      *,
      request_headers: Dict[str, str] = ...,
      complete_qs: bool = ...,
      status_code: int = ...,
      reason: str = ...,
      headers: Dict[str, str] = ...,
      cookies: Union[CookieJar, Dict[str, str]] = ...,
      json: Union[Any, Callable[[_RequestObjectProxy, _Context], Any]] = ...,
      text: Union[str, Callable[[_RequestObjectProxy, _Context], str]] = ...,
      content: Union[bytes, Callable[[_RequestObjectProxy, _Context], bytes]] = ...,
      body: Union[IOBase, Callable[[_RequestObjectProxy, _Context], IOBase]] = ...,
      raw: HTTPResponse = ...,
      exc: Exception = ...,
      additional_matcher: Optional[Callable[[_RequestObjectProxy], bool]] = ...,
      **kwargs: Any) -> Response: ...

_T = TypeVar('_T')

class Mocker(MockerCore):
    TEST_PREFIX: str = ...
    def __init__(
      self,
      kw: str = ...,
      case_sensitive: bool = ...,
      adapter: Any = ...,
      real_http: bool = ...) -> None: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def __call__(self, obj: Any) -> Any: ...
    def copy(self) -> Mocker: ...
    def decorate_callable(self, func: Callable[..., _T]) -> Callable[..., _T]: ...
    def decorate_class(self, klass: Type[_T]) -> Type[_T]: ...
mock = Mocker
