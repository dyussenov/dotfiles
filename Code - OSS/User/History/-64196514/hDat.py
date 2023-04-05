from tomli import load

class Settings:

    def __init__(self, config_path):
        with open(config_path, mode="rb") as fp:
            config = load(fp)

        match config:
            case {
                "database_login": str(),
                "database_password": str(),
                "database_host": str(),
                "database_port": int(),
                "allowed_urls": list()
            }:
                for k, v in config.items():
                    setattr(self, k, v)

            case _:
                raise ValueError(f"invalid configuration: {config}")
        self.database_url = f'mongodb://{self.database_login}:{self.database_password}@{self.database_host}:{self.database_port}'

settings = Settings('config.toml')
