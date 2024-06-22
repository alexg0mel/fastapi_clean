from typing import Iterable
from abc import ABC, abstractmethod
from uuid import UUID

from app.documents.models.document import Document, Item


class DocumentProvider(ABC):
    @abstractmethod
    async def get_document(self, uuid: UUID) -> Document | None:
        raise NotImplementedError

    @abstractmethod
    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        raise NotImplementedError

    @abstractmethod
    async def store_document(self, document: Document) -> Document:
        raise NotImplementedError


class ItemProvider(ABC):
    @abstractmethod
    async def get_item(self, uuid: UUID) -> Item | None:
        raise NotImplementedError

    @abstractmethod
    async def get_document_items(self, document_uuid: UUID) -> list[Item]:
        raise NotImplementedError

    @abstractmethod
    async def store_item(self, item: Item) -> Item:
        raise NotImplementedError

    @abstractmethod
    async def store_items(self, items: Iterable[Item]):
        raise NotImplementedError


class DocumentService:
    def __init__(self, document_provider: DocumentProvider):
        self.document_provider = document_provider

    async def get_document(self, uuid: UUID) -> Document:
        document = await self.document_provider.get_document(uuid)
        if document is not None:
            self.calculate_document(document)
        return document

    async def get_document_stages(self, base_uuid: UUID) -> list[Document]:
        documents = await self.document_provider.get_document_stages(base_uuid)
        for document in documents:
            self.calculate_document(document)
        return documents

    def calculate_document(self, document: Document) -> Document:
        sum = 0
        user_sum = 0
        qty = 0
        for item in document.items:
            sum += item.price * item.qty
            user_sum += item.user_price * item.qty
            qty += item.qty
        return document
