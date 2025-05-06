from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_PATH = Path(__file__).resolve().parent.parent


class DatabaseSettings(BaseModel):
    url: PostgresDsn


class AuthSettings(BaseModel):
    secret_key: str
    algorithm: str
    salt: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[BASE_PATH / ".env.template", BASE_PATH / ".env"],
        extra="ignore",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    db: DatabaseSettings
    auth: AuthSettings


settings = Settings()
