from datetime import date
from uuid import UUID

from app.lib.models.base import Base

from .enums import Stage, TypeUser, DocumentStatus, AlphaGroup
from .item import Item


class Document(Base):
    """
    Documents have stages of change. One stage follows from the previous one.
    The life cycle by stages of documents is as follows: tradezone order (TO),
    proforma invoice (PI), invoice(s) (IN), canceled document (CD).

    The beginning of the chain (the first document) is stored in the base_uuid field,
    the next document is stored in the next_uuid field
    """

    uuid: UUID
    base_uuid: UUID
    stage: Stage
    location_key: str
    number: str
    date: date
    session_id: int
    user_id: int
    type_user: TypeUser
    currency: str
    user_currency: str
    is_partner: bool = False
    status: DocumentStatus = DocumentStatus.Forming
    alpha_group: AlphaGroup = AlphaGroup.Empty
    next_uuid: UUID | None = None
    items: list[Item] = []
    sum: int = 0
    user_sum: int = 0
    qty: int = 0
