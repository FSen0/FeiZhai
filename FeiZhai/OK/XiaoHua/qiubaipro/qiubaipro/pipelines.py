# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql

class QiubaiproPipeline(object):
    # 构造方法
    def __init__(self):
        pass

    # 开启爬虫的函数
    def open_spider(self, spider):
        # 打开文件
        self.fp = open('qiubai.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        '''
        方法名：处理item函数
        item：要处理的数据单元，每一个item过来这个函数都要被调用
        spider：当前的爬虫对象
        方法有返回值  return item
        将item保存到文件中
        '''
        # 将item转化为字典
        d = dict(item)
        # 将字典搞成json
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')

        return item

    def close_spider(self, spider):
        # 关闭文件
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
        sql = 'insert into qiubai(joketype,jokecontent,jokeauthor,jokeimg) values("%s","%s","%s","%s")' % (item['joketype'],item['jokecontent'],item['jokeauthor'],item['jokeimg'])
        dtl = 'delete from qiubai where jokeimg="none"'
        #执行sql语句
        try:
            self.cursor.execute(sql)
            self.cursor.execute(dtl)
            self.conn.commit()

        except:
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
