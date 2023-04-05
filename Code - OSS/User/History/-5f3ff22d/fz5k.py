from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()
Base.metadata.create_all(bind=engine)
