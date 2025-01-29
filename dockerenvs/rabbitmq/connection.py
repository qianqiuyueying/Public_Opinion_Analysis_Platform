import pika
from config import *

class RabbitMQConnection:
    connection = None
    channel = None

    @classmethod
    def connect(cls):
        """
        返回一个连接对象
        1. 判断连接是否存在
        2. 如果不存在则创建一个新的连接
        3. 返回连接对象
        """
        try:
            if not cls.connection or cls.connection.is_closed:
                cls.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
                cls.channel = cls.connection.channel()
            yield cls.channel
        finally:
            cls.close
    
    @classmethod
    def close(cls):
        """
        关闭连接
        1. 判断连接是否存在
        2. 如果存在则关闭连接
        3. 清空连接对象
        """
        if cls.channel:
            cls.channel.close()
        if cls.connection:
            cls.connection.close()
        cls.connection = None
        cls.channel = None

    @classmethod
    def __del__(cls):
        """
        析构函数
        1. 关闭连接
        """
        cls.close()
