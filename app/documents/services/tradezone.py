from abc import abstractmethod
from copy import copy
from uuid import uuid4, UUID
from datetime import timedelta, datetime

from asyncpg.exceptions import UniqueViolationError

from app.documents.models import Transaction, BaseDocument, BaseItem, StageDocument, TypeUser, Stage
from app.documents.schemas.tradezone import TransactionSchema
from app.documents.exceptions import DataDuplicationException

from .database_transaction import DatabaseTransaction


class TransactionProvider(DatabaseTransaction):
    @abstractmethod
    async def get_similar_transactions(self,
                                       *,
                                       session_id: int,
                                       pv_id: int,
                                       buyer: int,
                                       seller: int) -> list[Transaction]:
        raise NotImplementedError

    @abstractmethod
    async def store_transaction(self, transaction: Transaction) -> Transaction:
        raise NotImplementedError

    @abstractmethod
    async def store_base_document(self, base_document: BaseDocument) -> BaseDocument:
        raise NotImplementedError

    @abstractmethod
    async def store_base_item(self, base_item: BaseItem) -> BaseItem:
        raise NotImplementedError

    @abstractmethod
    async def add_transaction_to_base_item(self, transaction: Transaction,
                                           base_item: BaseItem,
                                           added_qty: int) -> BaseItem:
        raise NotImplementedError

    @abstractmethod
    async def get_similar_base_item(self,
                                    *,
                                    user_id: int,
                                    type_user: TypeUser,
                                    user_currency: str,
                                    is_partner: bool,
                                    delivery_date: datetime,
                                    user_price: int,
                                    similar_transactions_id: list[int]) -> BaseItem | UUID | None:
        """
        :return: BaseItem if base_item exist,
                 document_uuid if there is no base_item but there is a document
                 or None if a document also does not exist
        """
        raise NotImplementedError

    @abstractmethod
    async def store_document(self, stage_document: StageDocument):
        raise NotImplementedError


