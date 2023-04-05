from pydantic import BaseSettings


class Settings(BaseSettings):
    ALLOWED_HOSTS: str
    PS_URL: str
    PS_PORT: str
    PS_LOGIN: str
    PS_DB_NAME: str
    PS_PASSWORD: str
    REDIS_URL: str
    REDIS_PORT: str

    class Config:
        env_file = ".env"

settings = Settings()
