from interface import RMI
import logging


# VARIABLES
# STR
# con_str_01: log format
# con_str_02: log date format
# con_str_03: log file

# DICT
# con_dic_01: Log-level information

# Message to Log:
# level: DEBUG, INFO, WARNING, ERROR, CRITICAL
# source: str() z.B. Display-Job, GSM-Job, Core-Job, ...
# msg: str()


# Define Functions for Logger
class Log(object):
    def __init__(self):
        # Define Logger
        con_str_01 = '[*] %(asctime)s %(levelname)s %(message)s'
        con_str_02 = '%Y-%m-%d %H:%M:%S'
        con_str_03 = 'eems.log'

        logging.basicConfig(level=logging.INFO,
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
        """Public function *write_log* writes messages to the log file.

        :param msg_as_dict: *dict*
        :return: *None*
        """
        self.logger.log(self.con_dic_01[msg_as_dict[u'level']],
                        '{}: {}'.format(msg_as_dict[u'source'],
                                        msg_as_dict[u'msg']))


def main():
    logger = Log()
    bus = RMI()
    while True:
        message = bus.receive('logger')
        logger.write_log(message)

if __name__ == '__main__':
    main()
