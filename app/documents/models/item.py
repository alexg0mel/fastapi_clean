from typing import Type, TypeVar
from datetime import datetime
from uuid import UUID

from app.lib.models.base import Base

from .enums import Stage, TypeUser


class BaseItem(Base):
    """
    Items belong to a specific document.
    Depending on the type of user and the stage of the document,
    there may be different subtype of an item, with its own fields.
    """
    uuid: UUID
    document_uuid: UUID
    product_id: int
    product_variant_id: int
    product_variant_name: str
    localization: str | None = None
    chip: str | None = None
    quality: str | None = None
    qty: int
    price: int
    user_price: int
    delivery_date: datetime


class ItemSO(BaseItem):
    pass


class ItemPO(BaseItem):
    pass


class ItemSI(BaseItem):
    qty0: int
    user_price0: int
    accepted: bool = False


class ItemPI(BaseItem):
    qty0: int
    user_price0: int
    accepted: bool = False


class ItemSIn(BaseItem):
    qty0: int
    user_price0: int


class ItemPIn(BaseItem):
    qty0: int
    user_price0: int


class ItemCD(BaseItem):
    pass


def select_type_of_item(stage: Stage, type_user: TypeUser) -> Type[BaseItem]:
    match (stage, type_user):
        case (Stage.TradezoneOrder, TypeUser.Buyer):
            return ItemPO
        case (Stage.TradezoneOrder, TypeUser.Seller):
            return ItemSO
        case (Stage.ProformaInvoice, TypeUser.Buyer):
            return ItemPI
        case (Stage.ProformaInvoice, TypeUser.Seller):
            return ItemSI
        case (Stage.Invoice, TypeUser.Buyer):
            return ItemPIn
        case (Stage.Invoice, TypeUser.Seller):
            return ItemSIn
        case (Stage.CanceledDocument, _):
            return ItemCD
        case (_, _):
            return Item


Item = TypeVar("Item", bound=BaseItem)
