import logging
from uuid import UUID
from fastapi import APIRouter, HTTPException
from app.documents.infrastructures.repository.sqlalchemy.document import DocumentRepository
from app.documents.services.document import DocumentService
from app.documents.models.document import Document

logger = logging.getLogger(__name__)

alchemy_document_router = APIRouter()


@alchemy_document_router.get('/{uuid}')
async def get_document(uuid: UUID, repository: DocumentRepository) -> Document:
    logger.info('get document AP', extra={'uuid': uuid})
    service = DocumentService(repository)
    document = await service.get_document(uuid)
    if document is None:
        raise HTTPException(status_code=404,
                            detail=f'Document {uuid} not found')
    return document


@alchemy_document_router.get('/stages/{base_uuid}')
async def get_document_stages(base_uuid: UUID, repository: DocumentRepository) -> list[Document]:
    logger.info('get document stages AP', extra={'base_uuid': base_uuid})
    service = DocumentService(repository)
    documents = await service.get_document_stages(base_uuid=base_uuid)
    return documents
