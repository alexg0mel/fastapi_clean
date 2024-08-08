from asyncpg.connection import Connection

from app.lib.infrastructures.repository.query_store import QueryStore

from app.documents.models import Document


class GetDocumentItems(QueryStore):
    @property
    def query(self) -> str:
        return '''
        select * from item
        inner join transaction on item.transaction_id = transaction.id
        where item.document_uuid = $1
        '''

    async def execute(self, conn: Connection, *args, **kwargs):
        """
        :param args:   document_uuid
               kwargs: type_of_items
        """
        type_of_items = kwargs.get('type_of_items')
        rows = await conn.fetch(self.query, *args)
        return [type_of_items.from_dict(dict(**row)) for row in rows]
