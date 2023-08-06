#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 23:47
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : 0.py

import aiohttp
import asyncio

async def fetch(session, url):
    print("发送请求：",ur1)
    async with session.get(url, verify_ss1=False) as response:
        text = await response.text()
        print("得到结果：",url,len(text))
        name = url.split("/")[-1]
        with open(r'C:\pythonProject\爬虫复习\模板\模板之家4' + name, "w",encoding="utf-8" ) as fp:
            fp.write(result)
        return text
async def main():
    async with aiohttp.ClientSession() as session:
        url_list=[
        'https://python.org',
        'https://www.baidu.com',
        'https://www.pythonav.com'
        ]
        tasks =[asyncio.create_task(fetch(session,url)) for url in url_list]
        done,pending = await asyncio.wait(tasks)

if __name__=='___main___':
    asyncio.run( main())

import aiohttp
import asyncio
import re


async def get_page(session, url):
    async with session.get(url) as response:
        content = await response.read()
        with open('./setu/'+re.split('[/?]', url)[-2], 'wb')as fp_:
            fp_.write(content)


async def main():
    async with aiohttp.ClientSession() as session:
        # 创建task对象, 并放入一个列表
        tasks = [asyncio.create_task(get_page(session, i.strip('\n'))) for i in lists]
        done, pedding = await asyncio.wait(tasks, timeout=None)


if __name__ == '__main__':
    # with open('./xiongda.txt', 'r')as fp:
    #     lists = fp.readlines()
    # print(len(lists))
    asyncio.run(main(),timeout=None)