class TradezoneService:
    def __init__(self, transaction_provider: TransactionProvider):
        self.transaction_provider = transaction_provider

    async def transactions_upload(self, body: list[TransactionSchema]):
        try:
            await self.transaction_provider.start_transaction()
            for body_item in body:
                transaction = Transaction(id=body_item.id,
                                          session_id=body_item.session.id,
                                          is_parthner=body_item.is_partner,
                                          product_id=body_item.item.product.id,
                                          product_variant_id=body_item.item.product_variant.id,
                                          product_variant_name=body_item.item.product_variant.name,
                                          localization=body_item.item.localization,
                                          chip=body_item.item.chip,
                                          quality=body_item.item.quality,
                                          brand=body_item.item.brand.name,
                                          category=body_item.item.category.name,
                                          supplier_id=body_item.supplier.id,
                                          customer_id=body_item.customer.id,
                                          confirmed_qty=body_item.item.qty if body_item.item.approved else 0
                                          )
                similar_transactions = (await self.transaction_provider.
                                        get_similar_transactions(session_id=transaction.session_id,
                                                                 pv_id=transaction.product_variant_id,
                                                                 buyer=transaction.customer_id,
                                                                 seller=transaction.supplier_id))
                await self.transaction_provider.store_transaction(transaction)

                similar_transactions = self.filter_transactions(similar_transactions,
                                                                localization=transaction.localization,
                                                                chip=transaction.chip,
                                                                quality=transaction.quality)
                customer_transactions = self.filter_transactions(similar_transactions,
                                                                 customer_id=transaction.customer_id)
                supplier_transactions = self.filter_transactions(similar_transactions,
                                                                 supplier_id=transaction.supplier_id)

                await self.process_document(transaction=transaction,
                                            body_item=body_item,
                                            type_user=TypeUser.Buyer,
                                            similar_transactions_id=[transaction.id
                                                                     for transaction in customer_transactions])
                await self.process_document(transaction=transaction,
                                            body_item=body_item,
                                            type_user=TypeUser.Seller,
                                            similar_transactions_id=[transaction.id
                                                                     for transaction in supplier_transactions])

            await self.transaction_provider.commit_transaction()
        except UniqueViolationError as e:
            ...
            await self.transaction_provider.rollback_transaction()
            raise DataDuplicationException from e
        return

    @staticmethod
    def filter_transactions(transactions: list[Transaction], **criteria) -> list[Transaction]:
        transactions = copy(transactions)
        for attr, value in criteria.items():
            transactions = list(filter(lambda d: getattr(d, attr) == value, transactions))
        return transactions

    async def process_document(self, transaction: Transaction,
                               body_item: TransactionSchema,
                               type_user: TypeUser,
                               similar_transactions_id: list[int]):
        doc_date = body_item.session.start_date
        delivery_date = doc_date + timedelta(days=body_item.item.delivery)
        user_currency = body_item.item.customer_currency if type_user == TypeUser.Buyer \
            else body_item.item.supplier_currency
        user_id = transaction.customer_id if type_user == TypeUser.Buyer else transaction.supplier_id

        base_item_or_document_uuid = await self.transaction_provider.get_similar_base_item(
            user_id=user_id,
            type_user=type_user,
            user_currency=user_currency,
            is_partner=transaction.is_parthner,
            delivery_date=delivery_date,
            user_price=body_item.item.customer_price if type_user == TypeUser.Buyer
            else body_item.item.supplier_price,
            similar_transactions_id=similar_transactions_id)
        need_create_base_item = False
        base_document_uuid = None
        if base_item_or_document_uuid is None:
            need_create_base_item = True
            base_document = BaseDocument(
                base_uuid=uuid4(),
                location_key=body_item.location.key,
                number=f"TTTTC-{transaction.id}",  # todo generate true doc number...
                date=doc_date,
                session_id=body_item.session.id,
                user_id=user_id,
                type_user=type_user,
                currency=body_item.item.base_currency,
                user_currency=user_currency,
                is_partner=transaction.is_parthner
            )
            base_document_uuid = base_document.base_uuid
            await self.transaction_provider.store_base_document(base_document)
            proforma_invoice_uuid = uuid4()
            invoice_uuid = uuid4()
            stage_documents_uuid = (base_document_uuid, proforma_invoice_uuid, invoice_uuid)
            next_documents_uuid = (proforma_invoice_uuid, invoice_uuid, None)
            stages_document = (Stage.TradezoneOrder.value, Stage.ProformaInvoice.value, Stage.Invoice.value)
            for document_uuid, stage, next_uuid in zip(stage_documents_uuid, stages_document, next_documents_uuid):
                stage_document = StageDocument(uuid=document_uuid,
                                               base_uuid=base_document_uuid,
                                               stage=stage,
                                               next_uuid=next_uuid)
                await self.transaction_provider.store_document(stage_document)

        elif isinstance(base_item_or_document_uuid, UUID):
            base_document_uuid = base_item_or_document_uuid
            need_create_base_item = True

        if need_create_base_item:
            base_item = BaseItem(
                uuid=uuid4(),
                document_base_uuid=base_document_uuid,
                qty0=0,
                price0=body_item.item.customer_base_price if type_user == TypeUser.Buyer
                else body_item.item.supplier_base_price,
                user_price0=body_item.item.customer_price if type_user == TypeUser.Buyer
                else body_item.item.supplier_price,
                delivery_date0=delivery_date
            )
            await self.transaction_provider.store_base_item(base_item)
        else:
            base_item = base_item_or_document_uuid

        await self.transaction_provider.add_transaction_to_base_item(transaction=transaction,
                                                                     base_item=base_item,
                                                                     added_qty=body_item.item.qty)


# todo
#  0 V создать транзакцию
#  1 V выбрать схожие транзакции (одинаковая сессия и продукт вариант а также совпадает или покупатель или продавец)
#  2 V сравнить чтобы были такие же локализация, чип и качество
#  2а V если найдено - то проходим отдельно по покупател. и продавцу
#  2б V ищем базовые айтемы с базовыми документами =  совпадение по пользователю, роли,
#  валюты пользователя, партнерства, срока поставки и цены
#  2в V если нашли - корректируем количество в айтеме
#  2г V если не нашли - создаем айтемы и документы
#  3 V создать если нет - первые 2 стадии документов (или 3?)  Их можно создать при создании базового документа.....
#  3а аналогично - пачку айтемов делать и при создании базового айтема (придется иметь все документы с базовым uuid)
#  3б айтемы ТО документа должны быть с заполненным количеством.
#  3с Так же следует предусмотреть "корректировку" количества при изменении базового документа (в стадии ТО)
