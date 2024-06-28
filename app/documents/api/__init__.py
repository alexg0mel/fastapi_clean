from fastapi import APIRouter

from .document import document_router
from .alchemy_document import alchemy_document_router

router = APIRouter()

router.include_router(document_router, tags=['documents'], prefix='/documents')
router.include_router(alchemy_document_router, tags=['documents'], prefix='/alchemy-documents')
