from app.lib.infrastructures.repository.query_store import QueryStore


class StoreBaseItem(QueryStore):
    def raw_query(self) -> str:
        return """
            insert into base_item (uuid, document_base_uuid, qty0, price0, user_price0, delivery_date0)
            values ({uuid}, {document_base_uuid}, {qty0}, {price0}, {user_price0}, {delivery_date0});
        """
