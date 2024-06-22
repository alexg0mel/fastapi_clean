from datetime import datetime
from uuid import UUID, uuid4
from app.documents.models import Item

from .item import ItemRepository


class TestItemRepository:
    async def test(self):
        document_uuid = uuid4()
        item1 = self.get_base_item(document_uuid)
        repository = ItemRepository()
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
