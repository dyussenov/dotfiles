from pydantic import BaseSettings


class Settings(BaseSettings):
    database_login: str = 'workaus'
    database_password: str = 'CHANGEME'
    database_host: str = '127.0.0.1'
    database_port: int = 27017
    database_url: str = f'mongodb://{database_login}:{database_password}@{database_host}:{database_port}'

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
