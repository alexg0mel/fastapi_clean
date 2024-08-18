from fastapi import APIRouter

from .document import document_router
from .item import item_router
from .transaction import transaction_router

router = APIRouter()

router.include_router(document_router, tags=['documents'], prefix='/documents')
router.include_router(item_router, tags=['items'], prefix='/documents')
router.include_router(transaction_router, tags=['transactions'], prefix='/transactions')
