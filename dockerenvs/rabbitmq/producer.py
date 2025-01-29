import pika
from connection import RabbitMQConnection
import json

class Producer:
    """
    生产者类
    对外提供发送消息的方法
    """
    def __init__(self):
        self.connection = RabbitMQConnection.connect()

    def set_spider_task(self, task_info: dict) -> None:
        """
        创建爬虫任务
        """
        self.connection.basic_publish(
            exchange='',
            routing_key='task_queue',  # 简单模式下，routing_key即为队列名
            body=json.dumps(task_info),  # rabbitmq服务器中不接受dict，接受json字符串
            properties=pika.BasicProperties(
                delivery_mode=2  # 数据持久化
            )
        )

    def set_analysis_task(self, task_info: dict) -> None:
        """
        创建情感分析任务
        """
        self.connection.basic_publish(
            exchange="",
            routing_key="analysis_queue",
            body=json.dumps(task_info),
            properties=pika.BasicProperties(
                delivery_mode=2  # 数据持久化
            )
        )

    # 示例类 -------------------------------
    def send_message(self, message):
        self.connection.basic_publish(exchange='', routing_key='hello', body=message)
        print(f" [x] Sent '{message}'")
    # 示例类 -------------------------------