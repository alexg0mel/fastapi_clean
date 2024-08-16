from asyncpg.connection import Connection

from app.documents.models.item import Item
from app.lib.infrastructures.repository.query_store import QueryStore


class GetDocumentItems(QueryStore):
    def raw_query(self) -> str:
        return '''
        select distinct on (item.base_item_uuid)
        base_item.uuid,
        item.document_uuid, item.qty, item.price, item.user_price, item.delivery_date,
        t.product_id, t.product_variant_id, t.product_variant_name, t.localization,
        t.chip, t.quality, t.brand, t.category
        from item
        inner join base_item on item.base_item_uuid = base_item.uuid
        inner join transaction_to_item on base_item.uuid = transaction_to_item.base_item_uuid
        inner join transaction t on transaction_to_item.transaction_id = t.id
        where item.document_uuid = {document_uuid}
        '''

    async def execute(self, conn: Connection):
        rows = await conn.fetch(self.query, *self.params)
        return [Item.from_dict(dict(**row)) for row in rows]
