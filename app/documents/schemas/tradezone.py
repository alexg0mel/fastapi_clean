from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# from .product_variant import ProductVariantSchema


class SessionSchema(BaseModel):
    id: int
    start_date: datetime


class IdNameTypeSchema(BaseModel):
    id: int
    name: str


class UserTypeSchema(IdNameTypeSchema):
    nickname: str = ''


class IdTypeSchema(BaseModel):
    id: int


class LocationSchema(BaseModel):
    key: str


class ItemSchema(BaseModel):
    product_variant: IdNameTypeSchema
    brand: IdNameTypeSchema
    category: IdNameTypeSchema
    product: IdTypeSchema
    localization: Optional[str] = ''
    chip: Optional[str] = ''
    quality: Optional[str] = ''
    delivery: int
    qty: int
    base_currency: str
    customer_currency: str
    supplier_currency: str
    reseller_currency: str
    supplier_price: int
    supplier_base_price: int
    customer_price: int
    customer_base_price: int
    reseller_price: int
    reseller_base_price: int
    approved: bool = False
    customer_to_price: int = 0
    customer_to_weight: int = 0
    customer_to_qty: int = 0
    supplier_to_price: int = 0
    supplier_to_weight: int = 0
    supplier_to_qty: int = 0
    reseller_to_price: int = 0
    reseller_to_weight: int = 0
    reseller_to_qty: int = 0


class TransactionSchema(BaseModel):
    id: int
    session: SessionSchema
    customer: UserTypeSchema
    supplier: UserTypeSchema
    location: LocationSchema
    item: ItemSchema
    is_partner: bool = False


# class BuildDocumentSchema(BaseModel):
#     product_variant: ProductVariantSchema
#     user_id: int
#     partner_id: int
#     partner_currency: str
#     delivery: int
#     localization: Optional[str] = ''
#     chip: Optional[str] = ''
#     quality: Optional[str] = ''
#     qty: int
#     user_price: int
#     origin_price: int
#     user_base_price: int
#     reseller_price: int = 0
#     reseller_base_price: int = 0
#     reseller_currency: str = ''
#     exchange_rate: float
#     approved: Optional[bool]
#     approved_qty: int = 0
#     to_price: int
#     to_weight: int
#     to_qty: int
#     reseller_to_price: int = 0
#     reseller_to_weight: int = 0class BuildDocumentResponseSchema(BaseModel):
    status: str = "SUCCESS"
    sales_orders: int = 0
    buy_orders: int = 0

#     reseller_to_qty: int = 0


# class BuildDocumentResponseSchema(BaseModel):
#     status: str = "SUCCESS"
#     sales_orders: int = 0
#     buy_orders: int = 0
