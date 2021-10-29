import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'cron', day_of_week='1-5', hour=11, minute=40)
    scheduler.add_job(job, 'interval', seconds=10, timezone=pytz.timezone('Asia/Shanghai'))
    scheduler.start()
