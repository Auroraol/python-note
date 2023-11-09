# 爬虫概述

## 爬虫的概念

爬虫就是一个自动化的机器人软件，按照设定去获得你想要的互联网数据，并且整个抓取的过程都是自动完成
的。我们所熟知的百度和谷歌两大搜索引擎的实质也就是爬虫，它们会不间断的爬取互联网上存在的和新出现的
内容，并以某种形式存储到自己烈数据库中。

注意:  爬虫也只能获取客户端(浏览器)所展示出来的数据

## 爬虫的基本原理

1. 浏览网页：就如同我们人浏览网页一样，爬虫需要先向目标地址发起请求，然后等待目标页面内容全部加载；
2. 解析网页：一张网页由许许多多的内容构成，不只是文字，还有图片、音频、视频、HTML代码、CSS样式表、JS脚本等各种元素，为此，需要一定的规则来定位到我们所需要的具体某个\些元素；
3. 下载数据：在解析出我们需要的部分后，便可以将其下载并暂时存储到内存中；
4. 存储数据：下载出来的数据可能远不止一个，而内存的空间有限且宝贵，我们需要用到数据库或其他形式来将下载的数据分类且长期存储，以便于后面的数据清洗、查找等各种操作；
5. 清洗数据：下载的数据可能会包含一些无效的、有错的内容，为此需要对这些内容进行清洗，只保留对我们有价值的东西。之所以将清洗放在存储后，是因为这里主要是对已经下载的内容进行处理，需要大量的I\O操作，而爬虫主要过程由CPU来调度，我们都知道主存的读写速度远高于辅存的读写速度，这一步如果放在存储前面，会极大的限制爬虫的效率。

## 爬虫的作用

+ [x] 数据采集
  + 抓取微博评论(机器学习舆情监控)
  + 抓取招聘网站的招聘信息(数据分析、挖掘)
  + 新浪滚动新闻
  + 百度新闻网站

+ [x] 软件测试
  + 爬虫之自动化测试
  + 虫师
+ [x] 12306抢票
  + 模拟登录
  + 模拟抢票
+ [x] 网站上的投票
+ [x] 网络安全
  +  短信轰炸 
  + web漏洞扫描 

## 爬虫的分类

![爬虫的分类](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255156.png) 

1. 根据被爬取网站的数量不同，可以分为：
   + 通用爬虫，如 搜索引擎
   + 聚焦爬虫，如 12306抢票，或专门抓取某一个（某一类）网站数据

2. 根据是否以获取数据为目的，可以分为：
   + 功能性爬虫，给你喜欢的明星投票、点赞
   + 数据增量爬虫，比如招聘信息

3. 根据url地址和对应的页面内容是否改变，数据增量爬虫可以分为：
   + 基于url地址变化、内容也随之变化的数据增量爬虫 
   + url地址不变、内容变化的数据增量爬虫 

4. 爬虫的流程

   ![image-20231106145017990](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255158.png)

# 网络请求库

## Requests 网络请求库:crossed_swords:

### **导入模块**

```
pip install fake_useragent //在pycharm得搜索fake-useragent
pip install requestes
```

```python
import random
import requests
from fake_useragent import UserAgent
```

### Response对象

####  **设置编码方式**

```python 
response.encoding = "utf-8"
```

#### **返回字符串**

```python
text = response.text
```

#### **返回二进制**

```python 
content = response.content
```

#### **返回json数据**

```
data = response.json()
```

#### **返回状态码**

```
code = response.status_code
```

#### **返回响应头**

```
headers = response.headers
```

#### **返回请求头**

```
headers2 = response.request.headers
```

#### 遍历响应数据
优化内存，避免一次性读取大文件

```python
itc = response.iter_content(1024 * 10)
for c in itc:
	print(c)
```

### Requests对象

#### Get请求

GET请求一般用于向服务器获取数据

```python
url = 'http://www.baidu.com'
response = requests.get(url)
```

**携带参数Get请求**

```python
url = 'http://www.baidu.com/s'
params = {'wd': '阿', 'sex': '男'}
response = requests.get(url=url, params=params)
response.encoding = 'utf-8'
print(response.text)
```

#### post请求

发送POST请求时，需要特别注意headers的一些属性： 

+ Content-Length: 144： 是指发送的表单数据长度为144，也就是字符个数是144个。
+  Content-Type: application/x-www-form-urlencoded： 表示浏览器提交 Web 表单时使用，表单数据会按照 name1=value1&name2=value2 键值对形式进行编码。 
+ X-Requested-With: XMLHttpRequest：表示Ajax异步请求。 有些网页内容使用AJAX加载，这种数据无法直接对网页url进行获取。**AJAX一般返回的是JSON，只要对AJAX地址进行post或get，就能返回JSON数据了**

```python
url = 'https://fanyi.baidu.com/sug'
data = {'kw': 'spider'}
headers = {'User-Agent': UserAgent().random}
response = requests.post(url=url, headers=headers, data=data).json()
result=response.get('data')
print(result)
```

#### 可选参数

##### **设置请求头**

```python
url = 'http://www.baidu.com'
headers = {'User-Agent': UserAgent().random}  #使用fake_useragent的作用就是能够帮助我们生成user-agent，从而不需要自己去写。
response = requests.get(url=url, headers=headers)
headers = response.request.headers
print(headers)
```

##### **超时设置**

```python
url = 'http://www.python.org'
try:
	response = requests.get(url=url, timeout=0.1)
except requests.exceptions.ConnectTimeout:
	print('访问超时')
```

##### **禁止重定向**

```python
url = 'http://www.baidu.com'
response = requests.get(url, allow_redirects=False).text
print(response)
```

##### **设置代理**

###### 使用HTTP代理

```python
proxies_pool = [
{'http': '47.57.188.208:80', 'https': '47.57.188.208:80'},
{'http': '59.124.224.205:3128', 'https': '59.124.224.205:3128'}
]
proxies = random.choice(proxies_pool)
url = 'http://httpbin.org/get'
response = requests.get(url=url, headers=headers, proxies=proxies)
print(response.text)
```

###### **使用Socks代理**

+ Socks5代理比http代理速度要快得多
+ 安装socks模块 pip install requests[socks]

```python
proxies_pool = [
	{'http': 'socks5://127.0.0.1:9742', 'https': 'socks5://127.0.0.1:9742'},
]
proxies = random.choice(proxies_pool)
url = 'http://httpbin.org/get'
response = requests.get(url=url, headers=headers, proxies=proxies)
print(response.text)
```

#####  **认证设置**

碰到需要认证的网站

```python
response=requests.get('http://120.27.34.24:9001',auth=('user','pwd'))
print(response.status_code)
```

### cookie

#### cookie和session的区别

+ cookie数据存放在客户的浏览器上
+ session数据放在服务器上
+ cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗
+ session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能
+ 单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie

####  cookie的获取与设置

**1 携带cookie访问**

```python
import re
import requests
import ddddocr

session = requests.Session()
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {'User-Agent': UserAgent().random}
response = session.get(url, headers=headers).text

code_url = 'https://so.gushiwen.cn/RandCode.ashx'
code_img = session.get(code_url).content
ocr = ddddocr.DdddOcr()
code = ocr.classification(code_img)
print('验证码:', code)

data = {
'VIEWSTATE': re.search(r'VIEWSTATE" value="(.*)?" />', response).group(1),
'__VIEWSTATEGENERATOR': re.search(r'VIEWSTATEGENERATOR" value="(.*)" />', response).group(1),
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': '15992296350',
'pwd': 'whp123123',
'code': code,
'denglu': '登录',
}

response = session.post(url=url, headers=headers, data=data).text
if re.search('>退出登录', response):
	print('登录成功！')
	print('绑定手机号:', re.search('>绑定手机号(.*)?', response).group(1))
	print('绑定邮箱:', re.search('>绑定邮箱(.*)?', response).group(1))
	url = 'https://so.gushiwen.cn/user/collectbei.aspx?sort=t'
	response = session.get(url=url, headers=headers).text
	print(response)
```

**储存cookie**

```python
import requests.utils
import json

cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
with open('cookie.txt', mode='w', encoding='utf-8') as file:
	json.dump(cookie_dict, file)
```

 **使用cookie**

```python
with open('cookie.txt', mode='r', encoding='utf-8') as file:
	cookie_dict = json.load(file)
	session.cookies = requests.utils.cookiejar_from_dict(cookie_dict)
	
url = 'https://so.gushiwen.cn/user/collectbei.aspx?sort=t'
response = session.get(url=url, headers=headers).text
print(response)
```

### **使用Exceptions**

```python
from requests.exceptions 
import ReadTimeout, HTTPError, RequestException

try:
	url = 'www.python.org'
	response = requests.get(url, timeout=0.5)
except ReadTimeout as e:
	print(e)
except HTTPError as e:
	print(e)
except RequestException as e:
	print(e)
```

### ssl证书验证

1 SSL证书验证介绍

●https协议会有一个ssl证书的加密认证

●现在随处可见 https 开头的网站，requests可以为 HTTPS 请求验证SSL证书，就像web浏览器一样，如果网站的SSL证书是经过CA认证的，则能够正常访问

●如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/ 的时候，会警告用户证书不受信任。（据说 12306 网站证书是自己做的，没有通过CA认证）

2 关闭ssl证书验证

```
url = 'https://www.12306.cn'
response = requests.get(url, verify=False)
print(response.text)
```

消除证书的警报
●没有通过CA认证的网站在访问的时候则会报出SSLError，我们需要单独处理SSL证书，让程序忽略SSL证书验证错误，即可正常访问。

```
from requests.packages import urllib3

urllib3.disable_warnings()
url = 'https://www.12306.cn'
response = requests.get(url, verify=False)
print(response.text)
```

**使用ssl证书**

```
url='http://www.baidu.com'
response=requests.get(url,cert=('/path/server.crt','/path/key'))
print(response.tex)
```

