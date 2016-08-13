from messagebus import MessageBus


message = {'level':     'WARNING',
           'source':    'core',
           'msg':       'Hi, Im the core!'}

MessageBus.send('logger', message)
# MessageBus.logger('send.py', message)
