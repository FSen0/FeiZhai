# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义你的数据结构
    #数据类别
    joketype = scrapy.Field()
    # 内容
    jokecontent = scrapy.Field()
    # 作者
    jokeauthor = scrapy.Field()
    #内容图片的url
    jokeimg = scrapy.Field()

