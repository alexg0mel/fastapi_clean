from fastapi import FastAPI
import uvicorn

from app.documents import ddd
from app.lib import l


def init_app() -> FastAPI:
    app = FastAPI()
    return app


if __name__ == "__main__":

    fastapi_app: FastAPI = init_app()

    print(ddd, l)
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000, access_log='INFO')

