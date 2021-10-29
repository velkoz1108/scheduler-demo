import sched
import time

s = sched.scheduler(time.time, time.sleep)


def job(inc):
    print("job start: %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    time.sleep(2)
    print("job end: %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    s.enter(inc, 0, job, (inc,))


if __name__ == '__main__':
    s.enter(1, 0, job, (10,))
    s.run()
