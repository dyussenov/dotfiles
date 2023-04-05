from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

from database import engine
Base = declarative_base()

class TextField(Base):
    __tablename__ = 'Text'
    __table_args__ = {
        'sqlite_autoincrement': True
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    value_ru = Column(String)
    value_kz = Column(String)


Base.metadata.create_all(bind=engine)
