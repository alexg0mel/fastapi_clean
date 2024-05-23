from datetime import date
from uuid import uuid4
from documents.models import Document, Stage, DocumentStatus, TypeUser

from .document import DocumentRepository


class TestDocumentRepository:
    async def test(self):
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
