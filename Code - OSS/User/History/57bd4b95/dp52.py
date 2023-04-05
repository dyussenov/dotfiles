from tomli import load

with open("config.toml", mode="rb") as fp:
    config = load(fp)

print(config)

match config:
    case {
        "user": {"player_x": {"color": str()}, "player_o": {"color": str()}},
        "constant": {"board_size": int()},
        "server": {"url": str()},
    }:
        pass
    case _:
        raise ValueError(f"invalid configuration: {config}")


