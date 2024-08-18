from app.lib.infrastructures.repository.query_store import QueryStore


class StoreBaseDocument(QueryStore):
    def raw_query(self) -> str:
        return """
            insert into base_document (base_uuid, location_key, number, "date", session_id, user_id,
            type_user, currency, user_currency, is_partner, alpha_group)
            values ({base_uuid}, {location_key}, {number}, {date}, {session_id}, {user_id},
            {type_user}, {currency}, {user_currency}, {is_partner}, {alpha_group});
        """
