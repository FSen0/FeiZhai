# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class DongmanPipeline(object):
    def open_spider(self,spider):
        #打开文件
        self.fp = open('dongman.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        #将字典搞成json
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self,spider):
        #关闭文件
        self.fp.close()

from scrapy.utils.project import get_project_settings
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
        sql = 'insert into fz_imgmain(imgtype,imgname,mainimg) values("%s","%s","%s")' % (item['imgtype'],item['imgname'],item['mainimg'])
        #执行sql语句
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
