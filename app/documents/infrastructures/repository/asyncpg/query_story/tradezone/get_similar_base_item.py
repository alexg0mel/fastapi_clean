from asyncpg.connection import Connection

from app.lib.infrastructures.repository.query_store import QueryStore
from app.documents.models import BaseItem


class GetSimilarBaseItem(QueryStore):
    def raw_query(self) -> str:
        return """
            select bd.base_uuid, bi.*
            from base_document bd
                left join base_item bi on bd.base_uuid = bi.document_base_uuid
                and bi.user_price0 = {user_price}
                and bi.delivery_date0 = {delivery_date}
                and bi.uuid in (select ti.base_item_uuid
                                from transaction_to_item ti
                                where ti.transaction_id = any({similar_transactions_id}::int[]))
            where bd.user_id = {user_id} and bd.type_user = {type_user}
            and bd.user_currency = {user_currency} and bd.is_partner = {is_partner}

        """

    async def execute(self, conn: Connection):
        row = await conn.fetchrow(self.query, *self.params)
        if row is None:
            return None
        if row.get('uuid') is None:
            return row.get('base_uuid')
        return BaseItem.from_dict(dict(**row))


class GetSimilarBaseDocument(QueryStore):
    def raw_query(self) -> str:
        return """
            select bd.base_uuid
            from base_document bd
            where bd.user_id = {user_id} and bd.type_user = {type_user}
            and bd.user_currency = {user_currency} and bd.is_partner = {is_partner}

        """

    async def execute(self, conn: Connection):
        row = await conn.fetchrow(self.query, *self.params)
        if row is None:
            return None
        return row.get('base_uuid')
