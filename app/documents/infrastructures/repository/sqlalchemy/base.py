from fastapi import Depends
from sqlalchemy import delete

from sqlalchemy.ext.asyncio import AsyncSession

from app.documents.infrastructures.clients.session import get_session


class BaseDBRepository:
    def __init__(self,
                 session: AsyncSession = Depends(get_session)):
        self.session = session

    async def load_entity(self, entity_type, pk):
        entity = await self.session.get(entity_type, pk)
        return entity

    async def save_entity(self, entity, **kwargs):
        self.session.add(entity)
        await self.session.commit()
        return await self.refresh(entity, **kwargs)

    async def delete_entity(self, entity):
        await self.session.delete(entity)
        await self.session.commit()

    async def bulk_create(self, entities):
        for entity in entities:
            self.session.add(entity)
        await self.session.commit()
        return entities

    async def delete_all(self, model):
        await self.session.execute(delete(model))
        await self.session.commit()

    async def refresh(self, entity, **kwargs):
        await self.session.refresh(entity, **kwargs)
        return entity
