from app.lib.infrastructures.repository.query_store import QueryStore


class StoreStageDocument(QueryStore):
    def raw_query(self) -> str:
        return """
            insert into document (uuid, base_uuid, stage, status, next_uuid)
            values ({uuid}, {base_uuid}, {stage}, {status}, {next_uuid});
        """
