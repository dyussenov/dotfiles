from tomli import load

with open("config.toml", mode="rb") as fp:
    config = load(fp)

print(config)

match config:
    case {
        "database": {
            "type": str(),
            "sqlite_path": str()
            "database_password": str() or None
            },
        "fastapi": {"allowed_urls": list()}
    }:
        pass
    case _:
        raise ValueError(f"invalid configuration: {config}")


