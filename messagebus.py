import pika
import json


class MessageBus(object):
    def __init__(self, host=None):
        """Public object *MessageBus* provides functions to interact with the message interface.


        :param host: *string*
        """
        if host is None:
            _host = 'localhost'
        else:
            _host = host

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=_host))
        self.channel = dict()
        self.message = dict()

    def __send(self, queue, body):
        """Private function *__connect* reconnects to the host and establishes the channel after disconnect function has been
        called.

        :param queue: *string*.
        :return: *None*
        """
        channel = self.connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=body)

    def disconnect(self):
        """Private function *__disconnect* closes the connection.

        :return: *None*
        """
        self.connection.close()

    def send(self, queue, message):
        """Public function *send* delivers messages to the RabbitMQ server.

        :param queue: *string*
        :param message: *dict*
        :return: *None*
        """
        # self.__connect(queue=queue)
        body = json.dumps(message)
        self.__send(queue, body)
        # self.channel.basic_publish(exchange='', routing_key=queue, body=body)
        # self.__disconnect()

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
        # self.__connect(queue='logger')
        body = json.dumps(message)
        self.__send('logger', body)

    def display(self, action):
        """Public function *display* delivers messages to the RabbitMQ server.

        :param action: *string*
        :return: *None*
        """
        message = {'action': action}
        # self.__connect(queue='display')
        body = json.dumps(message)
        self.__send('display', body)
        # self.channel.basic_publish(exchange='', routing_key='display', body=body)
        # self.__disconnect()

    def __callback(self, ch, method, properties, body, channel):
        """Private function *__callback* catches the values returned by the message.

        :param ch:
        :param method:
        :param properties:
        :param body: *string*
        :return: *None*
        """
        self.message = json.loads(body)
        channel.stop_consuming()
        print json.loads(body)
        # ch.basic_ack(delivery_tag=method.delivery_tag)

    def receive(self, queue):
        """Public function *receive* can be called to receive messages from the queue.

        :param queue: *string*
        :return: *dict*
        """
        # self.__connect(queue=queue)
        channel = self.connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_consume(self.__callback, queue=queue, no_ack=True)

        channel.start_consuming()
        message = self.message
        # self.__disconnect()
        return message

    class Receive(object):
        def logger(self):
            print 'receiver logger'

Bus = MessageBus()
