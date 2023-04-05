from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    allowed_urls: str
