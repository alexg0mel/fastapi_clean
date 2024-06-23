from datetime import datetime, date
from uuid import UUID, uuid4
from app.documents.models import Document, Item, Stage, DocumentStatus, TypeUser

from .document import DocumentRepository


class TestDocumentRepository:
    async def test_document(self):
        stage1_document = self.get_base_document()
        repository = DocumentRepository()
        assert await repository.get_document(uuid=stage1_document.uuid) is None
        await repository.store_document(stage1_document)
        assert await repository.get_document(uuid=stage1_document.uuid) == stage1_document
        stages_in_repo = await repository.get_document_stages(base_uuid=stage1_document.base_uuid)
        assert len(stages_in_repo) == 1
        stage2_document = Document.from_dict(stage1_document.to_dict())
        stage2_document.uuid = uuid4()
        stage1_document.next_uuid = stage2_document.uuid
        stage2_document.status = DocumentStatus.Draft
        await repository.store_document(stage1_document)
        await repository.store_document(stage2_document)
        assert await repository.get_document(uuid=stage1_document.uuid) == stage1_document
        assert await repository.get_document(uuid=stage2_document.uuid) == stage2_document
        stages_in_repo = await repository.get_document_stages(base_uuid=stage1_document.base_uuid)
        assert len(stages_in_repo) == 2
        assert stages_in_repo[0] == stage1_document
        assert stages_in_repo[1] == stage2_document

    async def test_item(self):
        document_uuid = uuid4()
        item1 = self.get_base_item(document_uuid)
        repository = DocumentRepository()
        assert await repository.get_item(uuid=item1.uuid) is None
        await repository.store_item(item1)
        assert await repository.get_item(uuid=item1.uuid) == item1
        document_items = await repository.get_document_items(document_uuid)
        assert len(document_items) == 0
        item2 = self.get_base_item(document_uuid)
        item3 = self.get_base_item(document_uuid)
        await repository.store_items((item1, item2, item3))
        assert await repository.get_item(uuid=item1.uuid) == item1
        assert await repository.get_item(uuid=item2.uuid) == item2
        assert await repository.get_item(uuid=item3.uuid) == item3
        document_items = await repository.get_document_items(document_uuid)
        assert len(document_items) == 3
        assert document_items[0] == item1
        assert document_items[1] == item2
        assert document_items[2] == item3

    @staticmethod
    def get_base_document():
        base_uuid = uuid4()
        base_document = Document(
            uuid=base_uuid,
            base_uuid=base_uuid,
            stage=Stage.TradezoneOrder,
            location_key='TEST',
            number="3F002",
            date=date.today(),
            session_id=12,
            user_id=4,
            type_user=TypeUser.Seller,
            currency='USD',
            user_currency='USDT',
            status=DocumentStatus.Active
        )
        return base_document

    @staticmethod
    def get_base_item(document_uuid: UUID):
        base_item = Item(
            uuid=uuid4(),
            document_uuid=document_uuid,
            product_id=1,
            product_variant_id=10,
            product_variant_name='test variant',
            localization='EU',
            qty=5,
            price=1000,
            user_price=10000,
            delivery_date=datetime.now()
        )
        return base_item
