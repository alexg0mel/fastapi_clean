from uuid import UUID
from documents.models import Document
from documents.services.document import DocumentProvider

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

