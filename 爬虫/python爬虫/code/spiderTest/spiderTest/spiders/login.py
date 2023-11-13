# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2023/11/13 10:46
# # @Author  : IngDao
# # @Email   : 1665834268@qq.com
# # @File    : login.py
# import json
#
# import scrapy
#
#
# class LoginSpider(scrapy.Spider):
#     # 类变量(静态)
#     name = 'login'
#     url = 'https://accounts.douban.com/j/mobile/login/basic'
#     data = {
#         'name': 'your name',
#         'password': 'your password',
#         'remember': "true"
#     }
#
#     # 携带cookies请求和post请求
#     def start_requests(self):
#         # 第一次登录，由于缺少cookie，会返回登录错误，并设置cookie
#         yield scrapy.FormRequest(
#             url=self.url,
#             formdata=self.data,
#             method='POST',
#             callback=self.getCookie  # 调用
#         )
#
#     def getCookie(self, response):
#         # scrapy会自动携带上一个请求设置的cookie
#         yield scrapy.FormRequest(
#             url=self.url,
#             formdata=self.data,
#             method='POST',
#             callback=self.parse,  # 调用
#             # 添加以防止出现：Filtered duplicate request
#             dont_filter=True
#         )
#
#     def parse(self, response):
#         res = json.loads(response.body.decode())
#         print("========")
#         print(res)
#         print("========")
#         url = "https://www.douban.com/"
#         yield scrapy.Request(url, callback=self.getHomePage)
#
#     def getHomePage(self, response):
#         navs = response.xpath("//div[@class='nav-items']//li")
#         for nav in navs:
#             title = nav.xpath(".//a/text()").extract_first().strip()
#             url = nav.xpath(".//a/@href").extract_first()
#             print(title.strip())
#             print(url)
#             if '我的豆瓣' in title:
#                 yield scrapy.Request(url, callback=self.getMyPage)
#
#     def getMyPage(self, response):
#         name = response.xpath("//div[@class='info']//h1/text()").extract_first().strip()
#         print("====start: getMyPage====")
#         print(name)
#         print("====end: getMyPage====")
