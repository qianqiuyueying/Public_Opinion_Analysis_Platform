from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import *

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def init_db() -> None:
    Base.metadata.create_all(engine)

def get_session() -> Session:
    """
    获取数据库会话对象Session
    :return: Session
    """
    return Session()