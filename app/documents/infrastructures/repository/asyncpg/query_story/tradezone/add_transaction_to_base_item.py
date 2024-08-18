from app.lib.infrastructures.repository.query_store import QueryStore


class AddTransactionToBaseItem(QueryStore):
    def raw_query(self) -> str:
        return """
            insert into transaction_to_item (transaction_id, base_item_uuid)
            values ({transaction_id}, {base_item_uuid});
            """
