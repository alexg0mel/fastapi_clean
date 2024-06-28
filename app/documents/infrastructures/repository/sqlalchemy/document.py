from typing import Annotated, Iterable, Type
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from fastapi import Depends

from app.documents.services.document import DocumentProvider, ItemModelType
from app.documents.models import Document, Item


from .base import BaseDBRepository
from .models import DocumentModel


class DocumentRepository(BaseDBRepository, DocumentProvider):
    async def get_document(self, uuid: UUID) -> Document | None:
        query = select(DocumentModel).where(DocumentModel.uuid == uuid).options(
            joinedload(DocumentModel.items, innerjoin=True)
        )
        document = await self.session.scalar(query)
        return document

    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        query = select(DocumentModel).where(DocumentModel.base_uuid == base_uuid).options(
            joinedload(DocumentModel.items, innerjoin=True)
        )
        result = await self.session.scalars(query)
        return result.unique().all()

    async def store_document(self, document: Document) -> Document:
        ...

    async def get_item(self, uuid: UUID, type_of_item: Type[ItemModelType]) -> Item | None:
        ...

    async def get_document_items(self, document_uuid: UUID, type_of_items: Type[ItemModelType]) -> list[Item]:
        return []

    async def store_item(self, item: Item) -> Item:
        ...

    async def store_items(self, items: Iterable[Item]):
        ...


DocumentRepository = Annotated[DocumentRepository, Depends()]
