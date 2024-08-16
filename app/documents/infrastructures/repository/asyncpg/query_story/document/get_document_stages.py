from asyncpg.connection import Connection

from app.lib.infrastructures.repository.query_store import QueryStore

from app.documents.models import Document


class GetDocumentStages(QueryStore):
    def raw_query(self) -> str:
        return '''
        select bd.*, d.uuid, d.stage, d.status, d.next_uuid
        from document d
        inner join base_document bd on d.base_uuid = bd.base_uuid
        where d.base_uuid = {base_uuid}
        '''

    async def execute(self, conn: Connection):
        rows = await conn.fetch(self.query, *self.params)
        return [Document.from_dict(dict(**row)) for row in rows]
