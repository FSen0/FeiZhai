# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoubanfeizhaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #手办名称
    goodsname = scrapy.Field()
    #手办价格
    goodsprice = scrapy.Field()
    #手办详情内容链接
    goodscon = scrapy.Field()
    #手办图片url
    goodsimg = scrapy.Field()
    #手办类别
    goodst_id = scrapy.Field()

