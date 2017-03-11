# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class AppcrawlPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for field, data in item.items():
            if not data:
                raise DropItem("Missing %s of app data from %s\n" %(field, item['url']))
        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        log.msg("App added to MongoDB database!",
                level=log.DEBUG, spider=spider)
        return item

