from abc import ABC, abstractmethod
from uuid import UUID

from app.documents.models import Box


class ItemProvider(ABC):
    @abstractmethod
    async def get_boxes(self, document_uuid: UUID, item_uuid: UUID) -> list[Box]:
        raise NotImplementedError


class ItemService:
    def __init__(self, item_provider: ItemProvider):
        self.item_provider = item_provider

    async def get_boxes(self, document_uuid: UUID, item_uuid: UUID) -> list[Box]:
        return await self.item_provider.get_boxes(document_uuid, item_uuid)
