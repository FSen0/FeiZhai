# -*- coding: utf-8 -*-
import scrapy
from cosplay.items import CosplayItem

class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['www.27270.com']
    start_urls = ['http://www.27270.com/game/cosplaymeitu/list_20_2.html']

    page = 2
    url = 'http://www.27270.com/game/cosplaymeitu/list_20_{}.html'

    def parse(self, response):
        #创建item对象
        item = CosplayItem()
        #找出所有含有li的ul
        li_list = response.xpath('//div[@class="pic_list_box w1200"]/ul/li')
        #遍历
        for li in li_list:
            #图片类别
            item['imgtype'] = 2
            #图片url
            src_l = li.xpath('./a/@href').extract()[0]
            yield scrapy.Request(url=src_l,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        #获取传递过来的item
        item = response.meta['item']
        #获取当页的图片
        item['mainimg'] = response.xpath('//p[@align="center"]/a[1]/img/@src').extract_first()
        #图片名称
        item['imgname'] = response.xpath('//div[@class="warp oh"]/h1[1]/text()').extract()[0]
        yield item


        if self.page < 4:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)

