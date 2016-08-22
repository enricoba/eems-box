import pika
import json


class MessageBus(object):
    def __init__(self, host=None):
        """Public object *MessageBus* provides functions to interact with the message interface.


        :param host: *string*
        """
        if host is None:
            self.host = 'localhost'
        else:
            self.host = host

        self.connection = None
        self.channel = None
        self.message = None

    def __connect(self, queue):
        """Private function *__connect* reconnects to the host and establishes the channel after disconnect function has been
        called.

        :param queue: *string*.
        :return: *None*
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue)

    def __disconnect(self):
        """Private function *__disconnect* closes the connection.

        :return: *None*
        """
        self.connection.close()
        self.connection = None
        self.channel = None
        self.message = None

    def send(self, queue, message):
        """Public function *send* delivers messages to the RabbitMQ server.

        :param queue: *string*
        :param message: *dict*
        :return: *None*
        """
        self.__connect(queue=queue)
        body = json.dumps(message)
        self.channel.basic_publish(exchange='', routing_key=queue, body=body)
        self.__disconnect()

    def logger(self, level='WARNING', source=None, msg=None):
        """Public function *logger* delivers messages to the RabbitMQ server.

        :param level: *string*
        :param source: *string*
        :param msg: *string*
        :return: *None*
        """
        message = {'level':     level,
                   'source':    source,
                   'msg':       msg}
        self.__connect(queue='logger')
        body = json.dumps(message)
        self.channel.basic_publish(exchange='', routing_key='logger', body=body)
        self.__disconnect()

    def display(self, action):
        """Public function *display* delivers messages to the RabbitMQ server.

        :param action: *string*
        :return: *None*
        """
        message = {'action': action}
        self.__connect(queue='display')
        body = json.dumps(message)
        self.channel.basic_publish(exchange='', routing_key='display', body=body)
        self.__disconnect()

    def __callback(self, ch, method, properties, body):
        """Private function *__callback* catches the values returned by the message.

        :param ch:
        :param method:
        :param properties:
        :param body: *string*
        :return: *None*
        """
        self.message = json.loads(body)
        self.channel.stop_consuming()

    def receive(self, queue):
        """Public function *receive* can be called to receive messages from the queue.

        :param queue: *string*
        :return: *dict*
        """
        self.__connect(queue=queue)
        self.channel.basic_consume(self.__callback, queue=queue, no_ack=True)
        self.channel.start_consuming()
        message = self.message
        self.__disconnect()
        return message

Bus = MessageBus()
