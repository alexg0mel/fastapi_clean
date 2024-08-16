from datetime import datetime
from uuid import UUID

from app.lib.models.base import Base


class Item(Base):
    uuid: UUID
    document_uuid: UUID
    product_id: int
    product_variant_id: int
    product_variant_name: str
    localization: str | None = None
    chip: str | None = None
    quality: str | None = None
    brand: str
    category: str
    qty: int
    price: int
    user_price: int
    delivery_date: datetime
