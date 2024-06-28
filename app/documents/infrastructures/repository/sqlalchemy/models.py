from datetime import datetime


from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.documents.models.enums import DocumentStatus, AlphaGroup


class Base(DeclarativeBase):
    pass


class AuditModel:
    created = Column(DateTime(timezone=True), default=datetime.now)
    created_by = Column(String, default="", nullable=False)
    updated = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String, default="", nullable=False)


class DocumentModel(Base, AuditModel):
    __tablename__ = "document"
    uuid = Column(UUID(as_uuid=True), primary_key=True)
    base_uuid = Column(UUID(as_uuid=True), nullable=False)
    stage = Column(String, nullable=False)
    location_key = Column(String, nullable=False)
    number = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    session_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    type_user = Column(String, nullable=False)
    currency = Column(String(6), nullable=False)
    user_currency = Column(String(6), nullable=False)
    is_partner = Column(Boolean, nullable=False, default=False)
    status = Column(String, nullable=False, default=DocumentStatus.Forming)
    alpha_group = Column(String, nullable=False, default=AlphaGroup.Empty)
    next_uuid = Column(UUID(as_uuid=True))

    items = relationship("ItemModel")


class ItemModel(Base):
    __tablename__ = "item"
    uuid = Column(UUID(as_uuid=True), primary_key=True)
    document_uuid = Column(UUID(as_uuid=True), ForeignKey("document.uuid"))
    product_id = Column(Integer, nullable=False)
    product_variant_id = Column(Integer, nullable=False)
    product_variant_name = Column(String, nullable=False)
    localization = Column(String)
    chip = Column(String)
    quality = Column(String)
    qty = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    user_price = Column(Integer, nullable=False)
    delivery_date = Column(DateTime(timezone=True), nullable=False)
