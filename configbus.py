class __ConfigBus(object):
    def __init__(self):
        """Private object *_ConfigBus* provides private functions for various config classes.

            """
        self.conf = 'eems.conf'

    def _read(self):
        """Private function *_read* reads the eems.conf file and returns all lines.

        :return: *list*
        """
        with open(self.conf, 'r') as conf:
            return conf.readlines()

    def _write(self, content):
        """Private function *_write* writes the param content to the eems.conf file.

        :param content: *string*
        :return: *None*
        """
        with open(self.conf, 'w') as conf:
            conf.write(content)


class _Interval(__ConfigBus):
    """Private class *_Interval* inherits from *_ConfigBus* and provides functions to manipulate the interval.

    """
    def read(self):
        """Public function *read* reads and returns the interval value.

        :return: *int*
        """
        conf = self._read()
        value = [c for c in conf if c.strip('\n')[:8] == 'interval'][0].split(' ')[-1:][0].strip('\n')
        return int(value)

    def write(self, value):
        """Public function *write* writes the passed interval value into eems.conf file.

        :param value: *int*
        :return: *None*
        """
        conf = self._read()
        conf_new = ''
        line = [c for c in conf if c.strip('\n')[:8] == 'interval'][0]
        for x in range(len(conf)):
            if conf[x] == line:
                conf_new += 'interval {}\n'.format(value)
            else:
                conf_new += conf[x]
        self._write(conf_new)


class _Monitoring(__ConfigBus):
    """Private class *_Monitoring* inherits from *_ConfigBus* and provides functions to manipulate the monitoring flag.

        """
    def read(self):
        """Public function *read* reads and returns the monitoring flag.

        :return: *bool*
        """
        conf = self._read()
        value = [c for c in conf if c.strip('\n')[:10] == 'monitoring'][0].split(' ')[-1:][0].strip('\n')
        return bool(value)

    def write(self, value):
        """Public function *write* writes the monitoring flag into eems.conf file.

        :param value: *bool* / *int*
        :return: *None*
        """
        conf = self._read()
        conf_new = ''
        line = [c for c in conf if c.strip('\n')[:10] == 'monitoring'][0]
        for x in range(len(conf)):
            if conf[x] == line:
                conf_new += 'monitoring {}\n'.format(int(value))
            else:
                conf_new += conf[x]
        self._write(conf_new)


class Config(object):
    def __init__(self):
        self.interval = _Interval()
        self.monitoring = _Monitoring()


Config = Config()
