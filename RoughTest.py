import time


def sleeper(ipnum):

    num = ipnum
    while True:


        try:
            num = float(num)
            timeout = float(num)  # [seconds]
            print("timeout", timeout, type(timeout))
            timeout_start = time.time()
        except ValueError:
            print("Please enter in a number./n")
            continue

        while time.time() < timeout_start + timeout:
            print('Before: %s' % time.ctime())
            time.sleep(num)
            num = float(input())
            print('Before: %s\n' % time.ctime())


try:
    sleeper(5)
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
