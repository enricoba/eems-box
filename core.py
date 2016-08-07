import subprocess
import time


# start jobs
class JobHandler(object):
    def __init__(self, job):
        command = ['python', '{}'.format(job)]
        self.job = subprocess.Popen(command)

    def term(self):
        self.job.terminate()

    def poll(self):
        return self.job.poll()


def main():
    logger = JobHandler('message-interface/receive.py')

    message = {
        'action':   'start',
        'job':      'logger'
    }

    message = {
        'event':    str(),  # 'error'/'warning'/'debug'/'info'
        'content':  str()   # content of the event message
    }

    while True:
        # 1. position = wait for message

        if message['action'] == 'stop':
            if message['job'] == 'logger':
                logger.term()


if __name__ == '__main__':
    main()
