# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DongmanzixunItem(scrapy.Item):
    # name = scrapy.Field()
    #资讯类别
    dong_type = scrapy.Field()
    #资讯主页简介
    # dong_jian = scrapy.Field()
    #资讯主页图片url
    # dong_first_url = scrapy.Field()
    #资讯标题
    title = scrapy.Field()
    #资讯时间
    dong_tiem = scrapy.Field()
    #资讯作者
    dong_author = scrapy.Field()
    #资讯内容
    dong_content = scrapy.Field()
    #资讯详情页图片
    dong_url = scrapy.Field()
