from messagebus import Bus


message = {'level':     'WARNING',
           'source':    'core',
           'msg':       'Hi, Im the core!'}

Bus.send('logger', message)
# Bus.logger('send.py', message)
