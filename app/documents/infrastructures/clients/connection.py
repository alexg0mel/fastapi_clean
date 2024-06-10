from app.lib.infrastructures.clients.connection import ConnectionPool

from app.documents.config import settings


pool = ConnectionPool(settings.POSTGRES_DSN)
