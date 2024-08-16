from typing import Iterable, Any
from abc import ABC, abstractmethod

from asyncpg.connection import Connection


class Serial(dict):
    def __getitem__(self, key):
        return f"${list(self.keys()).index(key) + 1}"


class QueryStore(ABC):

    def __init__(self, **params):
        self._params = Serial(**params)

    @abstractmethod
    def raw_query(self) -> str:
        raise NotImplementedError

    @property
    def query(self) -> str:
        return self.raw_query().format_map(self._params)

    @property
    def params(self) -> Iterable[Any]:
        return self._params.values()

    @abstractmethod
    async def execute(self, conn: Connection):
        raise NotImplementedError