关于CA
●CA（Certificate Authority）是数字证书认证中心的简称，是指发放、管理、废除数字证书的受信任的第三方机构，如[北京数字认证股份有限公司](http://www.bjca.org.cn/)、[上海市数字证书认证中心有限公司](http://www.sheca.com/)等...
●CA的作用是检查证书持有者身份的合法性，并签发证书，以防证书被伪造或篡改，以及对证书和密钥进行管理。
●现实生活中可以用身份证来证明身份， 那么在网络世界里，数字证书就是身份证。和现实生活不同的是，并不是每个上网的用户都有数字证书的，往往只有当一个人需要证明自己的身份的时候才需要用到数字证书。
●普通用户一般是不需要，因为网站并不关心是谁访问了网站，现在的网站只关心流量。但是反过来，网站就需要证明自己的身份了。
●比如说现在钓鱼网站很多的，比如你想访问的是 [www.baidu.com](http://www.baidu.com/)，但其实你访问的是 [www.daibu.com](http://www.daibu.com/)“，所以在提交自己的隐私信息之前需要验证一下网站的身份，要求网站出示数字证书。
●一般正常的网站都会主动出示自己的数字证书，来确保客户端和网站服务器之间的通信数据是加密安全的。

### 实例

#### **单词测试**

```python
import time

import requests
from pprint import pprint
from fake_useragent import UserAgent


def get_data(word):
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': str(UserAgent().random)
    }
    data = {
        'kw': word
    }
    while True:
        try:
            response = requests.post(url=url, headers=headers, data=data).json().get('cookie')[0]
            break
        except Exception as e:
            print(e)
    return response.get('k'), response.get('v')


def input_word(word, value):
    while True:
        input_value = input(value + '\n请输入单词(q跳过)：')
        if input_value == word:
            print('回答正确！')
            break
        elif input_value == 'q':
            print('回答错误！正确答案：%s' % word)
            word_dt[word] = value
            break


def get_word():
    with open('word.txt', 'r') as file:
        ls = file.readlines()
    for word in ls:
        result = get_data(word.strip())
        input_word(result[0], result[1])
    if word_dt:
        pprint(word_dt)
    else:
        print('恭喜你！满分通过！')


if __name__ == '__main__':
    word_dt = {}
    get_word()
```

#### **贝贝育儿登录**

```python
import requests
from fake_useragent import UserAgent

session = requests.Session()

url = 'https://www.beibei.com/yuer/wp-login.php'
headers = {
    'User-Agent': UserAgent().random,
    'referer': 'https://www.beibei.com/yuer/wp-login.php'
}
data = {
    'log': '账号',
    'pwd': '密码',
    'wp-submit': '登录',
    'redirect_to': 'https://www.beibei.com/yuer/wp-admin/',
    'testcookie': '1',
}
session.get(url=url, headers=headers)  # 获取cookie
response = session.post(url=url, headers=headers, data=data)
print(response.text)
print(response.status_code)
print(response.url)
```

#### 哔哩哔哩相簿

```python
import requests
from fake_useragent import UserAgent
import json
import os


def get_data():
    url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/index'
    params = {
        'type': 'recommend',
        'page_num': '0',
        'page_size': '45',
    }
    headers = {
        'User-Agent': UserAgent().random
    }
    response = requests.get(url=url, params=params, headers=headers).json()
    items = response.get('data').get('items')
    print('开始下载......')
    for item in items:
        title = item.get('item').get('title')
        title = title.replace('/', '、')
        path = f'相簿/{title}'
        if not os.path.exists(path):
            os.mkdir(path)
        pictures = item.get('item').get('pictures')
        for i, picture in enumerate(pictures):
            img_src = picture.get('img_src')
            while True:
                try:
                    imgFile = requests.get(img_src, timeout=5).content
                    break
                except Exception as e:
                    print(e)
            filename = f'{path}/{i + 1}.png'

            with open(filename, mode='wb') as file:
                file.write(imgFile)

            print(f'下载完成：{filename}')


if __name__ == '__main__':
    if not os.path.exists('相簿'):
        os.mkdir('相簿')

    get_data()
```

#### 下载m3u8视频

我们这次用Python下载优酷中的视频，以《名侦探柯南》为例，首分析下优酷视频的请求方式

打开链接:  https://v.youku.com/v_show/id_XMzk1NjM1MjAw.html?spm=a2hcb.12675304.m_7182_c_14738.d_4&s=cc003400962411de83b1&scm=20140719.rcmd.7182.show_cc003400962411de83b1

![img](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597108498651-e939ebec-8139-4c27-b97f-435d3ee753a2.png?x-oss-process=image%2Fresize%2Cw_937%2Climit_0)

可以看出，优酷中的视频是以“m3u8+ts”的形式展现的，我们用[you-get](https://github.com/soimort/you-get)尝试一下看能不能正常下载：

![img](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597108472448-8b0e27c0-6c6b-4554-babe-c2d634e6ede9.png?x-oss-process=image%2Fresize%2Cw_937%2Climit_0)

完美，可以正常下载并播放，说明优酷对公开视频没做加密处理（会员视频不知道有没有做加密处理，以后尝试），可以很容易地下载

以下是这个地址提取出的m3u8地址：

```
https://valipl.cp31.ott.cibntv.net/657344945574371BC95CD47EE/03000500005C87988D10F87011BA6A594ECA8A-95C1-4693-A925-8DA0F67B40B0.m3u8?ccode=0502&duration=1493&expire=18000&psid=f20c7e3b28c90f13fdc97bd835a4c2bc&ups_client_netip=7435f5f6&ups_ts=1589254536&ups_userid=&utid=G97wFuWSrCYCAXBwJ%2Bq2XrB6&vid=XMzk1NjM1MjAw&vkey=B10fdf26c2aed124113199eff1351e1d4&sm=1&operate_type=1&dre=u37&si=73&eo=0&dst=1&iv=0&s=cc003400962411de83b1&type=flvhdv3&bc=2
```

m3u8格式的内容如下：

```
#EXTM3U

\#EXT-X-VERSION:3

\#EXT-X-TARGETDURATION:10

\#EXT-X-MEDIA-SEQUENCE:0

\#EXTINF:10.000000,

\#EXT-X-PRIVINF:FILESIZE=233684

https://valipl.cp31.ott.cibntv.net/67756D6080932713CFC02204E/03000500005C87988D10F87011BA6A594ECA8A-95C1-4693-A925-8DA0F67B40B0-00001.ts?ccode=0502&duration=1493&expire=18000&psid=f20c7e3b28c90f13fdc97bd835a4c2bc&ups_client_netip=7435f5f6&ups_ts=1589254536&ups_userid=&utid=G97wFuWSrCYCAXBwJ%2Bq2XrB6&vid=XMzk1NjM1MjAw&sm=1&operate_type=1&dre=u37&si=73&eo=0&dst=1&iv=0&s=cc003400962411de83b1&type=flvhdv3&bc=2&vkey=B31b72434dad3d41e0ee875622526236a

\#EXTINF:10.000000,

\#EXT-X-PRIVINF:FILESIZE=332948

https://valipl.cp31.ott.cibntv.net/67756D6080932713CFC02204E/03000500005C87988D10F87011BA6A594ECA8A-95C1-4693-A925-8DA0F67B40B0-00002.ts?ccode=0502&duration=1493&expire=18000&psid=f20c7e3b28c90f13fdc97bd835a4c2bc&ups_client_netip=7435f5f6&ups_ts=1589254536&ups_userid=&utid=G97wFuWSrCYCAXBwJ%2Bq2XrB6&vid=XMzk1NjM1MjAw&sm=1&operate_type=1&dre=u37&si=73&eo=0&dst=1&iv=0&s=cc003400962411de83b1&type=flvhdv3&bc=2&vkey=Bf6e771a551f95093ab43a74104c9f429

...

\#EXTINF:3.000000,

\#EXT-X-PRIVINF:FILESIZE=37600

https://valipl.cp31.ott.cibntv.net/67756D6080932713CFC02204E/03000500005C87988D10F87011BA6A594ECA8A-95C1-4693-A925-8DA0F67B40B0-00150.ts?ccode=0502&duration=1493&expire=18000&psid=f20c7e3b28c90f13fdc97bd835a4c2bc&ups_client_netip=7435f5f6&ups_ts=1589254536&ups_userid=&utid=G97wFuWSrCYCAXBwJ%2Bq2XrB6&vid=XMzk1NjM1MjAw&sm=1&operate_type=1&dre=u37&si=73&eo=0&dst=1&iv=0&s=cc003400962411de83b1&type=flvhdv3&bc=2&vkey=B7326e6d22abf323fdabac4758774398c

\#EXT-X-ENDLIST
```

可以看出，就是一个播放列表，每一个视频分段是一个ts文件。

注：关于you-get的安装（我是在WSL中安装的），使用以下命令：

```
pip3 install you-get
```

you-get的详细使用文档参见：[you-get 中文说明](https://github.com/soimort/you-get/wiki/中文说明)

**使用Python直接调用you-get进行下载**

```python
# -*- coding: utf-8 -*-
from you_get import common

url = 'https://v.youku.com/v_show/id_XMzk1NjM1MjAw.html\?spm\=a2hcb.12675304.m_7182_c_14738.d_4\&s\=cc003400962411de83b1\&scm\=20140719.rcmd.7182.show_cc003400962411de83b1'
common.any_download(
    url=url,
    output_dir=r'C:\Users\quanzaiyu\Desktop\temp',
    merge=True
)
```

**使用Python自己实现**

```python
# -*- coding: utf-8 -*-
import os
import requests

def download(url):
    download_path = os.getcwd() + "\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
        for index, line in enumerate(file_line):
            if "https" in line:
                res = requests.get(line)
                with open(download_path + "\\云霄飞车杀人事件.mp4", 'ab') as f:
                    f.write(res.content)
                    f.flush()
        print("下载完成")


if __name__ == '__main__':
    url = "https://valipl.cp31.ott.cibntv.net/657344945574371BC95CD47EE/03000500005C87988D10F87011BA6A594ECA8A-95C1-4693-A925-8DA0F67B40B0.m3u8?ccode=0502&duration=1493&expire=18000&psid=f20c7e3b28c90f13fdc97bd835a4c2bc&ups_client_netip=7435f5f6&ups_ts=1589254536&ups_userid=&utid=G97wFuWSrCYCAXBwJ%2Bq2XrB6&vid=XMzk1NjM1MjAw&vkey=B10fdf26c2aed124113199eff1351e1d4&sm=1&operate_type=1&dre=u37&si=73&eo=0&dst=1&iv=0&s=cc003400962411de83b1&type=flvhdv3&bc=2"
    download(url)
```

### 1、爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）

可能出现的问题

- 乱码的问题：响应数据不是‘utf-8’格式（原因），用.encoding='utf-8'转换编码格式（解决方法）
- 数据丢失（比人工浏览到的数据少）：异常访问请求（没有伪请求头UA-headers）

```python
# encoding: utf-8
"""
@author: linpions
@software: PyCharm
@file: 案例1：爬取搜狗词条结果.py
@time: 2021-12-26 20:10
"""

import requests

url = 'https://www.sogou.com/web'
keywords = input('enter a key word:')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

# 实现参数动态化
# params参数（字典）：保存请求时URL携带的参数
params = {
    'query': keywords,
}

response = requests.get(url=url, params=params, headers=headers)
response.encoding = 'utf-8'
page_text = response.text

file_Name = '搜狗词条：' + keywords + '.html'
with open(file_Name, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(file_Name, '爬取完毕！')
```

### 2、破解百度翻译

- url: https://fanyi.baidu.com/v2transapi?from=en&to=zh
- 局部刷新，Ajax请求

```python
def baidu_fanyi(keyword=None):
    url = 'https://fanyi.baidu.com/v2transapi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '92.0.4515.131 Safari/537.36',
        'cookie': 'BIDUPSID=2437C970398B3648E3DCEFC3DA3F453F; PSTM=1588134641; BDUSS=2FNVTNXWFREN3lOS2VZWlh6eHJvcjdUWGN4d3RueWRKaGVCYWtJWHV6QnVDdjFmRVFBQUFBJCQAAAAAAAAAAAEAAADdjgBCwe7GvdfTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG591V9ufdVfN; BDUSS_BFESS=2FNVTNXWFREN3lOS2VZWlh6eHJvcjdUWGN4d3RueWRKaGVCYWtJWHV6QnVDdjFmRVFBQUFBJCQAAAAAAAAAAAEAAADdjgBCwe7GvdfTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG591V9ufdVfN; H_WISE_SIDS=110085_127969_128701_131423_144966_154214_156927_160878_164955_165135_165328_166148_167069_167112_167300_168029_168542_168626_168748_168763_168896_169308_169536_169882_170154_170240_170244_170330_170475_170548_170578_170581_170583_170588_170632_170754_170806_171446_171463_171567_171581; __yjs_duid=1_583e334168fb61ad031df70449fa28b11620848721011; BAIDUID=88DF09015FADA78B679498D7716BC9F3:FG=1; BAIDUID_BFESS=9AC90C484D04DC1AD589BE66E2DC00C5:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1629183095; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1629184241; __yjs_st=2_ZDRiNjhmMDM0ZWI2MTRmM2MyZDYyZDg3NTg5NGFhZmJkNmQzODZjZmUxNGQ5NmYxZmIyNTRiOTg1Y2Y5NjYzMDM0NzMzNWVjYTYyYjNjMjlkMThmZWRhYjZhZWYzNzliZjI1ZWM2YjExZmJlODUyMTI3YjFjNTU4Y2I5OGM1ZGFjNzNmNDA0N2Q2NjAzYzY4ZDZiYzUzZTcxYzE1ZjA5OTAwMmVkNWM2YjlmYTFjY2U3ZTQwOWU4NzVhZTlmMDEyYmU3NDVhYTVmOWEyYTVjOGUxNzUzNjI2Y2U3NTRkNmQyYTExMjUzNGJhYWVkMzgyOTMzZDFjOTVhOGVhODM3OV83XzI0MTkxNGNi; ab_sr=1.0.1_ZDg0NDMwZGY4ZWZiMTA5YjgzMmVlMDU0M2MxZDRkMzY4NDQ3MGI4YThlNjNhYTFiMGJhZTUzNzRkZTI5NjI5NzUwMGNkYjBmZTQ3MTBhN2FkMjgyMDg5OGNkMTkyOTg5M2UxYmNjYmE3NzUyZGM1ZGM4N2M5NzliNzBlYTg3ZTJlNjMwNTU3OTdjMmFkNTRjMDg3OTEyMDJiMjg2MmU5NGMzZjdiM2U3NjUyZTBjNjg1ODEyYTc5Yzk5MTI5NTAw',
    }
    data = {
        'from': 'en',
        'to': 'zh',
        'query': keyword,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '871501.634748',
        'token': '6567483e2686ce76cd8bbdb797a1a5bd',
        'domain': 'common',
    }
    response = requests.post(url=url, data=data, headers=headers)
    page_text = response.json()
    # page_text = page_text['data']
    return page_text
```

当改变要翻译的内容时，返回的不是想要的结果，出现**997/998错误**

原因：百度翻译增加了反爬机制，所以爬虫程序获取不到翻译结果了；参考分析方式进行学习；因为你被反爬了，headers(重点是useragent)和代理ip和动态验证码，这三个加上基本就没问题了

[**【Python】关于爬取百度翻译以及"errno":998&"errno":997_RedMaple-程序员宅基地**](https://www.cxyzjd.com/article/qq_25404477/103331566)

- **sign、cookie是动态的，**会变****

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255159.png" alt="image.png" style="zoom:50%;" />

**解决方案：**

- 修改url为手机版的地址：http://fanyi.baidu.com/basetrans 或者 https://fanyi.baidu.com/sug
  User-Agent也用手机版的

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255160.png)

```python
# 解决cookie和sign动态变化问题
def baidu_fanyi2(keyword=None):
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '92.0.4515.131 Safari/537.36',
        # 'cookie': 'BIDUPSID=2437C970398B3648E3DCEFC3DA3F453F; PSTM=1588134641; BDUSS=2FNVTNXWFREN3lOS2VZWlh6eHJvcjdUWGN4d3RueWRKaGVCYWtJWHV6QnVDdjFmRVFBQUFBJCQAAAAAAAAAAAEAAADdjgBCwe7GvdfTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG591V9ufdVfN; BDUSS_BFESS=2FNVTNXWFREN3lOS2VZWlh6eHJvcjdUWGN4d3RueWRKaGVCYWtJWHV6QnVDdjFmRVFBQUFBJCQAAAAAAAAAAAEAAADdjgBCwe7GvdfTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG591V9ufdVfN; H_WISE_SIDS=110085_127969_128701_131423_144966_154214_156927_160878_164955_165135_165328_166148_167069_167112_167300_168029_168542_168626_168748_168763_168896_169308_169536_169882_170154_170240_170244_170330_170475_170548_170578_170581_170583_170588_170632_170754_170806_171446_171463_171567_171581; __yjs_duid=1_583e334168fb61ad031df70449fa28b11620848721011; BAIDUID=88DF09015FADA78B679498D7716BC9F3:FG=1; BAIDUID_BFESS=9AC90C484D04DC1AD589BE66E2DC00C5:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1629183095; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1629184241; __yjs_st=2_ZDRiNjhmMDM0ZWI2MTRmM2MyZDYyZDg3NTg5NGFhZmJkNmQzODZjZmUxNGQ5NmYxZmIyNTRiOTg1Y2Y5NjYzMDM0NzMzNWVjYTYyYjNjMjlkMThmZWRhYjZhZWYzNzliZjI1ZWM2YjExZmJlODUyMTI3YjFjNTU4Y2I5OGM1ZGFjNzNmNDA0N2Q2NjAzYzY4ZDZiYzUzZTcxYzE1ZjA5OTAwMmVkNWM2YjlmYTFjY2U3ZTQwOWU4NzVhZTlmMDEyYmU3NDVhYTVmOWEyYTVjOGUxNzUzNjI2Y2U3NTRkNmQyYTExMjUzNGJhYWVkMzgyOTMzZDFjOTVhOGVhODM3OV83XzI0MTkxNGNi; ab_sr=1.0.1_ZDg0NDMwZGY4ZWZiMTA5YjgzMmVlMDU0M2MxZDRkMzY4NDQ3MGI4YThlNjNhYTFiMGJhZTUzNzRkZTI5NjI5NzUwMGNkYjBmZTQ3MTBhN2FkMjgyMDg5OGNkMTkyOTg5M2UxYmNjYmE3NzUyZGM1ZGM4N2M5NzliNzBlYTg3ZTJlNjMwNTU3OTdjMmFkNTRjMDg3OTEyMDJiMjg2MmU5NGMzZjdiM2U3NjUyZTBjNjg1ODEyYTc5Yzk5MTI5NTAw',
    }
    data = {
        'kw': keyword,
    }
    response = requests.post(url=url, data=data, headers=headers)
    page_text = response.json()
    # page_text = page_text['data']
    return page_text
```

### 3、爬取豆瓣电影详情数据

https://movie.douban.com/chart

难题：动态加载的数据

动态加载的数据：

- 无法每次实现可见即可得
- 非固定URL请求到的数据

**判断是否动态加载数据小技巧**：进入抓包工具，在preview页面搜索页面数据，不能搜索到即为动态加载

定位数据包（不是都能定位到）：原因：如果动态加载的数据是经过加密的密文数据

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255161.png)

从该数据包可以获取：

- 请求的URL
- 请求方式
- 请求携带的参数
- 看到响应的数据

**解析json数据时出错**：【Python】JSONDecodeError: Expecting value: line 1 column 1 (char 0)

https://blog.csdn.net/qq_29757283/article/details/98252728

原因：但是因为传递给 json.loads 的参数不符合 JSON 格式，所以抛出异常。

- 键值对使用单引号而非双引号。
- 参数为（或含有）普通的字符串格式（plain or html）。

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255162.png)

[**pandas创建空dataframe**](https://blog.csdn.net/chixujohnny/article/details/54133866)

[**Python Pandas 向DataFrame中添加一行/一列**](https://www.jianshu.com/p/936ad27d9865)

```python
def douban_movies():
    url = 'https://movie.douban.com/j/new_search_subjects'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '92.0.4515.131 Safari/537.36'
    }
    params = {
        'sort': 'U',
        'range': '0,10',
        'tags': '',
        'start': '0',
    }
    response = requests.get(url=url, params=params, headers=headers)
    page_text = response.json()  # .json()获取字符串形式的json数据序列化成列表
    df = pd.DataFrame(columns=['电影名', '评分'])  # 数据写入dataframe
    # 解析出电影的名称+评分
    id = 0
    for movie in page_text['data']:
        df.loc[id] = [movie['title'], movie['rate']]
        id += 1
    return df
# 多次爬取后有反爬机制，需登录操作
```

### 4、分页操作——爬取肯德基餐厅位置

- URL：http://www.kfc.com.cn/kfccda/storelist/index.aspx
- 录入关键字并按搜索才加载出位置信息：发起的是Ajax请求
- 基于抓包工具定位到该Ajax请求的数据包，从该数据包中捕获到：

- - 请求的URL
  - 请求方式（GET or POST）
  - 请求携带的参数（一般在headers最后）
  - 看到响应数据

- 跟GET请求参数动态化的封装不同的是封装为data，不是params
- 爬取多页数据：修改参数并加入循环

```python
def kfc_info():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '92.0.4515.131 Safari/537.36'
    }
    df = pd.DataFrame(columns=['餐厅名', '详细位置'])
    id = 0
    for page in range(1, 9):
        data = {
            'cname': '',
            'pid': '',
            'keyword': '广州',
            'pageIndex': str(page),
            'pageSize': '10',
        }

        response = requests.post(url=url, data=data, headers=headers)
        page_text = response.json()

        for dic in page_text['Table1']:
            df.loc[id] = [dic['storeName'], dic['addressDetail']]
            id += 1
    return df
```

### 5、药监局数据

爬取[药监局](http://scxk.nmpa.gov.cn:81/xk/)中的企业详情数据

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255163.png)

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255164.png)

- 不用数据解析
- 数据都是动态出来的（Ajax请求）
- 突破点：每个企业的详情页的参数id是列表页的id

```python
def get_canpanysid(pageNum=None):
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '92.0.4515.131 Safari/537.36'
    }
    df = pd.DataFrame(columns=['企业名称', 'ID'])
    id = 0
    for page in range(1, pageNum+1):
        data = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }

        response = requests.post(url=url, data=data, headers=headers)
        page_text = response.json()

        for dic in page_text['list']:
            df.loc[id] = [dic['EPS_NAME'], dic['ID']]
            id += 1
    return df

def get_canpanysinfo(pageNum=None):
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '92.0.4515.131 Safari/537.36'
    }
    df = pd.DataFrame(columns=['企业名称', '许可证编号', '许可项目', '企业住所', '生产地址', '社会信用代码', '法定代表人',
                               '企业负责人', '质量负责人', '发证机关', '签发人', '日常监督管理机构', '日常监督管理人员',
                               '有效期至', '发证日期', '状态', '投诉举报电话'])
    ID_df = get_canpanysid(pageNum=pageNum)
    id = 0
    for ID in ID_df['ID']:
        data = {
            'id': ID,
        }
        response = requests.post(url=url, data=data, headers=headers)
        response.encoding = 'utf-8'
        page_text = response.json()
        df.loc[id, '企业名称'] = page_text['epsName']
        df.loc[id, '许可证编号'] = page_text['productSn']
        df.loc[id, '许可项目'] = page_text['certStr']
        df.loc[id, '企业住所'] = page_text['epsAddress']
        df.loc[id, '生产地址'] = page_text['epsProductAddress']
        df.loc[id, '社会信用代码'] = page_text['businessLicenseNumber']
        df.loc[id, '法定代表人'] = page_text['legalPerson']
        df.loc[id, '企业负责人'] = page_text['businessPerson']
        df.loc[id, '质量负责人'] = page_text['qualityPerson']
        df.loc[id, '发证机关'] = page_text['qfManagerName']
        df.loc[id, '签发人'] = page_text['xkName']
        df.loc[id, '日常监督管理机构'] = page_text['rcManagerDepartName']
        df.loc[id, '日常监督管理人员'] = page_text['rcManagerUser']
        df.loc[id, '有效期至'] = page_text['xkDate']
        df.loc[id, '发证日期'] = page_text['xkDateStr']
        df.loc[id, '状态'] = '正常'
        df.loc[id, '投诉举报电话'] = '12331'
        id += 1

    df.to_csv('canpanysinfo.csv', encoding='utf-8')
    return df

```

## Urllib 网络请求库

[urllib库的使用-CSDN博客](https://blog.csdn.net/m0_43404934/article/details/122330996)

<font color=red>**requests是对urllib的进一步封装，因此在使用上显得更加的便捷，建议在实际应用当中尽量使用requests**</font>

# 数据解析

## **页面解析和数据提取**

一般来讲对我们而言，需要抓取的是某个网站或者某个应用的内容，提取有用的价值。内容一般分为两部分，非结构化的数据 和 结构化的数据。

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255165.png" style="zoom: 67%;" />

<font color=red>不同类型的数据，我们需要采用不同的方式来处理。</font>

### **结构化的数据处理**

先有结构、再有数据（http://wangyi.butterfly.mopaasapp.com/news/api?type=war&page=1&limit=10）

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255166.png" alt="image-20231106164753548" style="zoom:67%;" />

**JSON 文件**

+ JSON Path

+ 转化成Python类型进行操作（json类）

**XML 文件**

+ 转化成Python类型（xmltodict）

+ XPath

+ CSS选择器

+  正则表达式

### **非结构化的数据处理**

先有数据，再有结构，（[http://www.baidu.com](http://www.baidu.com)/)

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255167.png" style="zoom:67%;" />

**文本、电话号码、邮箱地址**

+ 正则表达式

**HTML 文件**

+ 正则表达式
+ XPath
+ CSS选择器

## Xpath 解析数据

**lxml模块**

+ 对html或xml形式的文本提取特定的内容，就需要我们掌握lxml模块的使用和xpath语法
+ lxml模块可以利用XPath规则语法，来快速的定位HTML\XML 文档中特定元素以及获取节点信息（文本内容、属性值）

###  **导入模块**

```python
from lxml import etree
```

### 基本使用

#### 解析本地文件

```python
with open('test.html', mode='r', encoding='utf-8') as f:
	data = f.read()
html = etree.HTML(data)
```

#### **解析网络数据**

```python
import requests

url = 'http://www.baidu.com'
response = requests.get(url).content
html = etree.HTML(response) #解析模板总页面
```

### xpath解析定位

+ <font color=red>xpath解析定位后返回的是列表数据 </font>
+ <font color=red>content = html.xpath('xpath语法')</font>



 **/ 从根节点定位**

 **// 从任意节点定位**

 **选取当前节点**



**..选取父节点**





#### **[@] 属性定位**

通用写法：tag[@attrname= "attrvalue"]

如： //div 就表示直接定位到的div（有多少返回多少）

**根据class定位**

```python
content = html.xpath('//input[@class="bg s_btn"]')
print(content)
```

 **根据id定位**

```python
content = html.xpath('//input[@id="su"]')
print(content)
```

**根据name定位**

```python
content = html.xpath('//input[@name="wd"]')
print(content)
```

 **根据存在属性定位**

```python
content = html.xpath('//input[@autocomplete]')
print(content)
```

#### **[n] 索引定位**

**[n] 索引定位**
xpath 的索引从 1 开始计数

```python
content = html.xpath('//form[@id="form"]/input[2]')
print(content)
```

 **[last()] 选中最后一个**

```python 
content = html.xpath('//input[last()]')
print(content)
```

**[position()>=n] 位置条件**

```python
content = html.xpath('//input[position()>=10]')
print(content)
```

+ 定位思路：先定位独一的，再思考定位不是单独的

+ 查找的方法是：是根据定位全面查找（仅仅得到单一的）是可以用，但要得到页面对应的多个数据必须先找到大点的范围再用遍历拿到多个东西

#### [attr[n]>=m] 通过子节点值修饰

```python 
content = html.xpath('//a[span[1]>2]')
print(content)
```

 #### *** 通配符**

```python
content = html.xpath('//*[@id="su"]')
print(content)
```

#### **[@ and @] 多属性定位**

```python
content = html.xpath('//*[@name="wd" and @class="s_ipt"]')
print(content)
```

####  **| 多条件定位**

符合一个条件即可定位

```python
content = html.xpath('//[@id="su"] | //[@class="bg s_btn"]')
print(content)
```

#### **模糊匹配**

 **[starts-with(@,value) 属性值开头匹配**

```Python
content = html.xpath('//*[starts-with(@class,"bg")]')
print(content)
```

**[starts-with(@,value) 文本开头匹配**

```Python
content = html.xpath('//*[starts-with(text(),"bg")]')
print(content)
```

**contains(@attr,value) 属性值包含匹配**

```Python
content = html.xpath('//*[contains(@class,"s_btn")]')
print(content)
```

**contains(text(),value) 文本包含匹配**

```Python
content = html.xpath('//*[contains(text(),"s_btn")]')
print(content)
```

#### **/text() 获取元素文本**

+ /text()    获取的是标签中直系的文本内容

+ //text()   标签中非直系的文本内容(所有的文本内容)

```python
title = html.xpath('//title/text()')[0]
print(title)
```

####  **/@attr  获取属性值**

```python
content = html.xpath('//*[@id="su"]/@value')
download_page.xpath(".//div[@class='downbody']/div[@class='dian']/a[1]/@href")
```

## **JsonPath 解析数据**

如果有一个多层嵌套的复杂字典，想要根据key和下标来批量提取value，这是比较困难的。jsonpath模块就能解决这个痛点。

### **导入模块**

```python
import json
import jsonpath
```

[JsonPath 解析数据 (yuque.com)](https://www.yuque.com/weicreate/111/jsonpath#eWkxQ)







## BeautifulSoup 解析数据

+ 简称bs4

+ Beautiful Soup 是一个HTML/XML的解析器，主要的功能是解析和提取 HTML/XML 数据。
+ Beautiful Soup 是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml。
+ BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器。

[BeautifulSoup 解析数据 (yuque.com)](https://www.yuque.com/weicreate/111/beautifulsoup)

[BeautifulSoup 官网](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

BeautifulSoup 是一个可以从HTML或XML文件中提取数据的Python库。它能够通过你喜欢的转换器实现惯用的文档导航，查找，修改文档的方式。Beautiful Soup会帮你节省数小时甚至数天的工作时间。

```python
pip install bs4
```

以下示例, 爬取一个简单的静态网页:

```python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.dbmeinv.com/'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36' }
response = requests.get(url=url, headers=headers)
content = response.content.decode()

soup = BeautifulSoup(content, 'html.parser')  # 注释1
img_list = soup.find_all(name='img', class_='height_min')  # 注释2

for img in img_list:  # 注释3
    src = img.attrs['src']
    title = img.attrs['title']  # 注释4
    response = requests.get(url=src, headers=headers)
    content = response.content
    
    imagesPath = 'images'
    if not os.path.exists(imagesPath):
        os.makedirs(imagesPath)
    with open('%s/%s.jpg' % (imagesPath, title), 'wb') as f:  # 注释5
        f.write(content)
```

+ 注释1：这里新建了一个Beautifulsoup对象，它有两个必要的参数，第一个参数是HTML代码对象，比如这里content存储了URL为"https://www.dbmeinv.com/"的这张网页的HTML代码，它是个字符串或者是一个文件句柄第二个参数是HTML解析器，这个解析器可以使用内置标准的"html.parser"，也可以安装第三方的解析器，比如lxml和html5lib。

| 解析器           | 使用方法                                                     | 优势                                                  | 劣势                                            |
| ---------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------- |
| Python标准库     | BeautifulSoup(markup, "html.parser")                         | Python的内置标准库执行速度适中文档容错能力强          | Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | BeautifulSoup(markup, "lxml")                                | 速度快文档容错能力强                                  | 需要安装C语言库                                 |
| lxml XML 解析器  | BeautifulSoup(markup, ["lxml", "xml"]) BeautifulSoup(markup, "xml") | 速度快唯一支持XML的解析器                             | 需要安装C语言库                                 |
| html5lib         | BeautifulSoup(markup, "html5lib")                            | 最好的容错性以浏览器的方式解析文档生成HTML5格式的文档 | 速度慢不依赖外部扩展                            |

比如安装 lxml HTML 解析器: pip install lxml

如果安装不成功, 可以到 [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 下载 lxml 模块, 比如 lxml-4.1.1-cp35-cp35m-win32.whl, 下载完成后到下载目录执行 pip install lxml-4.1.1-cp35-cp35m-win32.whl 即可安装。

+ 注释2：这里使用了soup对象的一个方法"find_all()"，字面理解就是"找出所有的"，那么找出什么，如何定位这个所谓的"什么"？这里就要传入两个参数，第一个是HTML文档的节点名，也可以理解为HTML的标签名；第二个则是该节点的class类名，比如上面代码中，我要找出该网页上所有的img节点，且我需要的img节点的类名为"height_min", 因为calss和关键字冲突，所以改名class_。但是对于一些没有class类名的HTML元素我们该如何寻找？

我们还可以用到另一个属性：attrs，比如这里可以写成：

```python
img_list = soup.find_all(name='img', attrs={'class': 'height_min'})
```

attrs是字典类型，冒号左边为关键字，右边为关键字的值。不一定要通过class来查找某一个元素，也可以通过比如"id"，"name"，"type"等各种HTML的属性，如果想要的元素实在没有其他属性，可以先定位到该元素的父属性，再使用.children定位到该元素。

+ 注释3：注释2返回的是一个列表对象，包含了整张网页上的图片，因此这里用一个循环，分别处理每一张图片。
+ 注释4：取出了图片的路径和标题。
+ 注释5：这里需要重新请求图片的地址，获得图片二进制的返回值，因为是图片，所以不能用decode()解码，必须以二进制的方式写入，后面的写入模式"wb"，加了个"b"就是表示以二进制的形式。

也可以将解码的工作放到 bs4 中:

```python
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
```

如果本身是 utf-8 编码，可省略 from_encoding 参数。

## **案例**

 **站长素材美女图片**

```python
import requests
from fake_useragent import UserAgent
from lxml import etree


def crawl_data(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/meinvtupian.html'
    else:
        url = f'https://sc.chinaz.com/tupian/meinvtupian_{page}.html'

    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    title_list = html.xpath('//div[@id="container"]//img/@alt')
    src_list = html.xpath('//div[@id="container"]//img/@src')
    for i in range(len(title_list)):
        title = title_list[i]
        src = 'https:' + src_list[i].replace('_s.', '.')
        yield title, src


def save_to_img(title, src):
    headers = {'User-Agent': UserAgent().random}
    data = requests.get(url=src, headers=headers).content
    with open(f'站长素材/{title}.png', mode='wb') as file:
        file.write(data)
    print(f'图片下载成功：站长素材/{title}.png')


def main():
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页码：'))
    print('-' * 50)
    for page in range(start, end + 1):
        for title, src in crawl_data(page):
            save_to_img(title, src)
    print('-' * 50)
    print('下载完毕')


if __name__ == '__main__':
    main()
```

**电影天堂国内电影**

```python
import requests
from fake_useragent import UserAgent
from lxml import etree


def crawl_data(page):
    url = f'https://www.ygdy8.net/html/gndy/china/list_4_{page}.html'
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    title_list = html.xpath('//div[@class="co_content8"]/ul//a[2]/text()')
    href_list = html.xpath('//div[@class="co_content8"]/ul//a[2]/@href')
    for i in range(len(title_list)):
        title = title_list[i]
        href = 'https://www.ygdy8.net/' + href_list[i]
        response = requests.get(url=href, headers=headers)
        response.encoding = 'gbk'
        html = etree.HTML(response.text)
        src = html.xpath('//*[@id="Zoom"]//img/@src')[0]
        yield title, src


def save_to_img(title, src):
    headers = {'User-Agent': UserAgent().random}
    data = requests.get(url=src, headers=headers).content
    with open(f'电影天堂/{title}.png', mode='wb') as file:
        file.write(data)
    print(f'图片下载成功：站长素材/{title}.png')


def main():
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页码：'))
    print('-' * 50)
    for page in range(start, end + 1):
        for title, src in crawl_data(page):
            save_to_img(title, src)
    print('-' * 50)
    print('下载完毕')


if __name__ == '__main__':
    main()
```

# 验证码

反爬机制：验证码，识别验证码图片中的数据，用于模拟登陆操作。

识别验证码的操作：

+ 人工肉眼识别（不推荐）
+ 第三方自动识别（推荐）
  + 超级鹰网站

## **Pytesseract 验证码识别**

Tesseract

●Tesseract 是一个 OCR 库,目前由 Google 赞助(Google 也是一家以 OCR 和机器学习技术闻名于世的公司)。Tesseract 是目前公认最优秀、最精确的开源 OCR 系统，除了极高的精确度，Tesseract 也具有很高的灵活性。它可以通过训练识别出任何字体，也可以识别出任何 Unicode 字符。

2 安装Tesseract-ocr

Windows 系统

●下载地址：https://github.com/UB-Mannheim/tesseract/wiki

●下载地址2：https://digi.bib.uni-mannheim.de/tesseract/

2 Linux 系统

●可以通过 apt-get 安装: $sudo apt-get tesseract-ocr



3 配置环境变量

●将“D:\Tesseract-OCR”添加到环境变量 path 中

●将语言字库文件夹添加到环境变量中，增加一个 TESSDATA_PREFIX 变量名，变量值为安装路径：D:\Tesseract-OCR\tessdata 



4 安装pytesseract

●Tesseract 是一个 Python 的命令行工具，不是通过 import 语句导入的库。安装之后,要用 tesseract 命令在 Python 的外面运行，但我们可以通过 pip 安装支持Python 版本的 Tesseract库：pip install pytesseract



4 pytesseract模块

●用PIL模块读取图片，使用pytesseract模块的image_to_string()方法识别图片

```
import pytesseract
from PIL import Image

image = Image.open('test.jpg')
text = pytesseract.image_to_string(image)
print(text)
```



##  **Ddddocr 识别验证码**

### 导入模块

```
import ddddocr
```

### 创建DdddOr对象

```
ocr = ddddocr.DdddOcr(old=False, show_ad=False)
```

### 识别验证码

#### 识别base64编码的验证码

●编码值不包含图片头

```
img_base64 = 'img_base64'
res = ocr.classification(img_base64=img_base64)
print(res)
```

识别英文数字验证码

![code.png](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255168.png)

```
with open('code.png', mode='rb') as file:
	code_img = file.read()
res = ocr.classification(code_img)
print('识别英文数字验证码：' + res)
```

识别汉字验证码

![image-20231107220522245](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255169.png)

```
with open("code2.png", mode='rb') as file:
	code_img = file.read()
res = ocr.classification(code_img)
print('识别汉字验证码：' + res)
```

识别算术验证码

![](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255170.png)

```
import re

with open('code3.png', mode='rb') as file:
code_img = file.read()
res = ocr.classification(code_img)
res = eval(re.match(r'(.*)=', res).group(1))
print('识别算术验证码：' + str(res))
```

### 切换老版本模式

●由于事实上确实在一些图片上老版本的模型识别效果比新模型好

●通过在初始化 ddddocr 的时候使用 old 参数即可快速切换老模型

```
ocr = ddddocr.DdddOcr(old=True, show_ad=False)
with open("code3.png", 'rb') as f:
	image = f.read()
res = ocr.classification(image)
print('识别验证码：' + res)
```

### 滑块验证码

滑块与背景识别

![](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255171.png)

```
with open('block.png', mode='rb') as file:
	code_block = file.read()
with open('bg.png', mode='rb') as file:
	code_bg = file.read()

res = ocr.slide_match(code_block, code_bg).get('target')
print('滑块验证码(长滑块)：', end='')
print({'x1': res[0], 'y1': res[1], 'x2': res[2], 'y2': res[3]})
```

●小滑块为单独的透明png图片，高度与背景高度一致

绘制矩形

![](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255172.png)

●rectangle：绘制矩形

●pt1：(x1,y1)

●pt2：(x2,y2)

●color：RGB颜色

●thickness：线条粗度

```
import cv2

bg = cv2.imread('bg.png')
img = cv2.rectangle(bg, (res[0], res[1]), (res[2], res[3]),
color=(0, 0, 255), thickness=2)
cv2.imwrite('bg_box.png', img)
```

simple_target参数

![image-20231107220457595](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255173.png)

●如果小滑块无过多背景部分，则可以添加 simple_target 参数

```
with open('block2.png', mode='rb') as file:
	code_block = file.read()
with open('bg2.png', mode='rb') as file:
	code_bg = file.read()

res = ocr.slide_match(code_block, code_bg, simple_target=True).get('target')
print('滑块验证码(纯滑块)：', end='')
print({'x1': res[0], 'y1': res[1], 'x2': res[2], 'y2': res[3]})

bg = cv2.imread('bg2.png')
img = cv2.rectangle(bg, (res[0], res[1]), (res[2], res[3]),
color=(0, 0, 255), thickness=2)
cv2.imwrite('bg2_box.png', img)
```

坑位与背景识别

![image-20231107220440861](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255174.png)

```
with open('block3.png', mode='rb') as file:
	code_block = file.read()
with open('bg3.png', mode='rb') as file:
	code_bg = file.read()

res = ocr.slide_comparison(code_block, code_bg).get('target')
print('滑块验证码(坑位)：' + str({'x': res[0], 'y': res[1]}))

bg = cv2.imread('block3.png')
img = cv2.rectangle(bg, (res[0], res[1]), (res[0] + 50, res[1] + 50),
color=(0, 0, 255), thickness=2)
cv2.imwrite('bg3_box.png', img)
```

### 点选验证码

1 切换目标检测模式

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255175.png" alt="image-20231107220534907" style="zoom:67%;" />

●默认为识别文字模式，为 det=True 则开启目标检测模式

```
ocr = ddddocr.DdddOcr(show_ad=False)
xy_ocr = ddddocr.DdddOcr(det=True, show_ad=False)
```

2 处理图片

1 截取图片上下部分

●cv2截取图片：img[y1:y2,x1:x2]

```
img = cv2.imread('code6.png')
height, width = img.shape[:2]
img_top = img[0:height - 40, 0:width]
img_down = img[height - 40:height, 0:150]
```

cv2转二进制

```
import numpy as np

img_top2 = np.array(cv2.imencode('.png', img_top)[1]).tobytes()
img_down2 = np.array(cv2.imencode('.png', img_down)[1]).tobytes()
```

3 识别下部分图片

```
res = ocr.classification(img_down2)
down_text = list(res)
print(down_text)
```

4 识别上部分图片

●返回坐标列表

```
res = xy_ocr.detection(img_top2)
```

 识别坐标区域文字

```
xy_dict = {}
for xy in res:
	x1, y1, x2, y2 = xy
	img = img_top[y1:y2, x1:x2]
	img2 = np.array(cv2.imencode('.png', img)[1]).tobytes()
	res = ocr.classification(img2)
	xy_dict[res] = [x1, y1, x2, y2]

print(xy_dict)
```

**按图片下部分匹配汉字坐标**

```
for text in down_text:
	res = xy_dict[text]
	xy = {'x1': res[0], 'y1': res[1], 'x2': res[2], 'y2': res[3]}
	print(text, xy)
```



**按图片下部分匹配汉字坐标中心点**

```
for text in down_text:
	x1, y1, x2, y2 = xy_dict[text]
	center = {'x': x1 + (x2 - x1) / 2, 'y': y1 + (y2 - y1) / 2}
	print(text, center)
```



# Scrapy框架

[Scrapy](https://scrapy.org/) 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。

Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

## scrapy架构组成:crossed_swords:

●engine：引擎，处理整个系统的数据流处理、触发事务，是整个框架的核心。

●**Item：项目，定义数数据结构**

●**spiders：爬虫，创建requests对象和接收引擎发送的response，解析数据**

●scheduler：调度器，接收并处理引擎发送的requests对象

●downloader：下载器，接收处理好的requests对象，爬取并返回响应数据到引擎

●**item pipeline：数据管道，储存和处理spiders解析好的数据**

●**downloader middleware：下载器中间件，位于引擎和下载器之间的钩子**

●**spider middlewares：爬虫中间件，位于引擎和爬虫爬虫之间的钩子**

## scrapy工作原理

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255176.png)1引擎向spiders要url
2spiders将url发送给引擎
3引擎将url发送给scheduler(调度器)
4scheduler生成requests对象并放入指定的队列中
5引擎根据队列发送requests对象到downloader(下载器)
6downloader爬取数据，并将response数据返回给引擎
7引擎将response数据发送给spiders
8spiders解析response数据，并将解析好的数据发送给引擎
9引擎得到数据后,将数据发送给pipeline
10pipeline储存和处理解析好的数据

### Scrapy 安装

```cmd
pip install scrapy
```

## **开发流程:crossed_swords:**

### 创建爬虫项目

项目名开头不为数字，不包含中文

```shell
$ scrapy startproject spidersXXXX
```

例子

```shell
$ scrapy startproject spiderTest
```

Scrapy 项目结构

```shell
spiderTest/
    scrapy.cfg            # 项目的配置文件
    spiderTest/           # 用来放你py代码的地方
        __init__.py
        items.py          # 用来定义你抓取内容的字段
        middlewares.py    # 中间器
        pipelines.py      # 管道文件
        settings.py       # 设置
        spiders/          # 放爬虫文件的文件夹
            __init__.py
```

### pycharm创建项目依赖

#### pycharm打开项目

![image-20231106212922251](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255177.png)

![image-20231106213057787](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255178.png)

效果

![image-20231106213131278](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255179.png)

#### 安装虚拟环境的Scrapy

点开pycharm里的项目终端

```shell
pip install scrapy

#or
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scrapy
```

![](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255180.png)

### **创建蜘蛛文件**

```shell
$ cd spidersXXXX
$ scrapy genspider 爬虫文件名 允许爬取的域名
```

例子: 爬取豆瓣

```shell
$ scrapy genspider douban movie.douban.com
```

```shell
PS C:\Users\16658\Desktop\python_note\爬虫\Python爬虫\code\spiderTest> scrapy genspider douban movie.douban.com
Created spider 'douban' using template 'basic' in module:
  spiderTest.spiders.douban
PS C:\Users\16658\Desktop\python_note\爬虫\Python爬虫\code\spiderTest> 
```

```
spiderTest/
    scrapy.cfg            # 项目的配置文件
    spiderTest/           # 用来放你py代码的地方
        __init__.py
        items.py          # 用来定义你抓取内容的字段
        middlewares.py    # 中间器
        pipelines.py      # 管道文件
        settings.py       # 设置
        spiders/          # 放爬虫文件的文件夹
            __init__.py
            douban.py     #爬虫文件
```

![image-20231106214122318](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255181.png)

![image-20231106214106747](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255182.png)

###  **运行爬虫**

**命令行运行**

```shell
scrapy crawl 爬虫名称
```

**运行并保存为json文件**

```
scrapy crawl 爬虫名称 - o filename.json
```

**保存csv文件**

```
scrapy crawl 爬虫名称 - o filename.csv
```

**通过mian文件运行**

```python
from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', '爬虫名称'])
```

### **scrapy shell**

在命令行使用scrapy shell 进行调试

```shell
scrapy shell 待爬取的网站
```

```
$ scrapy shell http://lab.scrapyd.cn
2019-01-12 13:52:25 [scrapy.core.engine] INFO: Spider opened
2019-01-12 13:52:26 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://lab.scrapyd.cn/robots.txt> (referer: None)
2019-01-12 13:52:26 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://lab.scrapyd.cn> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x000001F5CB69FB70>
[s]   item       {}
[s]   request    <GET http://lab.scrapyd.cn>
[s]   response   <200 http://lab.scrapyd.cn>
[s]   settings   <scrapy.settings.Settings object at 0x000001F5CB69FA90>
[s]   spider     <DefaultSpider 'default' at 0x1f5cb94d4a8>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> view(response)
True
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>SCRAPY爬虫实验室 - SCRAPY中文网提供</title>'>]
```



##  **开发爬虫**

### 基本方法

```python
import scrapy
from spiderTest.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "爬虫的名称"
    allowed_domains = ["允许的域名"]
    start_urls = ["要爬取的网站"]

    # 解析数据
    def parse(self, response):  
		pass
```

例子

```python
import scrapy
class simpleUrl(scrapy.Spider):
    name = "simpleUrl"
    start_urls = [  #另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)
```

**response的属性**

+ 返回响应数据的响应url

  ```
  response.url
  ```

+ 返回响应数据对应的请求url

  ```
  response.request.url
  ```

+  返回响应数据的响应请求头

  ```
response.headers
  ```

+ 返回响应数据的对应的请求头

  ```
  response.request.headers
  ```

+ 返回响应数据的文本内容

  ```
  response.text
  ```

+ 返回响应数据的二进制形式

  ```
  response.body
  ```

+  **将爬虫原始url与value拼接**

  ```
  response.urljoin(value)
  ```

+  **响应数据执行xpath语法**

  ```python
  result = response.xpath(xpath)
  ```

### **提取内容**

使用 extract() 方法提取获取到的内容, 返回的是一个 list, 如果只想获取其匹配的第一条数据, 使用 extract_first()。比如:

+ 提取selector对象或列表的data属性值

  ```
  selector.extract()
  ```

+  提取selector列表第一个数据的data属性值

  ```
  selector.extract_first()
  ```

注意:

+ 没有使用 extract() 的时候，提取出来的内容依然具有选择器属性，可以继续使用里面的内容进行提取下级内容
+ 使用了 extract() 之后，提取出来的内容就会变成字符串格式了。不能进行多级提取的时候。
+ 值得注意的是，选择器提取出来的内容是放在列表里面的，即使没有内容，那也是一个空列表

### **Items —使用数据结构**

要在items文件中定义数据结构

```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 继承scrapy.Item
class SpidertestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()

# Item对象2
class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()

# Item对象3 
# ......
class SpiderItem(scrapy.Item):
	fieldName1 = scrapy.Field()
	fieldName2 = scrapy.Field()
```


yield 将数据结构发送给pipelines(数据管道)

```python
import scrapy
from spiderTest.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "爬虫的名称"
    allowed_domains = ["允许的域名"]
    start_urls = ["要爬取的网站"]

    # 解析数据
	def parse(self, response):
        item = SpidertestItem()  # 创建 SpidertestItem
        item['title'] = '解析数据1'
        item['rank'] = '解析数据2'
        item['subject'] = '解析数据3'
        yield item
```

### **实现多页爬虫**

 实现多页爬虫
●scrapy.Request：构造请求
●url：请求地址
●callback：要调用的爬虫方法名称
●dont_filter：不过滤该请求地址
●注意：要修改allowed_domains或者使用dont_filter，防止访问被屏蔽

```python
class Spider(scrapy.Spider):
	name = ''
	allowed_domains = []
	start_urls = []
	
	def parse(self, response):
		...
        
        # 参数: new_url callback dont_filter
		yield scrapy.Request(url=new_url, callback=self.parse, dont_filter=True)
```

### 定义二级爬虫

+ 对第一次爬取数据得到的链接进行二次处理
+ meta：添加字典属性，将指定的字典发送给二级爬虫方法的response对象里

```python
class Spider(scrapy.Spider):
	name = ''
	allowed_domains = []
	start_urls = []
	
	def parse(self, response):
		...
		yield scrapy.Request(url=url, callback=self.parse2, meta={'fieldname': value})
	
	def parse2(self, response):
		response.meta.get('fieldname')
		...
		yield item
```

### **携带cookies请求**

重写start_requests方法, 构造请求携带cookie

```python
class Spider(scrapy.Spider):
	name = ''
	allowed_domains = []
	
	def start_requests(self):
		url = ''
		cookie = ''
		yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)
	
	
	def parse(self, response):
		pass
```

###  **post请求**

重写start_requests方法，构造请求携带formdata

```python
class Spider(scrapy.Spider):
	name = ''
	allowed_domains = []
	
	def start_requests(self):
		url = ''
		data = {}
		headers = {}
		yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)
	
	def parse(self, response):
		pass
```

### **链接提取器**

crawlspider经常应用于一级爬虫，二级爬虫一般使用spider

#### **创建爬虫项目**

```
scrapy startproject 项目名
```

#### 创建CrawlSpider爬虫文件

```
scrapy genspider - t crawl 爬虫文件名 允许爬取的域名
```

#### 爬虫类结构
●rules：过滤链接
●allow：正则匹配链接
●callback：要调用的爬虫方法名称
●follow：链接跟进，获取每页符合的链接，爬虫会自动过滤重复链接
●注意：rules可添加多个Rule来提取链接

```python
class CrawlSpider(CrawlSpider):
	name = 'spiderName'
	allowed_domains = ['']
	start_urls = ['']
	
	rules = (
		Rule(LinkExtractor(allow=r'Items/'),
			 callback='parse_item',
			 follow=False),
		...
	)

	def parse_item(self, response):
		pass
```

## **Scrapy选择器**

### 基础

最关键的就是如何从繁杂的网页中把我们需要的数据提取出来，python从网页中提取数据的包很多，常用的有下面的几个：

+ BeautifulSoup 它基于HTML代码的结构来构造一个Python对象， 对不良标记的处理也非常合理，但是速度上有所欠缺。
+ lxml 是一个基于 ElementTree (不是Python标准库的一部分)的python化的XML解析库(也可以解析HTML)。

可以在scrapy中使用任意你熟悉的网页数据提取工具，但是，scrapy本身也为我们提供了一套提取数据的机制，称之为选择器(seletors)，通过特定的 XPath 或者 CSS 表达式来“选择” HTML文件中的某个部分。XPath 是一门用来在XML文件中选择节点的语言，也可以用在HTML上。 CSS 是一门将HTML文档样式化的语言。选择器由它定义，并与特定的HTML元素的样式相关连。

示例: 使用 Selector 的 css 或 xpath 方法提取 www.xiaoyulive.top 的标题

css 提取

```python

import scrapy
from scrapy.selector import Selector

class test(scrapy.Spider):
    name = "xiaoyu"
    start_urls = ['https://www.xiaoyulive.top/']
    def parse(self, response):
        selector = Selector(response=response)
        title = selector.css('head title::text')
        print(title)

```

xpath 提取

```python
import scrapy
from scrapy.selector import Selector

class test(scrapy.Spider):
    name = "xiaoyu"
    start_urls = ['https://www.xiaoyulive.top/']
    def parse(self, response):
        selector = Selector(response=response)
        title = selector.xpath('//title/text()')
        print(title)
```

### CSS 提取

使用示例:

```
response.css('title') # 提取整条title标签
response.css('title::text') # 提取title的InnerHTML(内容)
response.css(".content img::attr(src)") # 提取img的src属性值
response.css(".navigator a::attr(href)") # 提取a标签的href属性值
```

一些常用的选择器

| 选择器               | 示例                  | 示例说明                                                  |
| -------------------- | --------------------- | --------------------------------------------------------- |
| .class               | .intro                | 选择所有class="intro"的元素                               |
| #id                  | #firstname            | 选择所有id="firstname"的元素                              |
| *                    | *                     | 选择所有元素                                              |
| element              | p                     | 选择所有<p>元素                                           |
| element,element      | div,p                 | 选择所有<div>元素和<p>元素                                |
| element element      | div p                 | 选择<div>元素内的所有<p>元素                              |
| element>element      | div>p                 | 选择所有父级是<div>元素的<p>元素                          |
| element+element      | div+p                 | 选择所有紧接着<div>元素之后的<p>元素                      |
| element1~element2    | p~ul                  | 选择<p>元素之后的每一个<ul>元素                           |
| [attribute]          | [target]              | 选择所有带有target属性元素                                |
| [attribute="value"]  | [target=_blank]       | 选择所有使用target="_blank"的元素                         |
| [attribute~="value"] | [title~=flower]       | 选择title属性包含单词"flower"的所有元素                   |
| [attribute^="value"] | img[src^="https"]     | 选择每一个src属性的值以"https"开头的元素                  |
| [attribute$="value"] | img[src$=".pdf"]      | 选择每一个src属性的值以".pdf"结尾的元素                   |
| [attribute*="value"] | img[src*="runoob"]    | 选择每一个src属性的值包含子字符串"runoob"的元素           |
| :link                | a:link                | 选择所有未访问链接                                        |
| :visited             | a:visited             | 选择所有访问过的链接                                      |
| :active              | a:active              | 选择活动链接                                              |
| :hover               | a:hover               | 选择鼠标在链接上面时                                      |
| :before              | p:before              | 在每个<p>元素之前的伪元素                                 |
| :after               | p:after               | 在每个<p>元素之后的伪元素                                 |
| :nth-child(n)        | p:nth-child(2)        | 选择每个p元素是其父级的第二个子元素                       |
| :nth-of-type(n)      | p:nth-of-type(2)      | 选择每个p元素是其父级的第二个p元素                        |
| :nth-last-child(n)   | p:nth-last-child(2)   | 选择每个p元素的是其父级的第二个子元素，从最后一个子项计数 |
| :nth-last-of-type(n) | p:nth-last-of-type(2) | 选择每个p元素的是其父级的第二个p元素，从最后一个子项计数  |
| :first-child         | p:first-child         | 选择每个p元素是其父级的第一个子级。                       |
| :last-child          | p:last-child          | 选择每个p元素是其父级的最后一个子级。                     |
| :focus               | input:focus           | 选择具有焦点的输入元素                                    |
| :checked             | input:checked         | 选择每个选中的输入元素                                    |
| :not(selector)       | :not(p)               | 选择每个并非p元素的元素                                   |
| :first-letter        | p:first-letter        | 选择每一个<p>元素的第一个字母                             |
| :first-line          | p:first-line          | 选择每一个<p>元素的第一行                                 |

### XPath 提取

使用示例:

```
response.xpath("//@href")
response.xpath("//ol//@href")
response.xpath("//ol[@class='page-navigator']//@href")
response.xpath("//title//text()")
response.xpath("//div[@class='post-content']//text()")
response.xpath("string(//div[@class='post-content'])")
```

XPath 表达式

| 表达式   | 描述                                                     |
| -------- | -------------------------------------------------------- |
| nodename | 选取此节点的所有子节点                                   |
| /        | 从根节点选取                                             |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置 |
| .        | 选取当前节点                                             |
| ..       | 选取当前节点的父节点                                     |
| @        | 选取属性                                                 |

XPath 通配符可用来选取未知的 HTML元素。

| 通配符 | 描述                 |
| ------ | -------------------- |
| *      | 匹配任何元素节点。   |
| @*     | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

| 路径表达式   | 结果                              |
| ------------ | --------------------------------- |
| /bookstore/* | 选取 bookstore 元素的所有子元素。 |
| //*          | 选取文档中的所有元素。            |
| //title[@*]  | 选取所有带有属性的 title 元素。   |

### 正则提取

如果我们想提取的内容不能使用一个选择器表示

 比如获取页脚的备案信息

```python
import scrapy
from scrapy.selector import Selector

class test(scrapy.Spider): #需要继承scrapy.Spider类
    name = "xiaoyu"
    start_urls = ['https://www.xiaoyulive.top/']
    def parse(self, response):
        selector = Selector(response=response)
        text = selector.css('.footers>p:first-child *::text').re(r'\d{8}')[0]
        print(text)
```



## **settings配置 —配置文件**

### 多配置切换

如果项目中包括多个配置，比如有如下目录结构：

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255183.png" alt="image.png" style="zoom:67%;" />

可以在scrapy.cfg 中配置：

```python
[settings]
default = ImageCrawler.settings.settings1
project1 = ImageCrawler.settings.settings1
project2 = ImageCrawler.settings.settings2
project3 = ImageCrawler.settings.settings3

[deploy]
project = ImageCrawler
```

切换配置需要设置环境变量 SCRAPY_PROJECT ，Windows下临时设置环境的命令如下：

```
set SCRAPY_PROJECT=project1
```

设置好后可以获取当前配置的名称，看是否切换成功：

```
scrapy settings --get BOT_NAME
```

然后再进行爬取即可：

```
scrapy crawl images1
```

### **配置文件详解**

在settings文件中配置爬虫的相关参数

+ 更多配置：https://www.jianshu.com/p/df9c0d1e9087

常见的配置字段如下：

```python 
# -*- coding: utf-8 -*-

# 爬虫名称
BOT_NAME = 'ImageCrawler1'

# 爬虫模块
SPIDER_MODULES = ['ImageCrawler.spiders']
NEWSPIDER_MODULE = 'ImageCrawler.spiders'

# 用户代理
# USER_AGENT = 'ImageCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules robot协议 建议修改成False
ROBOTSTXT_OBEY = True

#下载的延迟
DOWNLOAD_DELAY = 0.5

#并发请求的数量
CONCURRENT_REQUESTS = 16

# 默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 中间件
# SPIDER_MIDDLEWARES = {
#    'ImageCrawler.middlewares.ImageCrawlerSpiderMiddleware': 543,
# }

# 下载中间件
# DOWNLOADER_MIDDLEWARES = {
#    'ImageCrawler.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# 扩展
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 管道 数值代表优先级，值越小优先级越高 #设置开启的管道
ITEM_PIPELINES = {
    'ImageCrawler.pipelines.ImageCrawlerPipeline': 300,
}
 
#开启cookie传递 每次请求带上前一次的cookie，做状态保持，默认为True
COOKIES_ENABLED = True
```



获取某个字段使用命令：

```
scrapy settings --get 字段名
```

## Pipeline管道  —保存数据

> 需要在settings文件中开启数据管道

 管道类结构

```python
class SpidertestPipeline:
     def process_item(self, item, spider):
         return item
```

+ open_spider：开始爬虫前运行
+ process_item：处理item数据结构
+ close_spider：结束爬虫后运行
+ spider.name：返回对应爬虫的名称

### **Scrapy常用命令**

全局命令有如下几个: startproject、genspider、settings、runspider、shell、fetch、view、version

全局命令就是不依托项目存在的，也就是不关你有木有项目都能运行

●scrapy startproject <scrapyProjectName> 创建项目
●scrapy runspider XX.py 运行XX蜘蛛(基于文件)
●scrapy shell XX 调试网址XX
●scrapy genspider <spiderName> <websiteEnter> 根据蜘蛛模板创建蜘蛛
●scrapy settings --get BOT_NAME 获取蜘蛛的名字
●scrapy settings --get DOWNLOAD_DELAY 获取蜘蛛的下载延迟
●scrapy fetch [http://www.scrapyd.cn](http://www.scrapyd.cn/) >d:/scrapyd.html 模拟蜘蛛进行下载, 并保存到文件
●scrapy view [http://www.scrapyd.cn](http://www.scrapyd.cn/) >d:/scrapyd.html 直接在浏览器中进行查看下载的内容
●scrapy version 查看scrapy版本

项目命令有如下几个: crawl、check、list

●scrapy crawl XX 运行XX蜘蛛(基于项目)
●scrapy check XX 检查XX蜘蛛
●scrapy list 显示有多少个蜘蛛



## **middleware中间件 — 拦截响应数据**

下载器中间件

+ 在settings文件中开启中间件，权重值低的越优先执行
+ 在middlewares文件中定义中间件类

**类结构**

```Python
class DownloaderMiddleware:
	def process_request(self, request, spider):
		pass
	
	def process_response(self, request, response, spider):
		pass
	
	def process_exception(self, request, exception, spider):
		pass
```

### process_request

1 处理请求

●request通过下载中间件时，该方法被调用

2 返回值

1 None

●如果所有下载器中间件都返回None给引擎，则请求最终传给下载器处理，否则继续通过引擎传递给其他权重低的process_reqeust方法

2 Request对象

●如果返回request对象给引擎，则将reqeust对象通过引擎发送给调度器

3 Response对象

●将响应对象交给spider进行解析

### process_response

1 处理响应数据

●下载器完成请求返回响应数据时，该方法被调用

2 返回值

1 Request对象

●如果返回request对象给引擎，则将reqeust对象通过引擎发送给调度器

2 Response对象

●将响应对象交给spider进行解析







### 设置随机UA

1 定义中间件类

●在middlewares文件定义中间件类

```python
from fake_useragent import UserAgent

class RandomUserAgentMiddleware:
	def init(self):
		self.user_agent = UserAgent().random
	
	def process_request(self, request, spider):
		requests.headers['User-Agent'] = self.user_agent
```

 开启中间件
●在settings文件中开启中间件

```python
DOWNLOADER_MIDDLEWARES = {
'scrapydownloadertest.middlewares.RandomUserAgentmiddleware': 543
}
```



###  使用代理IP

代理的作用：突破id访问的限制, 隐藏自身真实的ip, 破解封ip这种反扒机制

 代理相关的网站:

+ 西司代理  
+ 快代理

代理ip的匿名度：
- 透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
- 匿名：知道使用了代理，不知道真实ip
- 高匿：不知道使用了代理，更不知道真实的ip





1 代理池

●在settings文件配置代理池

```
PROXIES_POOL = [
{'ip_port': 'http://223.96.90.216:8085'},
{'ip_port': 'http://120.220.220.95:8085'}
]
```

开启下载器中间件

●在settings文件开启下载器中间件

```
DOWNLOADER_MIDDLEWARES = {
'scrapy_proxy.middlewares.ProxyMiddleware': 543,
}
```

定义中间件类
●在middlewares文件定义中间件类
●在request的meta中添加proxy属性
●含有账号密码的IP需要进行http基本认证
●基本认证流程：请求头添加Proxy - Authorization: 'Basic ' + base64编码(user_passwd)
●注意：不能漏掉Basic的空格

```
from itemname.settings import PROXIES_POOL
import base64
import random

class ProxyMiddleware:
	def process_request(self, request, spider):
		proxy = random.choice(PROXIES_POOL)
		if 'user_passwd' in proxy:
			b64_up = base64.b64encode(proxy['user_passwd'].encode())
			request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
			request.meta['proxy'] = proxy['ip_port']
```

### 对接Selenium

1 定义中间件类

●在middlewares文件定义中间件类

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse


class SeleniumMiddleware:
    def process_request(self, request, spider):
        url = request.url
        if '地址关键字' in url:
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            data = driver.page_source
            driver.close()
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            return res
```

开启下载器中间件
●在settings文件开启下载器中间件

```
DOWNLOADER_MIDDLEWARES = {
'scrapy_selenium.middlewares.SeleniumMiddleware': 543,
}
```



## 日志信息及日志级别

1 日志级别

●CRITICAL：严重错误

●ERROR：一般错误

●WARNING：警告

●INFO：一般信息

●DEBUG：调试信息

2 设置日志级别

●在settings文件中设置

```
LOG_LEVEL = 'DEBUG'
```

保存日志文件

●在settings文件中设置

```
LOG_FILE = 'demo.log'
```



## 案例:crossed_swords:

### 豆瓣

#### 获取数据

目的：我们制作一个爬虫，用来爬取豆瓣网评分比较高的电影，并保存到文件。

地址：https://movie.douban.com/top250

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255184.png" alt="img" style="zoom:50%;" />

##### 分析页面结构

主体结构分析

![](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255185.png)

“下一页”按钮分析

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255186.png" alt="image-20231107195535820" style="zoom: 60%;" />

嵌套很明显了，很简单的页面结构，接下来就开始编写爬虫。

##### **创建scrapy项目**

```cmd
scrapy startproject douban
cd douban
scrapy genspider top250 movie.douban.com/top250
```

创建好的项目结构如下

<img src="https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255187.png" alt="img" style="zoom: 80%;" />

打开Top250Spider.py可以看到蜘蛛文件如下：

```python
class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        pass
```

##### 爬取数据

根据上面的分析，我们很容易写出爬取主体数据的代码：

```python
# -*- coding: utf-8 -*-
import scrapy


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        items = response.xpath('//div[@class="item"]')
        for item in items:
            title = item.xpath('.//span[@class="title"]/text()').extract_first()
            detail_page_url = item.xpath('./div[@class="pic"]/a/@href').extract_first()
            star = item.xpath('.//span[@class="rating_num"]/text()').extract_first()
            pic_url = item.xpath('./div[@class="pic"]/a/img/@src').extract_first()
```

我们分析了，页面中存在“下一页”按钮，逻辑是：当“下一页”按钮不存在时，停止爬取，若存在，继续解析：

```python

# -*- coding: utf-8 -*-
import scrapy


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        doubanItem = DoubanItem()
        items = response.xpath('//div[@class="item"]')
        for item in items:
            title = item.xpath('.//span[@class="title"]/text()').extract_first()
            detail_page_url = item.xpath('./div[@class="pic"]/a/@href').extract_first()
            star = item.xpath('.//span[@class="rating_num"]/text()').extract_first()
            pic_url = item.xpath('./div[@class="pic"]/a/img/@src').extract_first()

        next = response.xpath('//div[@class="paginator"]//span[@class="next"]/a/@href').extract_first()
        if next is not None:
            next = response.urljoin(next)
            yield scrapy.Request(next, callback=self.parse)
```

##### 提取到Items

爬虫主体创建好了，我们需要将其有效信息提取到Item，编写items.py文件如下：

```python
# -*- coding: utf-8 -*-
import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    detail_page_url = scrapy.Field()
    star = scrapy.Field()
    pic_url = scrapy.Field()
```

修改蜘蛛文件Top250Spider.py：

```python
# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        doubanItem = DoubanItem()
        items = response.xpath('//div[@class="item"]')
        for item in items:
            title = item.xpath('.//span[@class="title"]/text()').extract_first()
            detail_page_url = item.xpath('./div[@class="pic"]/a/@href').extract_first()
            star = item.xpath('.//span[@class="rating_num"]/text()').extract_first()
            pic_url = item.xpath('./div[@class="pic"]/a/img/@src').extract_first()
            #使用数据结构
            doubanItem['title'] = title
            doubanItem['detail_page_url'] = detail_page_url
            doubanItem['star'] = star
            doubanItem['pic_url'] = pic_url
            yield doubanItem

        next = response.xpath('//div[@class="paginator"]//span[@class="next"]/a/@href').extract_first()
        if next is not None:
            # 将爬虫原始url与value拼接
            next = response.urljoin(next)
            yield scrapy.Request(next, callback=self.parse)
```

#### **保存为文本文件**

##### 编写Pipline ––保存数据

+ 在settings文件中开启数据管道

使用csv进行表格存取，创建的管道如下：

```python
# -*- coding: utf-8 -*-
import csv


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
```

使用txt进行表格存取，创建的管道如下：

```python
# -*- coding: utf-8 -*-
import codecs


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
```

**在settings.py中加入这个管道：**

```python
...

ITEM_PIPELINES = {
   'douban.pipelines.DoubanPipeline': 300,
}
```

##### 启动爬虫

当然，直接这样爬取会报403，因为豆瓣网禁止了爬虫行为，我们需要在settings.py中配置用户代理，并禁止访问robots.txt文件：

```python
...

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
```

ok，开始爬取，执行：

```python
scrapy crawl top250
```

爬取结果如下：

csv格式

![image-20231107204322827](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255188.png)

txt格式

![image-20231107210724832](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255190.png)

#### **保存为MySQL文件**

首先在MySQL的test数据库中创建数据表：

```python
CREATE TABLE `douban_videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `detail_page_url` varchar(255) DEFAULT NULL,
  `star` varchar(255) DEFAULT NULL,
  `pic_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

##### 编写Pipline ––保存文件

+ 在settings文件中开启数据管道

**settings.py编写**

```python
MYSQL_DB_NAME = 'spiderTest'  # 数据库名
MySQL_HOST = 'localhost'  # 数据库地址
MYSQL_PORT = 3306  # 数据库端口
MYSQL_USER = 'root'  # 数据库用户名
MYSQL_PASSWORD = '741106'  # 数据库密码
MYSQL_CHARSET = 'utf8'  # 编码方式
```

**Pipline编写**

```python
# -*- coding: utf-8 -*-
import pymysql.cursors


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
```

##### 启动爬虫

ok，执行爬虫程序，可以看到豆瓣电影top250的信息都已经存储到数据库了

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255191.png)

#### **保存为MongoDB文件**

+ 在settings文件中开启数据管道

##### 编写Pipline ––保存文件

```python

# -*- coding: utf-8 -*-
from pymongo import MongoClient


class DoubanMongodbPipeline(object):
    def __init__(self, databaseIp='127.0.0.1', databasePort=27017, mongodbName='test'):
        client = MongoClient(databaseIp, databasePort)
        self.db = client[mongodbName]
        # 我的MongoDB无密码，如果有密码可以使用以下代码认证
        # self.db.authenticate(user, password)

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.db.scrapy.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写

```

##### 启动爬虫

k，执行爬虫程序，可以看到豆瓣电影top250的信息都已经存储到数据库了

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255192.png)



# Twisted框架(了解)

自行百度

详细源码分析：https://me.csdn.net/u012592285

大概理解：https://blog.csdn.net/dongfei2033/article/details/77151698

socket通讯原理：https://www.cnblogs.com/wangcq/p/3520400.html

读懂异步：http://blog.sina.com.cn/s/blog_704b6af70100q52t.html

# **Gevent 异步爬虫**

## 猴子补丁

使用猴子补丁可以实现协作式运行

```python 
from gevent import monkey
monkey.patch_all()
```

**导入模块**

```python 
import gevent
import requests
import time
from fake_useragent import UserAgent
from gevent.queue import Queue
```

## **创建Queue对象**

创建队列对象，可以向队列添加参数

```
work = Queue()
```

## **待爬取链接组**

```python 
url_list =[
	'https://www.baidu.com',
	'https://www.sina.com.cn',
	'http://www.sohu.com',
	'https://www.qq.com',
	'https://www.163.com',
	'http://www.iqiyi.com',
	'https://www.tmall.com',
	'http://www.ifeng.com'
]
```

## **定义爬虫函数**

```python 
def crawler():
	while not work.empty():
	url = work.get_nowait()
	headers = {'User-Agent': UserAgent().random}
	response = requests.get(url, headers=headers)
	print(url, response.status_code, work.qsize())
```

## 队列对象添加任务

```
for url in url_list:
	work.put_nowait(url)
```

## **创建多个协程任务**

```python 
start = time.time()
task_list = []
for i in range(5):
	task = gevent.spawn(crawler)
	task_list.append(task)
	gevent.joinall(task_list)
end = time.time()
print(f'timeout:{end - start}')
```

## **对比同步式爬虫**

```python
start = time.time()
for url in url_list:
	headers = {'User-Agent': UserAgent().random}
	response = requests.get(url, headers=headers)
	print(url, response.status_code)
end = time.time()
print(f'timeout:{end - start}')
```

## **案例**

 **食物热量统计**

```python 
from gevent import monkey
monkey.patch_all()

import csv
import gevent
import requests
from fake_useragent import UserAgent
from lxml import etree
from gevent.queue import Queue

work = Queue()


def crawler():
    while not work.empty():
        url = work.get_nowait()
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(url, headers=headers).text
        html = etree.HTML(response)
        food_list = html.xpath('//div[@class="text-box pull-left"]')
        for food in food_list:
            name = food.xpath('./h4/a/text()')[0]
            heat = food.xpath('./p/text()')[0][3:]
            link = 'https://www.boohee.com' + food.xpath('./h4/a/@href')[0]
            print(name, heat, link)

            writer.writerow([name, heat, link])


def start_tasks():
    url_list = []
    for group in range(1, 11):
        for page in range(1, 11):
            url = f'https://www.boohee.com/food/group/{group}?page={page}'
            url_list.append(url)

    for page in range(1, 11):
        url = f'https://www.boohee.com/food/view_menu?page={page}'
        url_list.append(url)

    for url in url_list:
        work.put_nowait(url)

    task_list = []
    for i in range(20):
        task = gevent.spawn(crawler)
        task_list.append(task)
    gevent.joinall(task_list)
    file.close()


if __name__ == "__main__":
    file = open('食物热量统计.csv', mode='w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['食物', '热量', '链接'])
    
    start_tasks()
```







# 使用selenium爬百度文库ppt

百度文库共享文档要下载券下载真的是烦死人，但是一个个图片点击保存又太麻烦。所以就只能有劳python爬虫大人出马了。不过鉴于我技术不过关，写出的爬虫等级比较低下.

下面介绍下我在写这个简单爬虫的过程.

概览：

图片ppt合成pdf分析网页必要编码步骤编写过程

这里的例子是爬高数答案ppt

网址：https://wenku.baidu.com/view/78deda6ac381e53a580216fc700abb68a882ad56.html?from=search 

## 1.分析网页

首先我们用谷歌打开这个网址，它是这个样子：

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255193.png)

我们的目标是把图片下载下来，那我们怎么找到它们？ 一般图片都是在其他网址z下载过了的

因此很简单，只需要找到存放图片信息的位置

**按F12，谷歌会弹出开发者界面，在这里我们可以找到图片的位置  右边的界面就是开发者界面

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255194.png)

**鼠标先点击下图的方框来

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255195.png)

然后鼠标点击你想下载的图片来定位图片

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255196.png)

定位到了之后，在右边蓝色的区域，我们发现有<div class...>这类东西，其实这是标签，有了它浏览器就知道怎么帮图片啊，文字啊，视频啊，链接等其他东西布局.写推文用的模板其实可以理解为不同方式的布局吧.有尖括号括起来的里面存放着"名字"，尖括号里面或者可能外面存放着信息.通过名字就可以找到想要的信息.

在这里可以找到url(网址)，括号开始到结束

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255197.png)



复制出来看看：

```
https://wkbjbos.bdimg.com/v1/docconvert3421/wk/6da8c8181da456d0bdb9fcb21b9e84e3/0.png?responseContentType=image%2Fpng&responseCacheControl=max-age%3D3888000&responseExpires=Tue%2C%2001%20Jan%202019%2014%3A43%3A32%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2018-11-17T06%3A43%3A32Z%2F3600%2Fhost%2F93c7d46568530e17fe73e33d09c83f9f89ba973978173197eef1e3ae65617730&x-bce-range=0-164464&token=1a05d8fc7c319f190be39020fd5e1c744040f9c18a3e93dbacca0ca5fc95524f&expire=2018-11-17T07:43:32Z](https://wkbjbos.bdimg.com/v1/docconvert3421/wk/6da8c8181da456d0bdb9fcb21b9e84e3/0.png?responseContentType=image%2Fpng&responseCacheControl=max-age%3D3888000&responseExpires=Tue%2C 01 Jan 2019 14%3A43%3A32 %2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2018-11-17T06%3A43%3A32Z%2F3600%2Fhost%2F93c7d46568530e17fe73e33d09c83f9f89ba973978173197eef1e3ae65617730&x-bce-range=0-164464&token=1a05d8fc7c319f190be39020fd5e1c744040f9c18a3e93dbacca0ca5fc95524f&expire=2018-11-17T07:43:32Z)
```

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255198.png)

我们想要的信息是<div class=...>后面的名字reader-pic-item，还有信息:url

然而这只是一张，我们想要所有的

其实我们一般信息存放的规则是一样的.

点击倒三角符号往上找

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255199.png)

 可以发现图片信息都放在这一块里面

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255200.png)

所以我们再记录包含这一块的<div class=....>（叫做节点) 的id   reader-container xreaderd   (有id就选id，因为它是唯一的)

先找到它再找到所有存放图片的节点,

这样第一步大概就结束了,其实还没

我们发现整个网页就显示了三张图片，所以要点一下按钮

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255201.png)

为了让爬虫帮我们点，我们要找到存放它的节点，步骤同上，结果

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255202.png)

很可惜没找到id，所以就勉强用class名字了  banner-more-btn

所以，分析网页的目的是写定位节点规则,和匹配信息的模板

## 2.编码

直接在代码中解释，没有注释的地方可以当作模板，直接跳过

结果：

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255203.png)

## 3.把图片合成pdf

全部选择：

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255204.png)