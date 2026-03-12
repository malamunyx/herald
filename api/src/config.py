from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )

    database_url: str

    api_prefix: str = "/api"


settings = Settings()  # type: ignore
