from uuid import uuid4
from datetime import date
from .document import Document


class TestDocument:
    def test(self):
        uuid = uuid4()
        document = Document(
            uuid=uuid,
            base_uuid=uuid,
            stage='TO',
            location_key='TEST',
            number='4F001',
            date=date.today(),
            session_id=2,
            user_id=1,
            type_user='seller',
            currency='USD',
            user_currency='RUB'
        )
        assert document
        assert document.uuid == uuid
        assert document.stage == 'TO'
        assert document.type_user == 'seller'
        assert document.status == 'forming'
        assert document.alpha_group == '-'
        assert document.next_uuid is None

        document_in_dict = document.to_dict()
        assert len(document_in_dict) == 19
        assert document_in_dict['uuid'] == uuid
