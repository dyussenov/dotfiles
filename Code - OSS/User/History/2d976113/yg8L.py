from tomli import load

class Settings:

    def __init__(self, config_path):
        with open(config_path, mode="rb") as fp:
            config = load(fp)

        match config:
            case {
                "sendpulse_url": str(),
                "client_id": str(),
                "client_secret": str(),
                "sms_text": str(),
                "allowed_urls": list()
            }:
                for k, v in config.items():
                    setattr(self, k, v)

            case _:
                raise ValueError(f"invalid configuration: {config}")

settings = Settings('config.toml')

