import os
import logging
from datetime import datetime

from .models import Schedule, Job, HandledJob

logger = logging.getLogger('django')


def run(websites):
    latest_schedule = Schedule.objects.latest('id')
    if latest_schedule.id != 1 and latest_schedule.finish_time is None:
        return
    latest_schedule.finish_time = None
    latest_schedule.save()

    # 爬取、预处理
    for website in websites:
        command = 'python WebSpider/WebSpider/spider_run/crawl_' + website + '.py'
        os.system(command)
    # 算法

    # 写回 Schedule 表
    latest_schedule = Schedule.objects.latest('id')
    latest_schedule.finish_time = datetime.now()
    latest_schedule.finish_count += 1
    latest_schedule.save()
