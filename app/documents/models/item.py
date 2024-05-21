from typing import Type
from dataclasses import dataclass
from datetime import date
from uuid import UUID

from .enums import Stage, TypeUser


@dataclass
class Item:
    """
    Items belong to a specific document.
    Depending on the type of user and the stage of the document,
    there may be different subtype of an item, with its own fields.
    """
    uuid: UUID
    document_uuid: UUID
    product_id: int
    product_variant_id: str
    product_variant_name: str
    localization: str | None
    chip: str | None
    quality: str | None
    qty: int
    price: int
    user_price: int
    delivery_date: date


class ItemSO(Item):
    pass


class ItemPO(Item):
    pass


class ItemSI(Item):
    qty0: int
    user_price0: int
    accepted: bool


class ItemPI(Item):
    qty0: int
    user_price0: int
    accepted: bool


class ItemSIn(Item):
    qty0: int
    user_price0: int


class ItemPIn(Item):
    qty0: int
    user_price0: int


class ItemCD(Item):
    pass


def select_type_of_item(stage: Stage, type_user: TypeUser) -> Type[Item]:
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
