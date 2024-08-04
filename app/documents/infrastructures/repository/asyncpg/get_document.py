from asyncpg.connection import Connection
from asyncpg import Record

from app.lib.infrastructures.repository.query_store import QueryStore

from app.documents.models import Document


class GetDocument(QueryStore):
    @property
    def query(self) -> str:
        return """
            select * from document
            where document.uuid = $1
        """

    async def execute(self, conn: Connection, *args):
        """
        :param args: uuid
        """
        row: Record = await conn.fetchrow(self.query, *args)
        if row is not None:
            return Document.from_dict(dict(**row))
