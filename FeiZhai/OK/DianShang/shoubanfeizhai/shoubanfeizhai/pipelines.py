# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import json

class ShoubanfeizhaiPipeline(object):
    def open_spider(self,spider):
        #打开文件
        self.fp = open('shouban_1.json','w',encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self,spider):
        self.fp.close()


from scrapy.utils.project import get_project_settings
class MysqlPipeline(object):
    def open_spider(self,spider):
        #获取配置参数
        settings = get_project_settings()
        #连接数据库
        self.conn = pymysql.Connect(host=settings['HOST'],port=settings['PORT'],
                                    user=settings['USER'],password=settings['PWD'],db=settings['DB'],
                                    charset=settings['CHARSET'])
        #获取游标
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        sql = 'insert into fz_goodsdet(goodsname,goodsprice,goodscon,goodsimg,goodst_id) values("%s","%s","%s","%s","%d")' % (item['goodsname'],item['goodsprice'],item['goodscon'],item['goodsimg'],item['goodst_id'])
        # dlc = 'delete from fz_goodsdet where goodscon="[' ', ' ']"'
        try:
            self.cursor.execute(sql)
            # self.cursor.execute(dlc)
            self.conn.commit()
        except:
            self.conn.rollback()
            print('-' * 50)
            print('失败')
            print('-' * 50)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
