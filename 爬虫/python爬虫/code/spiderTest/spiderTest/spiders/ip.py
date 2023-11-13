import scrapy


class IpSpider(scrapy.Spider):
    name = "ip"
    allowed_domains = ["ip138.com"]
    start_urls = ['https://2023.ip138.com/']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Content-Length': '0',
        "Connection": "keep-alive"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        print("=" * 40)
        print(response.xpath('/html/body/p[1]/a/text()').extract_first())
        # print(response.xpath('/html/body/p[1]/text()').extract())
        print("=" * 40)
