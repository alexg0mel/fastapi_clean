from typing import Annotated
from uuid import UUID

from fastapi import Depends

from app.documents.models import Box
from app.documents.services.item import ItemProvider

from .base import AsyncPgProvider
from .get_boxes import GetBoxes


class ItemRepository(AsyncPgProvider, ItemProvider):
    async def get_boxes(self, document_uuid: UUID, item_uuid: UUID) -> list[Box]:
        query = GetBoxes()
        return await query.execute(self.conn, document_uuid, item_uuid)


ItemRepository = Annotated[ItemRepository, Depends()]
