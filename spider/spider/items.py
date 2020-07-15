# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ContentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #问题ID
    questionId = scrapy.Field()
    #城市
    city = scrapy.Field()
    #回答ID
    answerId = scrapy.Field()
    #作者
    author = scrapy.Field()
    #头像URL
    headUrl = scrapy.Field()
    #知乎ID
    authorId = scrapy.Field()
    #性别
    gender = scrapy.Field()
    #赞同数
    voteupCount = scrapy.Field()
    #评论数
    commentCount = scrapy.Field()
    #创建时间
    createTime = scrapy.Field()
    #更新时间
    updateTime = scrapy.Field()
    #内容
    content = scrapy.Field()
    #是否有图片
    isPicture = scrapy.Field()

