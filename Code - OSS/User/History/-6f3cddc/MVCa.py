from pydantic import BaseSettings


class Settings(BaseSettings):
    database_login: str
    database_password: str
    database_host: str = '127.0.0.1'
    database_port: int = 27017
    database_url: str = f'mongodb://{database_login}:{database_password}@{database_host}:{database_port}'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)