import time
import subprocess
from messagebus import MessageBus


bus = MessageBus()


# start jobs
class JobHandler(object):
    def __init__(self, job):
        self.job_name = job[:-3]
        print self.job_name
        command = ['python', '{}'.format(job)]
        self.job = subprocess.Popen(command)
        time.sleep(1)
        bus.send_logger(source='core', msg='{}-job startup'.format(self.job_name))

    def term(self):
        bus.send_logger(source='core', msg='{}-job shutdown'.format(self.job_name))
        if self.job_name == 'logger':
            time.sleep(1)
        self.job.terminate()

    def poll(self):
        return self.job.poll()


def main():
    bus.send_logger(source='core', msg='core-job startup')
    logger = JobHandler('logger.py')
    logger.term()


if __name__ == '__main__':
    main()
