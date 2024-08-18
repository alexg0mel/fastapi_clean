from typing import Annotated
from datetime import datetime
from uuid import UUID

from fastapi import Depends

from app.documents.services.tradezone import TransactionProvider
from app.documents.models import Transaction, BaseDocument, BaseItem, StageDocument, TypeUser

from .base import AsyncPgProvider
from .query_story.tradezone import (StoreTransaction, StoreBaseItem,
                                    StoreBaseDocument, GetSimilarTransactions,
                                    AddTransactionToBaseItem, UpdateBaseItemQty,
                                    GetSimilarBaseItem, GetSimilarBaseDocument,
                                    StoreStageDocument)


class TransactionRepository(AsyncPgProvider, TransactionProvider):
    async def get_similar_transactions(self,
                                       *,
                                       session_id: int,
                                       pv_id: int,
                                       buyer: int,
                                       seller: int) -> list[Transaction]:
        query = GetSimilarTransactions(session_id=session_id,
                                       product_variant_id=pv_id,
                                       customer_id=buyer,
                                       supplier_id=seller)
        return await query.execute(self.conn)

    async def store_transaction(self, transaction: Transaction) -> Transaction:
        query = StoreTransaction(**transaction.to_dict())
        await query.execute(self.conn)
        return transaction

    async def store_base_document(self, base_document: BaseDocument) -> BaseDocument:
        query = StoreBaseDocument(**base_document.to_dict())
        await query.execute(self.conn)
        return base_document

    async def store_base_item(self, base_item: BaseItem) -> BaseItem:
        query = StoreBaseItem(**base_item.to_dict())
        await query.execute(self.conn)
        return base_item

    async def add_transaction_to_base_item(self, transaction: Transaction,
                                           base_item: BaseItem,
                                           added_qty: int) -> BaseItem:
        query = AddTransactionToBaseItem(transaction_id=transaction.id, base_item_uuid=base_item.uuid)
        await query.execute(self.conn)
        query = UpdateBaseItemQty(base_item_uuid=base_item.uuid, added_qty=added_qty)
        row = await query.execute(self.conn)
        base_item.qty0 = row.get('qty0')
        return base_item

    async def get_similar_base_item(self,
                                    *,
                                    user_id: int,
                                    type_user: TypeUser,
                                    user_currency: str,
                                    is_partner: bool,
                                    delivery_date: datetime,
                                    user_price: int,
                                    similar_transactions_id: list[int]) -> BaseItem | UUID | None:
        if similar_transactions_id:
            query = GetSimilarBaseItem(user_id=user_id,
                                       type_user=type_user,
                                       user_currency=user_currency,
                                       is_partner=is_partner,
                                       delivery_date=delivery_date,
                                       user_price=user_price,
                                       similar_transactions_id=similar_transactions_id)
        else:
            query = GetSimilarBaseDocument(
                user_id=user_id,
                type_user=type_user,
                user_currency=user_currency,
                is_partner=is_partner,
            )
        return await query.execute(self.conn)

    async def store_document(self, stage_document: StageDocument):
        query = StoreStageDocument(**stage_document.to_dict())
        await query.execute(self.conn)
        return stage_document


TransactionRepository = Annotated[TransactionRepository, Depends()]
