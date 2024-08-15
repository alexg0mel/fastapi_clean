from uuid import UUID

from app.lib.models.base import Base

from .imei import Imei


class Box(Base):
    uuid: UUID
    number: str
    imeis: list[Imei] = []
