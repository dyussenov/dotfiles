
# Bootstrap for FastAPI services

## TOML config file

Sadly, Pydantic's Settings class does not support toml files. This bootstrap uses custom toml parsing and validating class

## Only SQL allowed

Bootstrap uses SQLAlchemy as ORM which does not support nosql dabases

## Usage

- run ```docker```