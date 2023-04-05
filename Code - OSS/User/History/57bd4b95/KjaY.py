from tomli import load

class Settings:

    def __init__(self, config_path):
        with open(config_path, mode="rb") as fp:
            config = load(fp)

        match config:
            case {
                "db_type": str(),
                "db_path": str(),
                "allowed_urls": list()
            }:
                for k, v in config.items():
                    setattr(self, k, v)
            case _:
                raise ValueError(f"invalid configuration: {config}")

setting = Settings('config.toml')

print(setting.db_path)