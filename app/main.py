from fastapi import FastAPI
import uvicorn


def init_app() -> FastAPI:
    app = FastAPI()
    return app


if __name__ == "__main__":

    fastapi_app: FastAPI = init_app()

    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000, access_log='INFO')

