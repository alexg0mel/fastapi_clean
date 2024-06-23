from typing import Iterable, Type
from uuid import UUID
from app.documents.models import Document, Item
from app.documents.services.document import DocumentProvider, ItemModelType

from .base import InMemoryProvider


class DocumentRepository(InMemoryProvider, DocumentProvider):
    async def get_document(self, uuid: UUID) -> Document | None:
        return self.get_value(uuid=uuid)

    async def store_document(self, document: Document) -> Document:
        self.store(uuid=document.uuid, value=document)
        stages = await self.get_document_stages(base_uuid=document.base_uuid)
        new_stages = []
        for stage in stages:
            if stage.uuid != document.uuid:
                new_stages.append(stage)
        new_stages.append(document)
        self.store(base_uuid=document.base_uuid, value=new_stages)
        return document

    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        return self.get_value(base_uuid=base_uuid, default=[])

    async def get_item(self, uuid: UUID, type_of_item: Type[ItemModelType] = Item) -> Item | None:
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

    async def get_document_items(self, document_uuid: UUID, type_of_items: Type[ItemModelType] = Item) -> list[Item]:
        return self.get_value(document_uuid=document_uuid, default=[])
