import logging
from uuid import UUID
from fastapi import APIRouter, HTTPException
from app.documents.infrastructures.repository.asyncpg.document import DocumentRepository
from app.documents.services.document import DocumentService
from app.documents.models.document import Document
from app.lib.context import RequestId


logger = logging.getLogger(__name__)

document_router = APIRouter()


@document_router.get('/{uuid}')
async def get_document(uuid: UUID, repository: DocumentRepository, request_id: RequestId) -> Document:
    logger.info('get document AP', extra={'uuid': uuid})
    service = DocumentService(repository)
    document = await service.get_document(uuid)
    if document is None:
        raise HTTPException(status_code=404,
                            detail=f'Document {uuid} not found, request {request_id} ')
    return document


@document_router.get('/stages/{base_uuid}')
async def get_document_stages(base_uuid: UUID, repository: DocumentRepository) -> list[Document]:
    logger.info('get document stages AP', extra={'base_uuid': base_uuid})
    service = DocumentService(repository)
    documents = await service.get_document_stages(base_uuid=base_uuid)
    return documents
