import pika
import json


class __MessageBus(object):
    def __init__(self, host=None):
        """Public object *MessageBus* provides functions to interact with the message interface.


        :param host: *string*
        """
        if host is None:
            _host = 'localhost'
        else:
            _host = host

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=_host))
        self.channel = self.connection.channel()
        self.message = None

    def _send(self, queue, body):
        """Private function *__connect* reconnects to the host and establishes the channel after disconnect function has been
        called.

        :param queue: *string*.
        :return: *None*
        """
        body = json.dumps(body)
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='', routing_key=queue, body=body)

    def disconnect(self):
        """Private function *__disconnect* closes the connection.

        :return: *None*
        """
        self.connection.close()

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

    def _receive(self, queue):
        """Public function *receive* can be called to receive messages from the queue.

        :param queue: *string*
        :return: *dict*
        """
        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(self.__callback, queue=queue, no_ack=True)
        self.channel.start_consuming()
        message = self.message
        self.message = None
        return message


class _Logger(__MessageBus):
    def __init__(self):
        super(_Logger, self).__init__()
        self.queue = 'logger'

    def send(self, level='WARNING', source=None, msg=None):
        body = {'level':     level,
                'source':    source,
                'msg':       msg}
        self._send(self.queue, body)

    def receive(self):
        return self._receive(self.queue)


class _Display(__MessageBus):
    def __init__(self):
        super(_Display, self).__init__()
        self.queue = 'display'

    def send(self, action):
        body = {'action':   action}
        self._send(self.queue, body)

    def receive(self):
        return self._receive(self.queue)


class Bus(object):
    def __init__(self):
        self.logger = _Logger()
        self.display = _Display()

Bus = Bus()
