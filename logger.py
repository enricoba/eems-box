from messagebus import Bus
import logging

# Message to Log:
# level: DEBUG, INFO, WARNING, ERROR, CRITICAL
# source: str() z.B. Display-Job, GSM-Job, Core-Job, ...
# msg: str()


# Define Functions for Logger
class Logger(object):
    def __init__(self):
        # Define Logger
        log_format = '[*] %(asctime)s %(levelname)s %(message)s'
        log_date_format = '%Y-%m-%d %H:%M:%S'
        log_file = 'eems.log'

        logging.basicConfig(level=logging.WARNING,
                            format=log_format,
                            datefmt=log_date_format,
                            filename=log_file)

        self.logger = logging.getLogger('eems')
        self.log_lvl_info = {'DEBUG':       10,
                             'INFO':        20,
                             'WARNING':     30,
                             'ERROR':       40,
                             'CRITICAL':    50}

    def write_log(self, msg_as_dict):
        """Public function *write_log* writes messages to the log file.

        :param msg_as_dict: *dict*
        :return: *None*
        """
        self.logger.log(self.log_lvl_info[msg_as_dict[u'level']],
                        '{}: {}'.format(msg_as_dict[u'source'],
                                        msg_as_dict[u'msg']))


def main():
    logger = Logger()
    while True:
        message = Bus.receive('logger')
        logger.write_log(message)

if __name__ == '__main__':
    main()
