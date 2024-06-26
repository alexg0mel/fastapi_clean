from asyncpg import create_pool as create_asyncpg_pool
from asyncpg.connection import Connection


class ConnectionPool:
    __pool = None

    def __init__(self, dsn):
        self.dsn = dsn

    async def __call__(self) -> Connection:
        if self.__pool is None:
            self.__pool = await create_asyncpg_pool(self.dsn)
        async with self.__pool.acquire() as connection:
            yield connection
