# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .globalValue import QUESTION

class SpiderPipeline:
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://two:yuanfang@47.107.97.170:27017")
        mydb = myclient["zhihu"]
        self.mycol = mydb["content"]
    def process_item(self, item, spider):
        answerId = item["answerId"]
        updateTime = item["updateTime"]
        print(answerId)
        content = self.mycol.find_one({"answerId":answerId},{"_id":0});
        if content:
            if updateTime == content["updateTime"]:
                QUESTION.append(str(item["questionId"]))
                return item
            else:
                self.mycol.update({"answerId":answerId},{"$set":{'updateTime':updateTime,'content':item["content"]}})
                return item
        else:
            self.mycol.insert(dict(item))
            return item
