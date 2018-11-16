# -*- coding: utf-8 -*-
import scrapy
from dongmanzixun.items import DongmanzixunItem

class DongziSpider(scrapy.Spider):
    name = 'dongzi'
    allowed_domains = ['news.comicst.com']
    start_urls = ['http://news.comicst.com/']

    page = 1
    url = 'http://news.comicst.com/index.php?page={}'


    def parse(self, response):
        #创建一个item对象
        item = DongmanzixunItem()
        #首先找到所有的资讯li   /div[3]/div[1]/text():所有标题
        li_list = response.xpath('//dl[@class="bbdayy cl"]')
        #遍历
        for li in li_list:
            #找到简介
            dong_jian =  response.xpath('//dd[@class="xs2 cl"]/a/text()').extract_first()
            #资讯主页到详情页的链接
            u =  li.xpath('./dt/a/@href').extract_first()
            yield scrapy.Request(url=u,callback=self.parse_detail,meta={'item':item})

        if self.page < 5:
            self.page += 1
            hou_url = self.url.format(self.page)
            yield scrapy.Request(url=hou_url,callback=self.parse)

    def parse_detail(self,response):
        #传递过来的item
        item = response.meta['item']
        #资讯类别
        item['dong_type'] = '1'
        # 资讯主页图片
        # item['dong_first_url'] = response.xpath('./div[2]/a/img/@src').extract_first()
        #资讯标题
        item['title'] = response.xpath('//div[@class="h hm"]/h1[1]/text()').extract_first()
        #资讯时间
        item['dong_tiem'] = response.xpath('//div[@class="h hm"]/p/text()').extract_first()
        #资讯作者
        item['dong_author'] = response.xpath('//div[@class="h hm"]/p/a/text()').extract_first()
        #资讯内容
        item['dong_content'] = response.xpath('//td[@id="article_content"]//text()').extract()
        #资讯页图片url
        item['dong_url'] = response.xpath('//td[@id="article_content"]/p[2]/font/img/@src').extract_first()
        yield item

