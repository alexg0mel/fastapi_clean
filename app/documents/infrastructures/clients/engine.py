from app.documents.config import settings

from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=settings.DATABASE_ECHO)
