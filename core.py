from messagebus import Bus
from configbus import Monitoring
from threading import Thread
import subprocess
import time


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
        Bus.logger(source='core', msg='{}-job startup'.format(self.job_name))

    def term(self):
        if self.status is True:
            Bus.logger(source='core', msg='{}-job shutdown'.format(self.job_name))
            if self.job_name == 'logger':
                time.sleep(3)
            self.job.terminate()
            self.job.wait()
            self.status = False

    def poll(self):
        if self.status is True:
            return self.job.poll()


def job_control(job, ab):
    while True:
        # message structure
        # message = {'action': 'start/stop'}

        message = Bus.receive(ab)
        if message['action'] == 'stop':
            job.term()
            # setting monitoring flag false
            if job.job_name == 'monitoring':
                Monitoring.write(False)
        elif message['action'] == 'start':
            job.start()
            # setting monitoring flag true
            if job.job_name == 'monitoring':
                Monitoring.write(True)


def main():
    logger = JobHandler('logger.py')
    monitor = JobHandler('monitoring.py')
    try:
        Bus.logger(source='core', msg='core-job startup')
        logger.start()

        t = Thread(target=job_control, args=(monitor, 'display', ))
        t.setDaemon(True)
        t.start()

        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        print 'KeyboardInterrupt'
        monitor.term()
        logger.term()


if __name__ == '__main__':
    main()
