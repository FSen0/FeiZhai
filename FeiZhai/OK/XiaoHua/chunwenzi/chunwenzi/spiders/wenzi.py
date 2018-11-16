# -*- coding: utf-8 -*-
import scrapy
from chunwenzi.items import ChunwenziItem

class WenziSpider(scrapy.Spider):
    name = 'wenzi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    page = 1
    url= 'https://www.qiushibaike.com/text/page/{}/'
    def parse(self, response):
        #首先找到所有段子的div
        div_list = response.xpath('//div[starts-with(@id,"qiushi_tag")]')
        #遍历，依次提取每一个段子信息
        for div in div_list:
            #创建item对象
            item = ChunwenziItem()
            #段子类别
            item['joketype'] = '2'
            #段子内容
            item['jokecontent'] = div.xpath('./a[1]/div/span/text()').extract()
            #段子作者
            item['jokeauthor'] = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            yield item

        # 接着发送请求，爬取指定页码的内容
        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)
