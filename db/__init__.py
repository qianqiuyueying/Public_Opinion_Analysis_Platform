# 导入必要的模块
from sqlalchemy import create_engine  # 用于创建数据库引擎
from sqlalchemy.orm import sessionmaker, Session  # 用于创建会话工厂
from sqlalchemy.ext.declarative import declarative_base  # 用于创建基类
from .config import *  # 从配置文件中导入所有配置

# 创建数据库引擎
# DATABASE 是从配置文件中导入的数据库连接字符串
# echo=False 表示不打印SQL语句到控制台
engine = create_engine(DATABASE_URL, echo=False)

# 创建一个基类，所有的模型类都将继承这个基类
Base = declarative_base()
Session = sessionmaker(bind=engine)



def init_db() -> None: 
    """
    加载数据库表
    这个函数会根据继承自 Base 的所有模型类定义的表结构，
    在数据库中创建相应的表。
    如果表已经存在，则不会重复创建。
    """
    Base.metadata.create_all(engine)

def get_session():
    """
    获取数据库会话
    返回一个数据库会话对象，可以用来执行数据库操作。
    """
    # 创建一个会话工厂，绑定到上面创建的数据库引擎
    try:
        session = Session(autocommit=False, autoflush=False)
        yield session
    finally:
        session.close()