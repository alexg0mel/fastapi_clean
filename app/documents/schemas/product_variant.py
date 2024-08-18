from pydantic import BaseModel


class BrandSchema(BaseModel):
    id: int
    name: str


class CategorySchema(BaseModel):
    id: int
    name: str


class ProductVariantSchema(BaseModel):
    id: int
    name: str
    brand: BrandSchema
    category: CategorySchema
    product_id: int = 0


class ShortProductVariantSchema(BaseModel):
    id: int
    name: str
