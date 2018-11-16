# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FouthfeizhaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    man_time = scrapy.Field()
    man_addr = scrapy.Field()
    # man_info_a = scrapy.Field()
    man_name = scrapy.Field()
    man_price = scrapy.Field()
