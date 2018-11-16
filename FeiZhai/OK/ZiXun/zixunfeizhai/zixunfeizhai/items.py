# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZixunfeizhaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #详情页链接
    # zi_a = scrapy.Field()
    #资讯类别
    zi_type = scrapy.Field()
    #资讯名称
    zi_name = scrapy.Field()
    #资讯时间
    zi_time = scrapy.Field()
    #资讯内容
    zi_content = scrapy.Field()
    #资讯简介
    zi_brief = scrapy.Field()
    #资讯图片的url
    zi_tu_url = scrapy.Field()

