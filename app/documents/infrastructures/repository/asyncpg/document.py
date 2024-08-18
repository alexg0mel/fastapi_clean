from typing import Annotated, Iterable

from asyncpg import Record
from fastapi import Depends

from uuid import UUID
from app.documents.models import Document, Item
from app.documents.services.document import DocumentProvider

from app.documents.infrastructures.repository.asyncpg.query_story.document.get_document import GetDocument
from app.documents.infrastructures.repository.asyncpg.query_story.document.get_document_stages import GetDocumentStages
from app.documents.infrastructures.repository.asyncpg.query_story.document.get_document_items import GetDocumentItems

from .base import AsyncPgProvider


class DocumentRepository(AsyncPgProvider, DocumentProvider):
    async def get_document(self, uuid: UUID) -> Document | None:
        query = GetDocument(document_uuid=uuid)
        return await query.execute(self.conn)

    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        query = GetDocumentStages(base_uuid=base_uuid)
        return await query.execute(self.conn)

    async def get_item(self, uuid: UUID) -> Item | None:
        query = '''
        select * from item
        inner join transaction on item.transaction_id = transaction.id
        where item.uuid = $1
        '''
        row: Record = await self.conn.fetchrow(query, uuid)
        if row is not None:
            return Item.from_dict(dict(**row))

    async def get_document_items(self, document_uuid: UUID) -> list[Item]:
        query = GetDocumentItems(document_uuid=document_uuid)
        return await query.execute(self.conn)

    async def store_item(self, item: Item) -> Item:
        return Item

    async def store_items(self, items: Iterable[Item]):
        ...


DocumentRepository = Annotated[DocumentRepository, Depends()]
