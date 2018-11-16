# -*- coding: utf-8 -*-
import scrapy
from dongman.items import DongmanItem

class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['www.mmonly.cc']
    start_urls = ['http://www.mmonly.cc/ktmh/qbrw/']

    page = 1
    url = 'http://www.mmonly.cc/ktmh/list_28_{}.html'

    def parse(self, response):
        #创建item对象
        item = DongmanItem()
        #找出所有含有div图片的div
        #//div[@class="item masonry_brick masonry-brick"]/div[2]/div[1]/span/a/text()
        div_list = response.xpath('//div[@class="item masonry_brick masonry-brick"]')
        for div in div_list:
            # 图片详情页地址
            # u = div.xpath('./div[1]/div/div[1]/a/@href').extract_first()
            #图片类别
            item['imgtype'] = 1
            #找出所有图片的名称
            item['imgname'] = div.xpath('./div[1]/div/div[1]/a/img/@alt')[0].extract().strip('\n\t\r')
            print('-' * 50)
            print(item['imgname'])
            print('-' * 50)
            #所有图片的url
            item['mainimg'] = div.xpath('./div[1]/div/div[1]/a/img/@src')[0].extract().strip('\n\t\r')
            yield item


        # if self.page <5:
        #     self.page += 1
        #     url = self.url.format(self.page)
        #     yield scrapy.Request(url=url,callback=self.parse)

