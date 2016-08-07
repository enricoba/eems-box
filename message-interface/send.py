import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = {
    '1.': 10,
    '2.': 30
}

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(message))
print(" [x] Sent 'Hello World!'")
connection.close()
