from interface import RMI


bus = RMI()
message = {'level':     'WARNING',
           'source':    'core',
           'msg':       'Hi, Im the core!'}
bus.send_single('logger', message)

