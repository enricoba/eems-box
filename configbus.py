class ConfigBus(object):
    def __init__(self):
        self.conf = 'eems.conf'

    def _read(self):
        with open(self.conf, 'r') as conf:
            return conf.readlines()

    def _write(self, content):
        with open(self.conf, 'w') as conf:
            conf.write(content)


class Interval(ConfigBus):
    def read(self):
        conf = self._read()
        value = [c for c in conf if c.strip('\n')[:8] == 'interval'][0].split(' ')[-1:][0].strip('\n')
        return int(value)

    def write(self, value):
        conf = self._read()
        conf_new = ''
        line = [c for c in conf if c.strip('\n')[:8] == 'interval'][0]
        for x in range(len(conf)):
            if conf[x] == line:
                conf_new += 'interval {}\n'.format(value)
            else:
                conf_new += conf[x]
        self._write(conf_new)


class Monitoring(ConfigBus):
    def read(self):
        conf = self._read()
        value = [c for c in conf if c.strip('\n')[:10] == 'monitoring'][0].split(' ')[-1:][0].strip('\n')
        return bool(value)

    def write(self, value):
        conf = self._read()
        conf_new = ''
        line = [c for c in conf if c.strip('\n')[:10] == 'monitoring'][0]
        for x in range(len(conf)):
            if conf[x] == line:
                conf_new += 'monitoring {}\n'.format(value)
            else:
                conf_new += conf[x]
        self._write(conf_new)


Interval = Interval()
Monitoring = Monitoring()
