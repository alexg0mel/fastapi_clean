from asyncpg.connection import Connection
from asyncpg import Record

from app.lib.infrastructures.repository.query_store import QueryStore

from app.documents.models import Document


class GetDocument(QueryStore):
    def raw_query(self) -> str:
        return """
            select bd.*, d.uuid, d.stage, d.status, d.next_uuid
            from document d
            inner join base_document bd on d.base_uuid = bd.base_uuid
            where d.uuid = {document_uuid}
        """

    async def execute(self, conn: Connection):
        row: Record = await conn.fetchrow(self.query, *self.params)
        if row is not None:
            return Document.from_dict(dict(**row))
