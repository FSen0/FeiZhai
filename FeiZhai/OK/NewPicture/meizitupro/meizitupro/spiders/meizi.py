# -*- coding: utf-8 -*-
import scrapy
from meizitupro.items import MeizituproItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/meinv/']

    # page = 1
    # url = 'http://www.meizitu.com/a/more_{}.html'

    def parse(self, response):
        item = MeizituproItem()
        #先找到所有含有图片的div
        div_list = response.xpath('//div[@class="items"]')
        #遍历
        for div in div_list:
            #图片类别
            item['imgtype'] = 3
            #图片名称
            item['imgname'] = div.xpath('./p/a/text()').extract_first()
            #图片url
            href = div.xpath('./a/img/@src').extract_first()
            if href[:5] != 'http:':
                item['mainimg'] = 'http://www.xiaohuar.com/' + href

            yield item
            # yield scrapy.Request(url=href,callback=self.parse_detail,meta={'item':item})

    # def parse_detail(self,response):
    #     #获取传递过来的item
    #     item = response.meta['item']
    #     #获取图片名称
    #     item['dong_name'] = response.xpath('//td[@id="showpagephoto"]/img/@alt').extract_first()
    #     ret = response.xpath('//td[@id="showpagephoto"]/img/@src').extract_first()
    #     item['dong_url'] = 'http://www.xiaohuar.com' + ret
    #     yield item
