import time
from configbus import Interval


def main():
    print 'monitoring on'

    # get interval from DB
    interval = Interval.read()

    timestamp = int(time.time() / interval) * interval
    timestamp += interval
    time.sleep(timestamp - time.time())

    while True:
        # call for values and write to DB
        print 'monitoring every {} seconds'.format(interval)
        timestamp += interval
        time.sleep(timestamp - time.time())


if __name__ == '__main__':
    main()
