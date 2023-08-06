#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/1 13:41
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : InDao_01.py
import os
# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):

                print(i,j,k,end="   ")






import urllib.request

import urllib.parse

import json

import tkinter

import tkinter

root = tkinter.Tk()

root.title("简单翻译  v2.0")

root.geometry('325x300')

width = 325

height = 325

screenwidth =root.winfo_screenwidth()

screenheight = root.winfo_screenheight()

alignstr = '%dx%d+%d+%d' % (width,height, (screenwidth-width)/2,

(screenheight-height)/2)

root.geometry(alignstr)

def hit_me():

content = t1.get("0.0","end")

temp_content = content.replace(".", '.', content.count('.'))    #把句号换成点

# 从Request URL:拷贝过来。把_o删了

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# data就是表单数据，把Form Data 中的内容拷贝过来

data = {}

data['i'] = temp_content

data['from'] = 'AUTO'

data['to'] = 'AUTO'

data['smartresult'] = 'dict'

data['client'] = 'fanyideskweb'

data['salt'] = '15803439446390'

data['sign'] = '8e349204c5d1140741ffe43284595085'

data['ts'] = '1580343944639'

data['bv'] = 'bbb3ed55971873051bc2ff740579bb49'

data['doctype'] = 'json'

data['version'] = '2.1'

data['keyfrom'] = 'fanyi.web'

data['action'] = 'FY_BY_CLICKBUTTION'

# 使用urllib.parse.urlencode()函数将字符串转换为所需要的形式

# 把Unicode的文件格式转换为uf-8的编码形式

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)

# 解码的时候也要用uf-8来解码

html = response.read().decode("utf-8")

target = json.loads(html)

t2.delete("0.0","end")

t2_text=(target["translateResult"][0][0]["tgt"])

t2.insert(1.0,t2_text)

# 第5步，在窗口界面设置放置Button按键

# 在图形界面上设定输入框控件entry并放置控件

t1 = tkinter.Text(root, show=None, font=('Arial', 14))

t2 = tkinter.Text(root, show=None, font=('Arial', 14))

l1=tkinter.Label(root, text='       调用有道词典在线翻译.     by:张嘉',

font=('Arial', 12),     #font字体

width=20, height=2)

# t1.Text(root, height=3,wrap=WORD)

b1 = tkinter.Button(root, text='翻译一下', font=('Arial', 12),

width=10, height=1, command=hit_me)

t1.place(x=10,y=10,width=300, height=100)

b1.place(x=10,y=120)

t2.place(x=10,y=165,width=300, height=100)

l1.place(x=10,y=290,width=300, height=20)

root.mainloop()
'''
# import requests
#
# url = "https://doc.xuehai.net/bb919b97ce1a5ee88f30eada567cf950bcb4177d9-page.html"
# headers = {
#         "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
#
# }
#
# text = requests.get(url=url, headers=headers).text
# print(text)

#
# dic = [ {"k":5},{"l":8} ]
# for d in dic:
# dic = [ [1,2],[2,3],[3,4],[4,5],[5,6] ]
# for i in dic:
#      j = i[0]
#
# def mkdir(path):
  # os.path.exists(name)判断是否存在路径
  # os.path.join(path, name)连接目录与文件名
# import requests
# from lxml import etree
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
# }
# url = 'https://downsc.chinaz.net/Files/DownLoad/jianli/202201/jianli16821.rar'
# a = requests.get(url=url, headers=header).content
# with open("wwwsssssssssss" +'.rar', "wb") as fp:
#         fp.write(a)

# l = []
# k = { "1":a , "2":b }
# l.append(k)
# print(l)

# 示例1：
#
# 定义几个字典

alien_0 = {"color": "green", "points": 5}

alien_1 = {"color": "yellow", "points": 10}

alien_2 = {"color": "red", "points": 15}

# 把字典存入到列表aliens中

aliens = [alien_0, alien_1, alien_2]

# 遍历这个列表
print(aliens)

for alien in aliens:
     print(alien)

# 示例2：

# 创建一个用于存储外星人的空列表

aliens = []

# 创建30个绿色的外星人

for alien_number in range(30):
    new_alien = {"color": "green", 'points': 5, 'speed': 'slow'}

    aliens.append(new_alien)

# # 显示前5个外星人

for alien in aliens[:5]:
    print(alien)

print("...")

# 显示一共创建了多少个外星人

print("外星人的数量是： %d" % len(aliens))

# 示例3：

# 创建一个用于存储外星人的空列表

aliens = []

# 创建30个绿色的外星人

for alien_number in range(30):
    new_alien = {"color": "green", 'points': 5, 'speed': 'slow'}

    aliens.append(new_alien)
print(aliens)
for alien in aliens[0:3]:

    if alien['color'] == 'green':

        alien['color'] = 'yellow'

        alien['speed'] = 'medium'

        alien['points'] = 10

    elif alien['color'] == 'yellow':

        alien['color'] = 'red'

        alien['speed'] = 'fast'

        alien['points'] = 15

# 显示前5个外星人

for alien in aliens[:5]:
    print(alien)

print("...")



#

import aiohttp
import requests
from lxml import etree
import asyncio


async def fetch(session,download_url):
    print("请求发送:",download_url)
    async with session.get(download_url, verify_ssl=False) as response:
        result = await response.text()
        print("得到结果：", download_url)
        name = download_url.split("/")[-1]
        with open(r'C:\pythonProject\爬虫复习\模板\模板之家5' + name, "w",encoding="utf-8" ) as fp:
            fp.write(result)

async def main():
    async with aiohttp.ClientSession() as session:
        result_url_list =["http://www.cip.cc/",
                           "https://www.baidu.com",
                           "https://www.pythonav.com"
                         ]
        tasks = [ asyncio.create_task(fetch(session,download_url))for download_url in result_url_list]
        done, pending = await asyncio.wait(tasks)


from functools import wraps

from asyncio.proactor_events import _ProactorBasePipeTransport

def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

if __name__ == "__main__":
    asyncio.run(main())
