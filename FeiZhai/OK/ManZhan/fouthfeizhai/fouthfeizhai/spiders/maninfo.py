# -*- coding: utf-8 -*-
import scrapy
from fouthfeizhai.items import FouthfeizhaiItem


class ManinfoSpider(scrapy.Spider):
    name = 'maninfo'
    allowed_domains = ['http://www.manzhan8.com']
    start_urls = ['http://www.manzhan8.com/']

    # page = 1
    # url = 'http://www.manzhan8.com/'
    def parse(self, response):
        #首先得到所有的ul
        ul_list = response.xpath('//ul[@class="a"]')
        #遍历所有的ul,得到所有的漫展信息
        for man in ul_list:
            item = FouthfeizhaiItem()
            # 漫展时间
            item['man_time'] = man.xpath('./li[1]/a/text()')[0].extract().strip('\n\t\r')
            # 漫展地点
            try:
                item['man_addr'] = man.xpath('./li[2]/a/text()')[0].extract().strip('\n\t\r')
            except:
                item['man_addr'] = '敬请等待'
            print('-' * 50)
            print(item['man_addr'])
            print('-' * 50)
            # 漫展详情页链接
            # item['man_info_a'] = man.xpath('./li[3]/a/@href').extract()[0]
            # 漫展名称
            item['man_name'] = man.xpath('./li[3]/a/text()')[0].extract().strip('\n\t\r')
            # 漫展售价
            item['man_price'] = man.xpath('./li[4]/a/text()')[0].extract().strip('\n\t\r')
            yield item
