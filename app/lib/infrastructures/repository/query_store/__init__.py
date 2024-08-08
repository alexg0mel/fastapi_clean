from abc import ABC, abstractmethod

from asyncpg.connection import Connection


class QueryStore(ABC):

    @property
    @abstractmethod
    def query(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def execute(self, conn: Connection, *args, **kwargs):
        raise NotImplementedError

