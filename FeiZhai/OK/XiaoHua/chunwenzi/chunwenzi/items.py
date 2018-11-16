# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChunwenziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #数据类别
    joketype = scrapy.Field()
    # 内容
    jokecontent = scrapy.Field()
    # 作者
    jokeauthor = scrapy.Field()
