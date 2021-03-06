from apscheduler.schedulers.blocking import BlockingScheduler
import os
import shutil

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=9, minute=25)
def scheduled_job():
    print('New job: packtpub-crawler')
    shutil.rmtree('./ebooks', ignore_errors=True)
    os.system('python script/spider.py --config config/prod.cfg --upload googledrive --type pdf --notify gmail --extras')

sched.start()
