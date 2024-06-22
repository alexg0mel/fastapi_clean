from typing import Iterable
from uuid import UUID
from app.documents.models import Item
from app.documents.services.document import ItemProvider

from .base import InMemoryProvider


class ItemRepository(InMemoryProvider, ItemProvider):
    async def get_item(self, uuid: UUID) -> Item | None:
        return self.get_value(uuid=uuid)

    async def store_item(self, item: Item) -> Item:
        self.store(uuid=item.uuid, value=item)
        return item

    async def store_items(self, items: Iterable[Item]):
        document_uuid = None
        for item in items:
            if document_uuid is None:
                document_uuid = item.document_uuid
            await self.store_item(item)
        if document_uuid is not None:
            self.store(document_uuid=document_uuid, value=items)

    async def get_document_items(self, document_uuid: UUID) -> list[Item]:
        return self.get_value(document_uuid=document_uuid, default=[])
