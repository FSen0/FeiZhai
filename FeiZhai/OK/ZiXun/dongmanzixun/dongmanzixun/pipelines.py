# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.utils.project import get_project_settings

class DongmanzixunPipeline(object):
    def open_spider(self,spider):
        #打开文件
        self.fp = open('dongzi.txt','w',encoding='utf8')

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
        settings = get_project_settings()
        #连接数据库
        self.conn = pymysql.Connect(host=settings['HOST'],port=settings['PORT'],
                                    user=settings['USER'],password=settings['PWD'],db=settings['DB'],
                                    charset=settings['CHARSET'])
        #获取游标
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        #sql语句
        sql = 'insert into dongzi(dong_type,title,dong_time,dong_author,dong_content,dong_url) values("%s","%s","%s","%s","%s","%s")' % (item['dong_type'],item['title'],item['dong_tiem'],item['dong_author'],item['dong_content'],item['dong_url'])
        dec = 'delete from dongzi where dong_url="none"'
        ded = 'delete from dongzi where dong_content="none"'
        #执行sql语句
        try:
            self.cursor.execute(sql)
            self.cursor.execute(dec)
            self.cursor.execute(ded)
            self.conn.commit()
        except:
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
