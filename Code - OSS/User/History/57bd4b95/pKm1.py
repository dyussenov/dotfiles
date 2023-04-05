from tomli import load

with open("config.toml", mode="rb") as fp:
    config = load(fp)

print(config)




