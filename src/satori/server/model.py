from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, AsyncIterator, Generic, Protocol, TypeVar, Union, runtime_checkable

from satori.const import Api
from satori.model import Event, Login

if TYPE_CHECKING:
    from .route import RouteCall

JsonType = Union[list, dict, str, int, bool, float, None]
TA = TypeVar("TA", str, Api)
TP = TypeVar("TP")


@dataclass
class Request(Generic[TP]):
    headers: dict[str, Any]
    action: str
    params: TP


@runtime_checkable
class Provider(Protocol):
    def publisher(self) -> AsyncIterator[Event]: ...

    def authenticate(self, token: str) -> bool: ...

    def proxy_urls(self) -> list[str]: ...

    async def get_logins(self) -> list[Login]: ...

    async def download(self, url: str) -> bytes: ...


@runtime_checkable
class Router(Protocol):
    routes: dict[str, RouteCall[Any, Any]]

    def validate_headers(self, headers: dict[str, Any]) -> bool: ...
