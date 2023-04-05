from pydantic import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    database_login: str = os.getenv("DATABASE_LOGIN")
    database_password: str = os.getenv("DATABASE_PASSWORD")
    database_host: str = '127.0.0.1'
    database_port: int = 27017
    database_url: str = f'mongodb://{database_login}:{database_password}@{database_host}:{database_port}'
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')


print(settings.database_login)