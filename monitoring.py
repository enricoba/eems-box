from configbus import Interval
import time


def main():
    # get interval from DB
    print 'monitoring started'
    interval = Interval.read()
    print interval
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
