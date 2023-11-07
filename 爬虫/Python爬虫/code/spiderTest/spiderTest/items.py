# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidertestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 爬虫获取到的数据需要组装成Item对象
class MovieItem(scrapy.Item):
    title = scrapy.Field()
    detail_page_url = scrapy.Field()
    star = scrapy.Field()
    pic_url = scrapy.Field()
