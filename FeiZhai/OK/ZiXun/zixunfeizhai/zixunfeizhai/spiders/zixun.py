# -*- coding: utf-8 -*-
import scrapy
from zixunfeizhai.items import ZixunfeizhaiItem

class ZixunSpider(scrapy.Spider):
    name = 'zixun'
    allowed_domains = ['www.manzhan8.com']
    start_urls = ['http://www.manzhan8.com/zixun/']

    #首页：http://www.manzhan8.com/zixun/
    #http://www.manzhan8.com/zixun/index_2.html  从第二页开始有index_{}.html
    page = 1
    url = 'http://www.manzhan8.com/zixun/'
    hou_url = 'http://www.manzhan8.com/zixun/index_{}.html'


    def parse(self, response):
        #解析，首先找到包含资讯的所有div
        href_list = response.xpath('//div[@class="dmft radius5"]/div[1]/a/@href').extract()
        print('-' * 50)
        print(href_list[0])
        print('-' * 50)
        #遍历，依次想每个href发送请求
        for href in href_list:
            print('-' * 50)
            print(href)
            print('-' * 50)
            yield scrapy.Request(url=href, callback=self.parse_detail)
        #接着爬取指定页码的内容
        if self.page < 5:
            self.page += 1
            hou_url = self.hou_url.format(self.page)
            yield scrapy.Request(url=hou_url,callback=self.parse)

    def parse_detail(self,response):
        #创建一个item对象
        item = ZixunfeizhaiItem()
        #提取资讯名称
        item['zi_name'] = response.xpath('//div[@class="title"]/p/text()').extract_first()
        item['zi_time'] = response.xpath('//abbr[@class="timeago"]/@title').extract_first()
        print('--' * 50)
        print(item['zi_name'])
        print('--' * 50)
        # 资讯内容
        item['zi_content'] = response.xpath('//div[@class="con_1"]/p/span/text()').extract()
        # 资讯简介
        item['zi_brief'] = response.xpath('//div[@class="con_1"]/p[1]/span//text()')[0:2].extract()
        # 资讯图片链接
        item['zi_tu_url'] = response.xpath('//div[@class="con_1"]/p/img/@src').extract_first()
        if item['zi_tu_url'][:5] != "http:":
            item['zi_tu_url'] = 'http://www.manzhan8.com'+ item['zi_tu_url']
        yield item


