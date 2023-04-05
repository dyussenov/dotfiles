from pydantic import BaseSettings
from tomli import load

with open("config.toml", mode="rb") as fp:
    config = tomli.load(fp)

print(config)

class Settings(BaseSettings):
    database_url: str
    allowed_urls: str
