from asyncpg.connection import Connection

from app.lib.infrastructures.repository.query_store import QueryStore

from app.documents.models import Imei, Box


class GetBoxes(QueryStore):
    @property
    def query(self) -> str:
        return """
        select box.uuid, box.number, imei.code
        from box
        inner join imei on box.uuid = imei.box_uuid
        inner join transaction on transaction.id = imei.transaction_id
        inner join transaction_to_item on transaction_to_item.transaction_id = transaction.id
        inner join base_item on base_item.uuid = transaction_to_item.base_item_uuid
        where (box.document_uuid = $1 or imei.from_document_uuid = $1)
        and base_item.uuid = $2
        """

    async def execute(self, conn: Connection, *args):
        """
        :param args: document_uuid, document_uuid, item.uuid
        """
        boxes = {}
        rows = await conn.fetch(self.query, *args)
        for row in rows:
            uuid = row.get('uuid')
            if uuid not in boxes:
                boxes[uuid] = Box(uuid=uuid, number=row.get('number'))
            boxes[uuid].imeis.append(Imei(code=row.get('code')))
        return [box for box in boxes.values()]
