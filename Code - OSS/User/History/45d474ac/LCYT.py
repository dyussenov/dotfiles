from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    database_login: str = os.getenv("DATABASE_LOGIN")
    database_password: str = os.getenv("DATABASE_PASSWORD")
    database_host: str = os.getenv("DATABASE_HOST")
    database_port: int = os.getenv("DATABASE_PORT")
    database_url: str = f'mongodb://{database_login}:{database_password}@{database_host}:{database_port}'
    
    redis_host: str = os.getenv("REDIS_HOST")
    redis_port: int = os.getenv("REDIS_PORT")
    redis_password: str = os.getenv("REDIS_PASSWORD")
    
    allowed_urls: str = os.getenv("ALLOWED_URLS")
    
    jwt_secret: str = os.getenv("JWT_SECRET")
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
