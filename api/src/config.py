from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
