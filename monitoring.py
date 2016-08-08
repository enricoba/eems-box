import time


def main():
    print 'monitoring on'

    # get interval from DB
    interval = 2

    timestamp = int(time.time() / interval) * interval
    timestamp += interval
    time.sleep(timestamp - time.time())

    while True:
        # call for values
        print 'monitoring every 2 seconds'
        timestamp += interval
        time.sleep(timestamp - time.time())


if __name__ == '__main__':
    main()
