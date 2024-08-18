from datetime import datetime
from uuid import UUID

from app.lib.models.base import Base
from .enums import TypeUser, AlphaGroup, Stage, DocumentStatus


class Transaction(Base):
    id: int
    session_id: int
    is_parthner: bool = False
    product_id: int
    product_variant_id: int
    product_variant_name: str
    localization: str | None = None
    chip: str | None = None
    quality: str | None = None
    brand: str
    category: str
    supplier_id: int
    customer_id: int
    confirmed_qty: int


class BaseDocument(Base):
    base_uuid: UUID
    location_key: str
    number: str
    date: datetime
    session_id: int
    user_id: int
    type_user: TypeUser
    currency: str
    user_currency: str
    is_partner: bool = False
    alpha_group: AlphaGroup = AlphaGroup.Empty


class BaseItem(Base):
    uuid: UUID
    document_base_uuid: UUID
    qty0: int
    price0: int
    user_price0: int
    delivery_date0: datetime


class StageDocument(Base):
    uuid: UUID
    base_uuid: UUID
    stage: Stage
    status: DocumentStatus = DocumentStatus.Draft
    next_uuid: UUID | None = None
