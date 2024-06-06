from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    DATABASE_ECHO: bool = True
    POSTGRES_CONNECTION_URI: SecretStr
    PATH_TO_CERTS: Path = Path(__file__).parent.parent / "certs"
    ALGORITHM: SecretStr
    JWT_SECRET: SecretStr

    model_config = SettingsConfigDict(
        env_file=(".env", "stack.env"), env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
