from fastapi import Depends

from asyncpg.connection import Connection

from app.documents.infrastructures.clients.connection import pool


class AsyncPgProvider:
    def __init__(self, conn: Connection = Depends(pool)):
        self.conn = conn
