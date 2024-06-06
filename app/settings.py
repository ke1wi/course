from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_ECHO: bool = True
    POSTGRES_CONNECTION_URI: SecretStr

    model_config = SettingsConfigDict(
        env_file=(".env", "stack.env"), env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
