from yoyo import read_migrations
from yoyo import get_backend


import logging
from logger import init_es_log

from config import settings

init_es_log(logging.INFO)
logger = logging.getLogger(__name__)

backend = get_backend(settings.POSTGRES_DSN)
migrations = read_migrations('migrations')
logger.info(migrations)

with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))


