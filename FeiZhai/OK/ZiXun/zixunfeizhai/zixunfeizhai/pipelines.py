# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings
import json

class ZixunfeizhaiPipeline(object):
    def __init__(self):
        pass
    def open_spider(self,spider):
        self.fp = open('zixun.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string + '\n')

        return item
    def close_spider(self,spider):
        #关闭文件
        self.fp.close()


class MysqlPipeline(object):
    def open_spider(self,spider):
        #从配置文件中获取参数
        settings  = get_project_settings()
        #连接数据库
        self.conn = pymysql.Connect(host=settings['HOST'],port=settings['PORT'],
                                    user=settings['USER'],password=settings['PWD'],db=settings['DB'],
                                    charset=settings['CHARSET'])
        #获取游标
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        # sql = 'insert into testtable(title) values("%s")' % item['title']
        sql = 'insert into zixun(zi_type,zi_name,zi_time,zi_content,zi_brief,zi_tu_url) values(1,"%s","%s","%s","%s","%s")' % (item['zi_name'],item['zi_time'],item['zi_content'],item['zi_brief'],item['zi_tu_url'])
        dlc = 'delete from zixun where zi_content="[]"'
        dlb = 'delete from zixun where zi_brief="[]"'
        dlt = 'delete from zixun where zi_tu_url="none"'
        #执行sal语句
        try:
            self.cursor.execute(sql)
            self.cursor.execute(dlc)
            self.cursor.execute(dlb)
            self.cursor.execute(dlt)
            self.conn.commit()
        except:
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()