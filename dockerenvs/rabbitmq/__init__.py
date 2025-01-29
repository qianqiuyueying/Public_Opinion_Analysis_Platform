from connection import RabbitMQConnection

channel = RabbitMQConnection.connect()
# 爬虫任务队列
channel.queue_declare(queue='task_queue', durable=True)
# 情感分析任务队列
channel.queue_declare(queue='analysis_queue', durable=True)