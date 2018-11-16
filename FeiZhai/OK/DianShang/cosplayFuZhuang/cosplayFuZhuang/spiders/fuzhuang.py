# -*- coding: utf-8 -*-
import scrapy
from cosplayFuZhuang.items import CosplayfuzhuangItem

class FuzhuangSpider(scrapy.Spider):
    name = 'fuzhuang'
    allowed_domains = ['www.rigouwang.com']
    start_urls = ['http://www.rigouwang.com/Yahoo/Auction/query/11975.html/']

    def parse(self, response):
        #找到所有详情页的连接
        div_list = response.xpath('//div[@id="item"]/div')
        #遍历
        for div in div_list:
            #详情页链接
            ret = div.xpath('./div/a/@href').extract_first()
            ret_url = 'http://www.rigouwang.com' + ret
            yield scrapy.Request(url=ret_url,callback=self.parse_detail)

    def parse_detail(self,response):
        #创建item
        item = CosplayfuzhuangItem()
        #查找服装名字
        item['goodsname'] = response.xpath('//div[@class="tb-property"]/div/text()').extract_first()
        #查找服装价格
        item['goodsprice'] = response.xpath('//div[@class="tb-property"]/ul/li[1]/label/text()').extract_first()
        #查找服装详情
        temp = ""
        for x in response.xpath('//ul[@id="tikgoodsmeg"]//text()').extract():
            zz = x.strip("\n\r\t")
            aa = zz.replace("\r\n"," ")
            temp += aa
        item['goodscon'] = temp
        #查找服装图片
        item['goodsimg'] = response.xpath('//div[@id="showbox"]/div[1]/img/@src').extract_first()
        #图片类型id
        item['goodst_id'] = 2
        yield item

