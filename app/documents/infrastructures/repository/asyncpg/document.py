from typing import Annotated, Type, Iterable

from asyncpg import Record
from fastapi import Depends

from uuid import UUID
from app.documents.models import Document, Item
from app.documents.services.document import DocumentProvider, ItemModelType
from .base import AsyncPgProvider
from .get_document import GetDocument
from .get_document_stages import GetDocumentStages


class DocumentRepository(AsyncPgProvider, DocumentProvider):
    async def get_document(self, uuid: UUID) -> Document | None:
        query = GetDocument()
        return await query.execute(self.conn, uuid)

    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        query = GetDocumentStages()
        return await query.execute(self.conn, base_uuid)

    async def store_document(self, document: Document) -> Document:
        query = '''
        insert into document(uuid, base_uuid, stage, location_key, number, date, 
                             session_id, user_id, type_user, currency, user_currencyy,
                             is_partner, status, alpha_group, next_uuid)
                    values($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15)
        '''
        await self.conn.execute(query, document.uuid, document.base_uuid, document.stage,
                                document.location_key, document.number, document.date, document.session_id,
                                document.user_id, document.user_id, document.type_user, document.currency,
                                document.user_currency, document.is_partner, document.status,
                                document.alpha_group, document.next_uuid)

        return document

    async def get_item(self, uuid: UUID, type_of_item: Type[ItemModelType]) -> Item | None:
        query = '''
        select * from item
        inner join transaction on item.transaction_id = transaction.id
        where item.uuid = $1
        '''
        row: Record = await self.conn.fetchrow(query, uuid)
        if row is not None:
            return type_of_item.from_dict(dict(**row))

    async def get_document_items(self, document_uuid: UUID, type_of_items: Type[ItemModelType]) -> list[Item]:
        query = '''
        select * from item
        inner join transaction on item.transaction_id = transaction.id
        where item.document_uuid = $1
        '''
        rows = await self.conn.fetch(query, document_uuid)
        return [type_of_items.from_dict(dict(**row)) for row in rows]

    async def store_item(self, item: Item) -> Item:
        return Item

    async def store_items(self, items: Iterable[Item]):
        ...


DocumentRepository = Annotated[DocumentRepository, Depends()]
