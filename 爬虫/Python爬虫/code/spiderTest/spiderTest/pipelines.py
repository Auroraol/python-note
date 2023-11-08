# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

#
# class SpidertestPipeline:
#     def process_item(self, item, spider):
#         return item

# -*- coding: utf-8 -*-
import codecs
import csv

import pymysql
from scrapy import settings


class DoubanCsvPipeline:
    def __init__(self):
        with open("videos.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["电影名", "详情页", "豆瓣评分", "封面图片"])

    def process_item(self, item, spider):
        title = item['title']
        detail_page_url = item['detail_page_url']
        star = item['star']
        pic_url = item['pic_url']
        with open("videos.csv", "a", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([title, detail_page_url, star, pic_url])
        return item


class DoubanTxtPipeline:
    def __init__(self):
        with open("videos.txt", "w", newline='', encoding='utf-8') as f:
            f.write(f"电影名, 详情页, 豆瓣评分, 封面图片\r\n")

    def process_item(self, item, spider):
        title = item['title']
        detail_page_url = item['detail_page_url']
        star = item['star']
        pic_url = item['pic_url']

        txt = f"{title},{detail_page_url},{star},{pic_url}"
        with codecs.open("videos.txt", 'a', encoding='utf-8') as f:
            f.write(f"{txt}\r\n")
        return item


class DoubanMysqlPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host=settings.MySQL_HOST,
                                       port=settings.MYSQL_PORT,
                                       user=settings.MYSQL_USER,
                                       password=settings.MYSQL_PASSWORD,
                                       db=settings.MYSQL_DB_NAME,
                                       charset=settings.MYSQL_CHARSET,
                                       use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

        # 如果没有则创建表
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `douban_videos` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `title` varchar(255) DEFAULT NULL,
              `detail_page_url` varchar(255) DEFAULT NULL,
              `star` varchar(255) DEFAULT NULL,
              `pic_url` varchar(255) DEFAULT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """)

    def process_item(self, item, spider):
        # 检查是否已经存在数据
        value = self.cursor.execute(
            """
            select title from douban_videos where title=%s
            """, item['title']
        )

        if value == 0:
            self.cursor.execute(
                """
                insert into douban_videos(title, detail_page_url, star, pic_url ) value (%s, %s, %s, %s)
                """,
                (item['title'], item['detail_page_url'], item['star'], item['pic_url']))
            # 提交sql语句
            self.connect.commit()
        
        return item
