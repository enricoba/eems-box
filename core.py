import time
import subprocess
from messagebus import MessageBus


# start jobs
class JobHandler(object):
    def __init__(self, job):
        command = ['python', '{}'.format(job), '&']
        self.job = subprocess.Popen(command)
        time.sleep(1)

    def term(self):
        time.sleep(1)
        self.job.terminate()

    def poll(self):
        return self.job.poll()


def main():
    bus = MessageBus()
    bus.send_logger(source='core', msg='core-job startup')

    logger = JobHandler('logger.py')
    print 'send message'
    bus.send_logger(source='core', msg='logger-job startup')

    print 'vor sleep'
    bus.send_logger(source='core', msg='logger-job shutdown')
    logger.term()


if __name__ == '__main__':
    main()
