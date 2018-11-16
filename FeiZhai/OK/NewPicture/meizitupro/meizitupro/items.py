# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #类别
    imgtype = scrapy.Field()
    #名称
    imgname = scrapy.Field()
    #图片地址
    mainimg = scrapy.Field()
