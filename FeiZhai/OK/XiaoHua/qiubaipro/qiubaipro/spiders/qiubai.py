# -*- coding: utf-8 -*-
import scrapy
from qiubaipro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']

    #热图url
    start_urls = ['https://www.qiushibaike.com/imgrank/']

    #纯文字url
    #start_urls = ['https://www.qiushibaike.com/text/']

    # 在这里定义页码和url
    page = 1
    #https://www.qiushibaike.com/imgrank/page/2/
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'

    def parse(self, response):
        # 解析，首先找到所有的段子div
        div_list = response.xpath('//div[starts-with(@id,"qiushi_tag")]')
        # 遍历，依次提取每一个段子信息
        for div in div_list:
            # 创建item对象
            item = QiubaiproItem()
            item['joketype'] = '1'
            # 内容
            item['jokecontent'] = div.xpath('.//div[@class="content"]/span')[0].xpath('string(.)').extract_first()
            # 获取作者
            item['jokeauthor'] = div.css('.author h2::text').extract_first()
            #获取内容图片链接
            item['jokeimg'] = div.xpath('./div[2]/a/img/@src').extract_first()
            item['jokeimg'] = 'https:' + item['jokeimg']
            print('-' * 50)
            print(item['jokeimg'])
            print('-' * 50)

            yield item

        # 接着发送请求，爬取指定页码的内容
        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)
