import time


def timer(n, m=10):
    '''''
    每n秒执行一次
    '''
    count = 0
    while True:
        count = count + 1
        if count > m:
            break
        print(time.strftime('%Y-%m-%d %X', time.localtime()))
        myTask()  # 此处为要执行的任务
        time.sleep(n)


def myTask():
    print("this is my task")


if __name__ == '__main__':
    timer(500)
