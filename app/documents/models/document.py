from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class Document:
    """
    Documents have stages of change. One stage follows from the previous one.
    The life cycle by stages of documents is as follows: tradezone order (TO),
    proforma invoice (PI), invoice(s) (IN), canceled document (CD).

    The beginning of the chain (the first document) is stored in the base_uuid field,
    the next document is stored in the next_uuid field
    """

    uuid: UUID
    base_uuid: UUID
    stage: str  # todo
    location_key: str
    number: str
    date: date
    session_id: int
    user_id: int
    type_user: str  # buyer, seller todo
    currency: str
    user_currency: str
    is_partner: bool = False
    status: str = 'forming'  # draft, active, forming (default) todo
    alpha_group: str = '-'  # α, β, γ, etc  - (default) todo
    next_uuid: UUID | None = None

    # todo подумать как в документе хранить (или нет? - потому что для каждой стадии будет свой тип айтемов) айтемы
    # todo расписать тодошки выше - енумы
    # todo ООП привязать к стадии тип айтема
