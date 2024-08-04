from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from app.documents.config import settings
from app.lib.logger import init_es_log
from app.lib.context import context_header
from app.documents.api import router
from app.documents.infrastructures.clients import close_connections


@asynccontextmanager
async def lifespan(_: FastAPI):
    ...
    yield
    await close_connections()


def init_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, docs_url=settings.DOCS_URL,
                  redoc_url=settings.REDOC_URL, openapi_url=settings.OPENAPI_URL,
                  root_path=settings.GLOBAL_SERVICE_PATH,
                  debug=settings.DEBUG, lifespan=lifespan)
    app.include_router(router)
    app.middleware('http')(context_header)
    return app


if __name__ == "__main__":
    init_es_log(settings.LOGGING_LEVEL)
    fastapi_app = init_app()
    uvicorn.run(fastapi_app, host="0.0.0.0", port=settings.APP_PORT)
