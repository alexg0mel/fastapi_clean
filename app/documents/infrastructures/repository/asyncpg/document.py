from typing import Annotated

from asyncpg import Record
from fastapi import Depends

from uuid import UUID
from app.documents.models import Document
from app.documents.services.document import DocumentProvider
from .base import AsyncPgProvider


class DocumentRepository(AsyncPgProvider, DocumentProvider):
    async def get_document(self, uuid: UUID) -> Document | None:
        query = '''
        select * from document
        where document.uuid = $1
        '''
        row: Record = await self.conn.fetchrow(query, uuid)
        if row is not None:
            return Document.from_dict(dict(**row))

    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        query = '''
        select * from document
        where document.base_uuid = $1
        '''
        rows = await self.conn.fetch(query, base_uuid)
        return [Document.from_dict(dict(**row)) for row in rows ]

    async def store_document(self, document: Document) -> Document:
        query = '''
        insert into document(uuid, base_uuid, stage, location_key, number, date, 
                             session_id, user_id, type_user, currency, user_currencyy,
                             is_partner, status, alpha_group, next_uuid)
                    values($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15)
        '''
        await self.conn.execute(query, document.uuid, document.base_uuid, document.stage,
                                document.location_key,document.number,document.date, document.session_id,
                                document.user_id, document.user_id, document.type_user, document.currency,
                                document.user_currency, document.is_partner, document.status,
                                document.alpha_group, document.next_uuid)

        return document


DocumentRepository = Annotated[DocumentRepository, Depends()]
