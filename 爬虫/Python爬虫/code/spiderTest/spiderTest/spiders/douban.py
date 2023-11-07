import scrapy

from spiderTest.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    # def parse(self, response):  # 使用XPATH实现
    #     list_items = response.xpath('//*[@id="content"]/div/div[1]/ol/li')  # 总的
    #     for list_item in list_items:
    #         movie_item = MovieItem()  # 创建 movie_item对象
    #         movie_item['title'] = list_item.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()  # 使用键值
    #         movie_item['rank'] = list_item.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract()
    #         movie_item['subject'] = list_item.xpath('./div/div[2]/div[2]/p[1]/text()').extract_first()
    #         yield movie_item

    def parse(self, response):
        movie_item = MovieItem()
        items = response.xpath('//div[@class="item"]')
        for item in items:
            title = item.xpath('.//span[@class="title"]/text()').extract_first()
            detail_page_url = item.xpath('./div[@class="pic"]/a/@href').extract_first()
            star = item.xpath('.//span[@class="rating_num"]/text()').extract_first()
            pic_url = item.xpath('./div[@class="pic"]/a/img/@src').extract_first()
            # 使用数据结构
            movie_item['title'] = title
            movie_item['detail_page_url'] = detail_page_url
            movie_item['star'] = star
            movie_item['pic_url'] = pic_url
            yield movie_item

        next_page = response.xpath('//div[@class="paginator"]//span[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            # 将爬虫原始url与value拼接
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
