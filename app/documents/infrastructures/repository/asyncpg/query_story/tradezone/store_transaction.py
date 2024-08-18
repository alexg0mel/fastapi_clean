from app.lib.infrastructures.repository.query_store import QueryStore


class StoreTransaction(QueryStore):
    def raw_query(self) -> str:
        return """
            insert into transaction (id, session_id, product_id, product_variant_id, product_variant_name,
            localization, chip, quality, brand, category, supplier_id, customer_id, confirmed_qty, is_parthner)
                    values({id}, {session_id}, {product_id}, {product_variant_id}, {product_variant_name},
            {localization}, {chip}, {quality}, {brand}, {category}, {supplier_id},
            {customer_id}, {confirmed_qty}, {is_parthner})
        """
