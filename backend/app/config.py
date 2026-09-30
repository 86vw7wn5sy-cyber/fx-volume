from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FX Volume"
    debug: bool = True
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173", "*"]

    class Config:
        env_file = ".env"


settings = Settings()
