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

    def get_db_uri(self):
        print(f"postgres://{self.PS_LOGIN}:{self.PS_PASSWORD}@{self.PS_URL}:5432/{self.PS_DB_NAME}")
        return f"postgres://{self.PS_LOGIN}:{self.PS_PASSWORD}@{self.PS_URL}:5432/{self.PS_DB_NAME}"

    class Config:
        env_file = ".env"

settings = Settings()
