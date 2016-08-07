import logging

### VARIABLES
# STR
# con_str_01: log format
# con_str_02: log date format
# con_str_03: log file

# DICT
# con_dic_01: Log-level information

### Message to Log:
# level: DEBUG, INFO, WARNING, ERROR, CRITICAL
# source: str() z.B. Display-Job, GSM-Job, Core-Job, ...
# msg: str()


# Define Functions for Logger
class Log(object):
    def __init__(self):
        # Define Logger
        con_str_01 = '%(asctime)s %(levelname)s %(message)s'
        con_str_02 = '%Y-%m-%d %H:%M:%S'
        con_str_03 = 'eems.log'

        logging.basicConfig(level=logging.DEBUG,
                            format=con_str_01,
                            datefmt=con_str_02,
                            filename=con_str_03)

        self.logger = logging.getLogger('eems')
        self.con_dic_01 = {'DEBUG': 10,
                           'INFO': 20,
                           'WARNING': 30,
                           'ERROR': 40,
                           'CRITICAL': 50}

    def write_log(self, msg_as_dict):
        """
        Function to write logs to the log-flie
        :param msg_as_dict:
        Message to log given as a dict. Key of the Dict are level, source and msg

        :return:
        nothing
        """
        self.logger.log(self.con_dic_01[msg_as_dict['level']], '{}_{}'.format(msg_as_dict['source'], msg_as_dict['msg']))


# while True:
#     msg_2_log =
#     write_log(msg_2_log)


# EXAMPLE
test_dict = {'level':   'CRITICAL',  # MUSS grossgeschrieben werden
             'source':  'Monitoring-Job',
             'msg':     'Read DS18B20 failed'}

logger = Log()
logger.write_log(test_dict)


