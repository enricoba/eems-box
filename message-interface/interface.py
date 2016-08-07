import pika
import json


class RMI(object):
    def __init__(self, host=None):
        """Public object *RMI* provides functions to interact with the message interface.


        :param host:
            Expects *string*
        """
        if host is None:
            self.host = 'localhost'
        else:
            self.host = host

        # initial connection
        self.connection = None
        self.channel = None
        self.message = None

    def __connect(self, queue):
        """Private function *__connect* reconnects to the host and establishes the channel after disconnect function has been
        called.

        :param queue:
            Expects *string*.
        :return:
            Returns *None*.
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue)

    def __disconnect(self):
        """Private function *__disconnect* closes the connection.

        :return:
            Return *None*.
        """
        self.connection.close()
        self.connection = None
        self.channel = None

    def send_single(self, queue, message):
        """Public function *send_single* delivers messages to the RabbitMQ server.

        :param queue:
            Expects *string*.
        :param message:
            Expects *dict*.
        :return:
            Returns *None*.
        """
        self.__connect(queue=queue)
        body = json.dumps(message)
        self.channel.basic_publish(exchange='', routing_key=queue, body=body)
        self.__disconnect()

    def __callback(self, ch, method, properties, body):
        """Private function *__callback* catches the values returned by the message.

        :param ch:
        :param method:
        :param properties:
        :param body:
        :return:
            Returns *None*.
        """
        # self.__disconnect()
        print body
        self.message = body
        self.channel.stop_consuming()

    def receive(self, queue):
        """Public function *receive* can be called to receive messages from the queue.

        :param queue:
            Expects *string*.
        :return:
            Returns *dict*.
        """
        self.__connect(queue=queue)
        self.channel.basic_consume(self.__callback, queue=queue, no_ack=True)
        self.channel.start_consuming()
        self.__disconnect()
        return self.message
