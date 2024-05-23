from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from app.documents.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    ...
    yield
    ...


def init_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, docs_url=settings.DOCS_URL,
                  redoc_url=settings.REDOC_URL, openapi_url=settings.OPENAPI_URL,
                  root_path=settings.GLOBAL_SERVICE_PATH,
                  debug=settings.DEBUG, lifespan=lifespan)
    return app


if __name__ == "__main__":
    fastapi_app = init_app()
    uvicorn.run(fastapi_app, host="0.0.0.0", port=settings.APP_PORT)
