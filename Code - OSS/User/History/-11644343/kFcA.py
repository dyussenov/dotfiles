from pydantic import BaseSettings


class Settings(BaseSettings):
    ALLOWED_HOSTS: str
    REDIS_URL: str
    REDIS_PORT: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
