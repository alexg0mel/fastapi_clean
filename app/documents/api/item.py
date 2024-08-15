import logging
from uuid import UUID
from fastapi import APIRouter
from app.documents.infrastructures.repository.asyncpg.item import ItemRepository
from app.documents.services.item import ItemService


logger = logging.getLogger(__name__)

item_router = APIRouter()


@item_router.get('/{document_uuid}/items/{item_uuid}')
async def get_boxes(document_uuid: UUID, item_uuid: UUID, repository: ItemRepository):
    logger.info('get item boxes AP', extra={"document_uuid": document_uuid,
                                            "item_uuid": item_uuid})
    service = ItemService(repository)
    boxes = await service.get_boxes(document_uuid=document_uuid,
                                    item_uuid=item_uuid)

    return boxes
