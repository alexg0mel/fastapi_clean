import logging
from fastapi import APIRouter

from app.documents.schemas.tradezone import TransactionSchema
from app.documents.services.tradezone import TradezoneService
from app.documents.infrastructures.repository.asyncpg.tradezone import TransactionRepository


logger = logging.getLogger(__name__)

transaction_router = APIRouter()


@transaction_router.post('/upload')
async def transactions_upload(body: list[TransactionSchema], repository: TransactionRepository):
    logger.info('transaction upload AP')
    service = TradezoneService(repository)
    await service.transactions_upload(body)
    return
