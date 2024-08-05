from fastapi import Depends

from asyncpg.connection import Connection

from app.documents.infrastructures.clients.connection import pool
from app.lib.context import RequestId


class AsyncPgProvider:
    def __init__(self, request_id: RequestId, conn: Connection = Depends(pool)):
        self.conn = conn
        self.request_id = request_id
        self.transaction = conn.transaction()

    async def start_transaction(self):
        await self.transaction.start()

    async def commit_transaction(self):
        await self.transaction.commit()

    async def rollback_transaction(self):
        await self.transaction.rollback()
