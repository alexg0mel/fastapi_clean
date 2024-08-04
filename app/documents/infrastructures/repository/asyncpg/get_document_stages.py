from asyncpg.connection import Connection
from asyncpg import Record

from app.lib.infrastructures.repository.query_store import QueryStore

from app.documents.models import Document


class GetDocumentStages(QueryStore):
    @property
    def query(self) -> str:
        return '''
        select * from document
        where document.base_uuid = $1
        '''

    async def execute(self, conn: Connection, *args):
        """
        :param args: base_uuid
        """
        rows = await conn.fetch(self.query, *args)
        return [Document.from_dict(dict(**row)) for row in rows]
