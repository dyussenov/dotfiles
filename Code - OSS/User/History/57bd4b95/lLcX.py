from tomli import load

class Settings:

    def __init__(self, config_path):
        with open(config_path, mode="rb") as fp:
            config = load(fp)

        match config:
            case {
                "database": {
                    "type": str(),
                    "path": str()
                    },
                "fastapi": {"allowed_urls": list()}
            }:
                for k, v in config.items():
                    setattr(self, k, v)
            case _:
                raise ValueError(f"invalid configuration: {config}")
        self.config = config

setting = Settings('config.toml')

print(setting.config)