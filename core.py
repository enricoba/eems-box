import time
import subprocess
from messagebus import MessageBus
from threading import Thread


# start jobs
class JobHandler(object):
    def __init__(self, job):
        self.job_name = job[:-3]
        self.command = ['python', '{}'.format(job)]
        self.job = object
        self.status = False

    def start(self):
        self.job = subprocess.Popen(self.command)
        self.status = True
        time.sleep(1)
        MessageBus.logger(source='core', msg='{}-job startup'.format(self.job_name))

    def term(self):
        if self.status is True:
            MessageBus.logger(source='core', msg='{}-job shutdown'.format(self.job_name))
            if self.job_name == 'logger':
                time.sleep(1)
            self.job.terminate()
            self.status = False

    def poll(self):
        if self.status is True:
            return self.job.poll()


def job_control(job):
    while True:
        # message structure
        # message = {'action': 'start/stop'}

        message = MessageBus.receive('display')
        if message['action'] == 'stop':
            job.term()
        elif message['action'] == 'start':
            job.start()


def main():
    try:
        MessageBus.logger(source='core', msg='core-job startup')
        logger = JobHandler('logger.py')
        logger.start()

        display = JobHandler('monitoring.py')
        t = Thread(target=job_control, args=(display, ))
        t.setDaemon(True)
        t.start()

        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        print 'KeyboardInterrupt'


if __name__ == '__main__':
    main()
