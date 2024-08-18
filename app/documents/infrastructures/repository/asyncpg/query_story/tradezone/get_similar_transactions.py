from asyncpg.connection import Connection

from app.lib.infrastructures.repository.query_store import QueryStore
from app.documents.models import Transaction


class GetSimilarTransactions(QueryStore):
    def raw_query(self) -> str:
        return """
            select * from transaction
                where session_id = {session_id}
                and product_variant_id = {product_variant_id}
                and (customer_id = {customer_id} or supplier_id = {supplier_id})
        """

    async def execute(self, conn: Connection):
        rows = await conn.fetch(self.query, *self.params)
        return [Transaction.from_dict(dict(**row)) for row in rows]
