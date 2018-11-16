# -*- coding: utf-8 -*-
import scrapy
from shoubanfeizhai.items import ShoubanfeizhaiItem

class ShoubanSpider(scrapy.Spider):
    name = 'shouban'
    allowed_domains = ['www.ymi.cn']
    #类别1
    # start_urls = ['http://www.ymi.cn/auccate-2084023785.html']
    #类别2
    # start_urls = ['http://www.ymi.cn/auccate-2084305385.html']
    #类别3
    start_urls = ['http://www.ymi.cn/auccate-2084305368.html']

    page = 1
    first_url = 'http://www.ymi.cn/auccate-2084023785.html?&page={}'
    second_url = 'http://www.ymi.cn/auccate-2084305385.html?page={}'
    third_url = 'http://www.ymi.cn/auccate-2084305368.html?page={}'

    def parse(self, response):
        #找到所有详情页的链接
        a_list = response.xpath('//div[@class="list"]/div/a[1]/@href').extract()
        #遍历列表
        for a in a_list:
            print('-' * 50)
            print(a)
            print('-' * 50)
            ha = "http://www.ymi.cn" + a
            print(ha)
            print('-' * 50)
            yield scrapy.Request(url=ha,callback=self.parse_detail)

        if self.page <5:
            self.page += 1
            # url = self.first_url.format(self.page)
            # url = self.second_url.format(self.page)
            url = self.third_url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse_detail(self,response):
        #创建item对象
        item = ShoubanfeizhaiItem()
        #手办类型
        item['goodst_id'] = 1
        #提取名称
        item['goodsname'] = response.xpath('//dl[@class="title"]/dt/text()').extract_first()
        #商品编号
        # item['shou_num'] = response.xpath('//dl[@class="title"]/dd[1]/span/text()').extract_first()
        #提取价格
        item['goodsprice'] = response.xpath('//div[@class="detail_r_price"]/div[1]/b/text()').extract_first()[1:]

        #提取图片  第一张
        item['goodsimg'] = response.xpath('//ul[@class="tb-thumb"]/li[1]/div/a/img/@src').extract_first()
        #提取详情内容链接
        xiang_a = response.xpath('//div[@class="goods_detail"]/div[2]/div[1]/div[2]/iframe/@src').extract()[0]
        print('-' * 50)
        print(xiang_a)
        print('-' * 50)
        yield scrapy.Request(url=xiang_a,callback=self.parse_second,meta={'item':item})

    def parse_second(self,response):
        #获取传递过来的item
        item = response.meta['item']
        #提取详细信息
        haha = ""
        for x in  response.xpath('//body/center/text()').extract():
            haha += x.strip('\n\p\r')
        print('-' * 50)
        print(len(haha))
        print('-' * 50)
        if len(haha) < 3:
            del(haha)
        else:
            item['goodscon'] = haha
        # print('-' * 50)
        # print(item['shou_xiang'])
        # print('-' * 50)
        yield item




