import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
