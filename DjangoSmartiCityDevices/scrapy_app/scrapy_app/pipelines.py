# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.htm
import json
import sys

import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath('../../')))


from webscrapy.models import ScrapyItem, ScrapyTasks


class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

        scrapy_task = ScrapyTasks.objects.get(self.task_id)
        scrapy_task.status = 'RUNING'
        scrapy_task.save()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),  # this will be passed from django view
        )


    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.

        scrapy_task = ScrapyTasks.objects.get(self.task_id)
        scrapy_task.status = 'FINISH'
        scrapy_task.finish_datetime = datetime.now()
        scrapy_task.save()

        item = ScrapyItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        self.items.append(item['url'])
        return item
