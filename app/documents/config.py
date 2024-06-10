from typing import Optional, Any, Union
from functools import lru_cache
from pydantic import Field, field_validator, PostgresDsn
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
    DATABASE_ECHO: bool = False
    LOGGING_LEVEL: str = "INFO"
    ACCESS_LOG: bool = False
    SERVICE_TOKEN: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVICE: str
    POSTGRES_DB: str = Field(alias="DOCUMENT_POSTGRES_DB", default="documents_service")
    POSTGRES_PORT: int = 5432

    POSTGRES_DSN: Union[Optional[PostgresDsn], Optional[str]] = None

    @field_validator("POSTGRES_DSN", mode="before")
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        return str(
            PostgresDsn.build(
                scheme="postgresql",
                username=values.data.get("POSTGRES_USER"),
                password=values.data.get("POSTGRES_PASSWORD"),
                host=values.data.get("POSTGRES_SERVICE"),
                path=values.data.get('POSTGRES_DB') or '',
                port=values.data.get('POSTGRES_PORT'),
            )
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
