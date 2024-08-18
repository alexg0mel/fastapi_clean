from asyncpg.connection import Connection

from app.lib.infrastructures.repository.query_store import QueryStore


class UpdateBaseItemQty(QueryStore):
    def raw_query(self) -> str:
        return """
            update base_item set qty0 = qty0 + {added_qty}
            where uuid = {base_item_uuid}
            returning qty0
        """

    async def execute(self, conn: Connection):
        return await conn.fetchrow(self.query, *self.params)
