from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_PORT: int = Field(alias="DOCUMENT_APP_PORT", default=8000)
    PROJECT_NAME: str = Field(alias="DOCUMENT_PROJECT_NAME", default="service")

    GLOBAL_SERVICE_PATH: str = Field(alias="DOCUMENT_GLOBAL_SERVICE_PATH", default="")
    DOCS_URL: str = Field(alias="DOCUMENT_DOCS_URL", default="/docs")
    REDOC_URL: str = Field(alias="DOCUMENT_REDOC_URL", default="/redoc")
    DOCUMENT_OPENAPI_URL: str = "/openapi.json"
    OPENAPI_URL: str = Field(alias="DOCUMENT_OPENAPI_URL", default="/openapi.json")

    DEBUG: bool = False
    LOGGING_LEVEL: str = "INFO"
    ACCESS_LOG: bool = False
    SERVICE_TOKEN: str

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
