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
response = requests.post(url=url,  data=data, headers=headers).json()
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

### 为什么要进行 URL 编码？

在 URL 地址中，不允许出现非 ASCII 字符，如果 URL 地址中需要包含中文字符，就必须对中文字符进行**编码**（转义）。

在 URL 参数字符串中用 key=value 这种键值对的形式进行传递参数，多个键值对中间用 & 连接。如果在 value 中也存在 & 这个符号的话，不对其进行编码，就会引起**歧义**

### pyhon中url 编码和解码

```python 
from urllib import parse

# %E7%BE%8E%E5%A5%B3  不是乱码---> url编码
# url解码
res=parse.unquote('%E7%BE%8E%E5%A5%B3')
print(res)

# url编码
res=parse.quote('刷币')  # %E5%88%B7%E5%B8%81
print(res)
```

###  js中URL 编码

####  escape()（已废弃）

escape() 是对**字符串**进行编码，不适用于 URI，其中 @*_±./ 被排除在外，不会被编码。

```javascript
console.log(escape("qaqa666"));  // qaqa666
console.log(escape("你好"));  // %u4F60%u597D
console.log(escape("&&%%"));  // %26%26%25%25
console.log(escape("@*_+-./"));  // @*_+-./
1234
```

> 注意：escape() 已经从 Web 标准中删除，这里只是作为了解，虽然现在它还在，但是说不定哪天它就没了。
>
> 我们进行 URI 编码还是要使用下面两种函数。

#### encodeURI() 和 encodeURIComponent()

**相同点**：都是对 URI 进行编码。

**不同点**：encodeURI 通常用于转码整个 URI，而 encodeURIComponent 主要是用来转码 URI 的组成部分（？后面的参数部分）。

#####  encodeURI()

encodeURI 会替换除`;` `,` `/` `?` `:` `@` `&` `=` `+` `$` `-` `_` `.` `!` `~` `*` `'` `(` `)` `#`的所有的字符，如下示例：

```javascript
// encodeURI() 编码
// 不编码
console.log(encodeURI(";,/?:@&=+$-_.!~*'()#"));
// 输出：;,/?:@&=+$-_.!~*'()#

console.log(encodeURI("https://hanyu.baidu.com/?id=1&name=六十六"));
// 输出：https://hanyu.baidu.com/?id=1&name=%E5%85%AD%E5%8D%81%E5%85%AD
// 六十六 被编码为了 %E5%85%AD%E5%8D%81%E5%85%AD
```

> 注意：encodeURI 自身无法产生能适用于 HTTP GET 或 POST 请求的URI，例如对于 XMLHTTPRequests，因为 “&”, “+”, 和 “=” 不会被编码，然而在 GET 和 POST 请求中它们是特殊字符。encodeURIComponent 这个方法会对这些字符编码。

##### encodeURIComponent()

encodeURIComponent 会替换除`A-Z` `a-z` `0-9` `-` `_` `.` `!` `~` `*` `'` `(` `)`的所有的字符，如下示例：

```javascript
//encodeURIComponent 编码
// 不编码
console.log(encodeURIComponent("A-Za-z0-9-_.!~*'()"));
// 输出：A-Za-z0-9-_.!~*'()

// 错误用法，不能直接将整个 URI 进行编码
console.log(encodeURIComponent("https://hanyu.baidu.com/?name=六十六"));
// 输出：https%3A%2F%2Fhanyu.baidu.com%2F%3Fname%3D%E5%85%AD%E5%8D%81%E5%85%AD
// 可以看到 ：/ 都被编码了

// 正确用法，只对单个参数进行编码
console.log("https://hanyu.baidu.com/?name=" + encodeURIComponent("六十六"));
// 输出：https://hanyu.baidu.com/?name=%E5%85%AD%E5%8D%81%E5%85%AD
12345678910111213
```

为了避免服务器收到不可预知的请求，对任何用户输入的作为 URI 部分的内容都需要用 encodeURIComponent 进行转义，示例如下：

```javascript
// "https://hanyu.baidu.com/?type=a&name=你好"
// 对于上面这串字符串，key 为 type，而 value 为 a&name=你好，如果我们不用 encodeURIComponent 编码，那么将会出现如下结果
console.log(encodeURI("https://hanyu.baidu.com/?type=a&name=你好"));
// 输出：https://hanyu.baidu.com/?type=a&name=%E4%BD%A0%E5%A5%BD
// 如果服务器端收到数据，这将会变为两个参数，就会引发歧义，所以需要用 encodeURIComponent 进行编码
console.log("https://hanyu.baidu.com/?type=" + encodeURIComponent("a&name=你好"));
// 输出：https://hanyu.baidu.com/?type=a%26name%3D%E4%BD%A0%E5%A5%BD
// 通过对比可以看到 & 被编码为了 %26，这样就能有效解决歧义
12345678
```

###  js中URL 解码

#### unescape()（已废弃）

unescape() 就是将被编码过的字符串重新计算生成，与上文所述的 escape() 对应，这也是已经废弃的函数。

```javascript
console.log(unescape("qaqa666"));  // qaqa666
console.log(unescape("%u4F60%u597D"));  // 你好
console.log(unescape("%26%26%25%25"));  // &&%
console.log(unescape("@*_+-./"));  // @*_+-./
1234
```

#### decodeURI()

decodeURI 就是将被 encodeURI 编码过的 URI 解码为未编码版本的新字符串。

> 注意：decodeURI 不能解码那些不会被 encodeURI 编码的内容（例如 "`&` `=` `+` `$` `#`"）。

```javascript
// decodeURI 解码
// 不解码
console.log(decodeURI("&=+$#"));
// 输出：&=+$#

console.log(decodeURI("https://hanyu.baidu.com/?id=1&name=%E5%85%AD%E5%8D%81%E5%85%AD"));
// 输出：https://hanyu.baidu.com/?id=1&name=六十六
// %E5%85%AD%E5%8D%81%E5%85%AD 被解码为了 六十六
12345678
```

#### decodeURIComponent()

decodeURIComponent() 就是将被 encodeURIComponent() 编码过的**部分** URI 解码为一个统一资源标识符（URI）字符串，处理前的 URI 经过了给定格式的编码。

> 同样，decodeURIComponent 也不能解码那些不会被 encodeURIComponent 编码的内容。

```javascript
// decodeURIComponent 解码
// 不解码
console.log(decodeURIComponent("A-Za-z0-9-_.!~*'()"));
// 输出：A-Za-z0-9-_.!~*'()

console.log("https://hanyu.baidu.com/?type=" + decodeURIComponent("a%26name%3D%E4%BD%A0%E5%A5%BD"));
// 输出：https://hanyu.baidu.com/?type=a&name=你好
```







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

#### **[@] 属性定位**

通用写法：tag[@attrname= "attrvalue"]

如： //div 就表示直接定位到的div（有多少返回多少）

**根据class定位**

```python
content = html.xpath('//input[@class="bg s_btn"]')
print(content)

# 使用 XPath 定位所有 class="pic" 或 class="loading" 的元素
pic_elements = driver.find_elements_by_xpath("//div[contains(@class, 'pic') or contains(@class, 'loading')]")
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

# 数据保存

对于文本类型的response，`Content-Type`通常是`text/html`。

对于json类型的response，`Content-Type`通常是`application/json`。

+ 图片 用content -----> 对应 "wb",不用写编码格式
+ 文本 用text  --------> 对应 "w", 用编码格式 encoding="utf-8"
+ json 用json() --------> 对应相应的数据类型(text还是content) . 不用with .. as..

储存路径写法:     "基本路径/ 部分名字 " +  可变名字 比如: 

```python
with open(r'C:\pythonProject\爬虫复习\模板\模板之家 ' + name, "wb") as fp:
	fp.write(a)
	print("完成",name)
```

## **csv表格存储数据**

### csv的介绍

+ CSV，全称为 Comma-Separated Values，中文可以叫作逗号分隔值或字符分隔值，其文件以纯文本形式存储表格数据

+ 该文件是一个字符序列，可以由任意数目的记录组成，记录间以某种换行符分隔。每条记录由字段组成，字段间的分隔符是其他字符或字符串，最常见的是逗号或制表符

+ 不过所有记录都有完全相同的字段序列，相当于一个结构化表的纯文本形式。它比 Excel 文件更加简洁，XLS 文本是电子表格，它包含了文本、数值、公式和格式等内容，而 CSV 中不包含这些内容，就是特定字符分隔的纯文本，结构简单清晰。所以，有时候用 CSV 来保存数据是比较方便的

### csv的使用

| 函数       | 说明                                |
| ---------- | ----------------------------------- |
| reader     | 用于读取CSV文件中的数据，返回迭代器 |
| DictReader | 以键值对形式读取CSV文件中的数据     |
| writer     | 用于写入CSV文件中的数据             |
| DictWriter | 以键值对形式写入CSV文件中的数据     |

**csv数据准备**

```
user_name,gender,money,birthday,address
邵敏,男,11989.79,2004-05-04 11:17:42,海南省 三亚市 -
孟艳,男,5939.52,1993-09-30 05:01:42,宁夏回族自治区 吴忠市 盐池县
孟秀英,女,5035.06,1971-12-09 02:15:25,四川省 阿坝藏族羌族自治州 其它区
胡娜,男,9201.28,2007-03-28 10:42:27,青海省 海西蒙古族藏族自治州 天峻县
孔艳,女,10042.75,2019-11-08 18:48:26,甘肃省 甘南藏族自治州 卓尼县
锺军,女,11410.27,1987-01-20 02:30:12,青海省 西宁市 湟中县
孟丽,女,4352.68,2022-12-21 07:31:06,吉林省 吉林市 丰满区
万秀兰,女,13328.74,1997-11-18 10:05:50,浙江省 绍兴市 绍兴县
陈勇,女,9128.15,2010-12-09 08:59:52,上海 上海市 金山区
熊娜,女,11702.69,1995-09-18 17:33:06,广东省 茂名市 电白县
刘杰,男,10277.58,2021-07-02 11:27:41,四川省 泸州市 古蔺县
毛秀英,男,3781.16,2015-10-07 13:23:21,浙江省 温州市 文成县
李强,男,7010.92,1992-06-10 13:34:43,河北省 秦皇岛市 山海关区
常秀兰,男,15778.79,2006-11-20 00:10:35,内蒙古自治区 兴安盟 扎赉特旗
何芳,女,19429.38,2018-05-01 00:25:15,宁夏回族自治区 固原市 彭阳县
胡霞,男,18284.23,2000-10-23 14:08:15,宁夏回族自治区 银川市 兴庆区
龚娜,男,6578.04,2020-12-18 05:32:12,北京 北京市 丰台区
廖秀兰,女,19719.13,2007-08-17 14:26:06,山东省 临沂市 郯城县
陈静,女,1523.39,1984-11-28 15:47:00,黑龙江省 牡丹江市 阳明区
康磊,女,3141.22,1979-01-27 20:53:00,四川省 巴中市 通江县
```

####   reader

+ 用于读取CSV文件中的数据，返回迭代器

```python
import csv

with open('data.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for item in reader:
    	print(item)
```

![image-20231110081056000](Python%E7%88%AC%E8%99%AB.assets/image-20231110081056000.png)

#### DictReader

+ 以键值对形式读取CSV文件中的数据

```python
with open('data.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    print(headers)
    for item in reader:
        print(item)
```

![image-20231110080914759](Python%E7%88%AC%E8%99%AB.assets/image-20231110080914759.png)

#### writer

+ 用于写入CSV文件中的数据
+ 默认情况下保存的CSV数据会间隔一行，设置 newline='' 取消空行
+ 使用 writer.writerow 方法 以列表形式写入一行数据
+ 使用 writer.writerows 方法 以二维列表形式写入多行数据

```python
with open('user_data.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'gender', 'age'])
    writer.writerow(['001', '阿洁', '男', 20])
    writer.writerow(['002', '阿柒', '男', 21])
    writer.writerow(['003', '阿通', '女', 19])
    writer.writerow(['004', '阿典', '男', 30])
    
    writer.writerows([['005', '阿晴', '女', 25], ['006', '阿雅', '女', 28]])
```

#### DictWriter

+ 以键值对形式写入CSV文件中的数据

+ 使用 DictWriter.writerow(fn,fieldnames) 方法 以键值对形式写入一行数据

+ 使用 DictWriter.writerows(fn,fieldnames) 方法 以列表嵌套键值对形式写入多行数据

+ 使用 writer.writeheader 方法 以键值对形式写入表头

```python
with open('user_data2.csv', mode='w', newline='', encoding='utf-8') as f:
    headers = {'id', 'name', 'gender', 'age'}
    writer = csv.DictWriter(f, headers)
    writer.writeheader() #表头 
    writer.writerow({'id': '001', 'name': '阿洁', 'gender': '男', 'age': 20})
    writer.writerow({'id': '002', 'name': '阿柒', 'gender': '男', 'age': 21})
    writer.writerow({'id': '003', 'name': '阿通', 'gender': '女', 'age': 19})
    writer.writerow({'id': '004', 'name': '阿典', 'gender': '男', 'age': 30})
    
    data = [{'id': '005', 'name': '阿晴', 'gender': '女', 'age': 25},
            {'id': '006', 'name': '阿雅', 'gender': '女', 'age': 28}]
    writer.writerows(data)
```

###  **csv案例**

 获取4399游戏中"最新好玩小游戏列表"

**目标地址：**[4399小游戏](https://www.4399.com/)

```python
import requests
import csv
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
}
url = "https://www.4399.com"
response = requests.get(url, headers=headers)
response.encoding = 'gbk'

print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('.tm_fun.h_3 ul a')
items = []
for item in data:
    href = item.get('href')
    item_info = {
        'title': item.get_text(),
        'img': 'https:' + item.select_one('img').get('lz_src'),
        'href': url + href if href.startswith('/') else href
    }
    items.append(item_info)
    print(item_info)

with open('games.csv', mode='a', newline='', encoding='utf-8') as f:
    fieldnames = {'title', 'img', 'href'}
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(items)
```

获取B站视频标题、作者、播放量、喜欢、壁纸
目标网址：https://www.bilibili.com/

```python
import requests
import csv
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
}
url = "https://www.4399.com"
response = requests.get(url, headers=headers)
response.encoding = 'gbk'

print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('.tm_fun.h_3 ul a')
items = []
for item in data:
    href = item.get('href')
    item_info = {
        'title': item.get_text(),
        'img': 'https:' + item.select_one('img').get('lz_src'),
        'href': url + href if href.startswith('/') else href
    }
    items.append(item_info)
    print(item_info)

with open('games.csv', mode='a', newline='', encoding='utf-8') as f:
    fieldnames = {'title', 'img', 'href'}
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(items)
```

## **MySQL存储数据**

### **MySQL的介绍**

多个表组成一个数据库，也就是关系型数据库

关系型数据库有多种，如 SQLite、MySQL、Oracle、SQL Server、DB2 等

### **MySQL的使用**

```python
import pymysql
import requests


class Spider:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123123',
            db='spider'
        )
        # 获取游标对象
        self.cursor = self.db.cursor()
        # 定义网页信息
        self.url = 'https://baidu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }

    def create_table(self):
        # 创建数据表
        sql = """CREATE TABLE name(
            id INT PRIMARY KEY AUTO_INCREMENT NOT NULL ,
            name VARCHAR(255) NOT NULL,
            age DECIMAL(5,2) DEFAULT 0,
            gender ENUM('man','woman'),
            class INT NOT NULL 
        )"""
        # 异常处理
        try:
            self.cursor.execute(sql)
            print('CREATE SUCCESS')
        except Exception as e:
            print('CREATE FAILED,CASE:', e)

    def get_data(self):
        # 获取网页数据
        response = requests.get(url=self.url, headers=self.headers)
        return response.text

    def parse_data(self, response):
        # 解析响应数据
        # ...
        name = '获取的姓名'
        age = '获取的年龄'
        gender = '获取的性别'
        _class = '获取的班级'
        self.save_data(name, age, gender, _class)

    def save_data(self, name, age, gender, _class):
        # 数据库插入数据
        sql = 'INSERT INTO name(id,name,age,gender,class) values(%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, args=(0, name, age, gender, _class))
            self.db.commit()  # 提交
            print('INSERT SUCCESS')
        except Exception as e:
            self.db.rollback()  # 回滚
            print('CREATE FAILED,CASE:', e)

    def run(self):
        self.create_table()
        response = self.get_data()
        self.parse_data(response)
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
```

### MySQL案例

获取百度招聘Python岗位信息

目标地址：[百度招聘](https://talent.baidu.com/external/baidu/index.html)

+ 获取名称、工作条件、工作内容、工作地点

```python
import requests
            'Cookie': 'BIDUPSID=6DAE2BE6DE41A36518E0802F1B820BAA; PSTM=1672477071; BAIDUID=6DAE2BE6DE41A365056D0C9618163E37:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=6DAE2BE6DE41A365056D0C9618163E37:FG=1; Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1672559377,1672559564; RT="z=1&dm=baidu.com&si=7w2nasej03r&ss=lcd2o1kb&sl=5&tt=342&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=1672559581',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }

    def create_table(self):
        """创建数据表"""
        sql = """CREATE TABLE IF NOT EXISTS baidu(
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                serviceCondition TEXT NOT NULL,
                workContent TEXT NOT NULL,
                workPlace VARCHAR(255) NOT NULL                          
        )"""
        try:
            self.cursor.execute(sql)
            print('CREATE TABLE SUCCESS')
        except Exception as e:
            print('CREATE TABLE FAILED,CASE:', e)

    def get_data(self, keyword, page):
        """获取网页数据"""
        data = {
            'recruitType': 'SOCIAL',
            'pageSize': '10',
            'keyWord': keyword,
            'curPage': page,
            'projectType': '',
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        # print(response.json())
        return response.json()

    def parse_data(self, response):
        """解析响应数据"""
        data = response['data']['list']
        for item in data:
            name = item.get('name', '无')
            serviceCondition = item.get('serviceCondition', '无')
            workContent = item.get('workContent', '无')
            workPlace = item.get('workPlace', '无')
            # print(name, serviceCondition, workContent, workPlace)
            # 数据库插入数据
            self.save_data(name, serviceCondition, workContent, workPlace)

    def save_data(self, name, serviceCondition, workContent, workPlace):
        """数据库插入数据"""
        sql = 'INSERT INTO baidu(id,name,serviceCondition,workContent,workPlace) VALUES(%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, (0, name, serviceCondition, workContent, workPlace))
            self.db.commit()  # 提交
            print('INSERT SUCCESS')
except Exception as e:
        self.db.rollback()  # 回滚
        print('INSERT FAILED,CASE:', e)

        def run(self):
        keyword = input('请输入招聘岗位：')
        page = int(input('请输入页数：'))
        self.create_table()
        for page in range(1, page + 1):
        response = self.get_data(keyword, page)
        self.parse_data(response)
        self.cursor.close()
        self.db.close()


        if __name__ == '__main__':
        baidu = Baidu()
        baidu.run()
```

获取腾讯视频电视剧一栏里的电视剧信息

目标网址：[腾讯视频 - 中国领先的在线视频媒体平台,海量高清视频在线观看](https://v.qq.com/channel/tv?channel=tv&feature=7&iarea=814&listpage=1)

+ 提取名称、集数、描述，获取20个页面

```python
import pymysql

class Spider:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123123',
            db='spider'
        )
        # 获取游标对象
        self.cursor = self.db.cursor()
        # 定义网页信息
        self.url = 'https://pbaccess.video.qq.com/com.tencent.qqlive.protocol.pb.VLPageService/getVLPage?video_appid=3000010'
        self.headers = {
            'cookie': 'RK=yvN8hrwEHy; ptcz=4749f7ca08e70dc65bed32bd2c7448af9eb38c99f032a6974725b335bb55c25b; pgv_pvid=5165889288; _clck=3866836399|1|f7e|0; pac_uid=0_b686f84f0328f; eas_sid=B126z7P1Q701w4I6Y6H8M6s4h6; video_platform=2; tvfe_boss_uuid=9d8908044291084c; video_platform=2; video_guid=6699dba602dade94; pgv_info=ssid=s2191640720',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }

    def create_table(self):
        # 创建数据表
        sql = """CREATE TABLE tencent_video(
            id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            title VARCHAR(255) NOT NULL,
            second_title VARCHAR(255) NOT NULL,
            timelong VARCHAR(255) NOT NULL
        )"""
        # 异常处理
        try:
            self.cursor.execute(sql)
            print('CREATE SUCCESS')
        except Exception as e:
            print('CREATE FAILED,CASE:', e)

    def get_data(self, page):
        # 获取网页数据
        data = {"page_context": {"page_index": page},
                "page_params": {"page_id": "channel_list_second_page", "page_type": "operation", "channel_id": "100113",
                                "filter_params": "feature=-1&iarea=-1&year=-1&pay=-1&sort=75", "page": page}}
        response = requests.get(url=self.url, headers=self.headers, json=data)
        return response.json()

    def parse_data(self, response, page):
        # 解析响应数据
        try:
            data = response["CardList"][1]["children_list"]["list"]["cards"]
        except:
            data = response["CardList"][0]["children_list"]["list"]["cards"]
        for item in data:
            title = item.get('params').get('title', '无')
            second_title = item.get('params').get('second_title', '无')
            timelong = item.get('params').get('timelong', '无')
            print(title,second_title,timelong)
            self.save_data(title, second_title, timelong)

    def save_data(self, title, second_title, timelong):
        # 数据库插入数据
        sql = 'INSERT INTO tencent_video(id,title,second_title,timelong) values(%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, args=(0, title, second_title, timelong))
            self.db.commit()  # 提交
            print('INSERT SUCCESS')
        except Exception as e:
            self.db.rollback()  # 回滚
            print('CREATE FAILED,CASE:', e)

    def run(self):
        self.create_table()
        page = int(input('请输入页数：'))
        for p in range(page):
            response = self.get_data(p)
            self.parse_data(response, p)
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
```

## **MongoDB存储数据**

### **MongoDB简介**

MongoDB 是由 C++ 语言编写的非关系型数据库，是一个基于分布式文件存储的开源数据库系统，其内容存储形式类似 JSON 对象，它的字段值可以句含其他文档、数组及文档数组，非常灵活。

### **MongoDB封装类**

```python

import pymongo
import requests


class Spider:
    def __init__(self):
        # 连接数据库
        self.client = pymongo.MongoClient(
            host='localhost',
            port=27017
        )
        # 创建数据库集合
        self.collection = self.client['spider']['name']
        self.url = 'https://www.baidu.com'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'

        }

    def get_data(self):
        # 获取网页数据
        response = requests.get(url=self.url, headers=self.headers)
        return response.text

    def parse_data(self, response):
        # 解析响应数据
        # ...
        item_info = {}
        item_info['title'] = '获取的标题'
        item_info['img'] = '获取的图片地址'
        item_info['url'] = '获取的链接地址'
        self.save_data(item_info)

    def save_data(self, info):
        # 插入数据到mongo数据库
        self.collection.insert_one(info)

    def run(self):
        response = self.get_data()
        self.parse_data(response)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
```

### MongoDB案例

获取到爱奇艺视频电视剧信息

目标网址:[内地电视剧大全-好看的内地电视剧排行榜-爱奇艺](https://list.iqiyi.com/www/2/15-------------11-1-1-igiyi--.html?s_source=PCW_SC)

+ 获取标题、链接、描述信息并保存到mongo数据库

```python
import pymongo
import requests
from retrying import retry


class IQiYi:
    def __init__(self):
        self.client = pymongo.MongoClient(
            host='localhost',
            port=27017
        )
        self.collection = self.client['spider']['iqiyi']
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }

    @retry(stop_max_attempt_number=3)
    def get_data(self, params):
        response = requests.get(url=self.url, params=params, headers=self.headers)
        return response.json()

    def parse_data(self, response):
        data = response['data']['list']
        for item in data:
            item_info = {}
            item_info['title'] = item['title']
            item_info['playUrl'] = item['playUrl']
            item_info['description'] = item['description'].replace('\n', '')
            print(item_info)
            self.save_data(item_info)

    def save_data(self, info):
        self.collection.insert_one(info)

    def run(self):
        page = int(input('请输入页数：'))
        for page in range(1, page+1):
            params = {
                'channel_id': '2',
                'data_type': '1',
                'mode': '11',
                'page_id': page,
                'ret_num': '48',
                'session': '63bd9816bc423d33355fcf0333b55637',
                'three_category_id': '15;must',
            }
            response = self.get_data(params)
            self.parse_data(response)


if __name__ == '__main__':
    iqy = IQiYi()
    iqy.run()
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



# Scrapy框架:crossed_swords:

[Scrapy](https://scrapy.org/) 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。

Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

## scrapy架构组成

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

  ```python
  selector.extract()
  ```

+  提取selector列表第一个数据的data属性值

  ```python
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

###  start_requests()

#### **携带cookies请求**

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

####  **post请求**

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



## **middleware下载中间件 — 拦截响应数据**

位置：引擎和下载器之间

作用：批量拦截到整个工程中所有的请求和响应

使用

+ 在settings文件中开启中间件，权重值低的越优先执行
+ 在middlewares文件中定义中间件类

拦截请求：

+ UA伪装：process_request

- 
代理IP:  process_exception:  return request

拦截响应：

- 篡改响应数据，响应对象

**类结构**

![image-20231113160927670](Python%E7%88%AC%E8%99%AB.assets/image-20231113160927670.png)

```python
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
from scrapy import signals


# useful for handling different item types with a single interface

# 爬虫中间件
class SpidertestSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r
    #
    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)


# 下载中间件
class SpidertestDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as
    # if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 拦截请求
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 拦截所有的响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 拦截发生异常的请求对象
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
    #
    # # 打印的是日志(可以注释）
    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)

# 设置随机UA
class RandomUserAgentMiddleware:
    def __init__(self):
        self.user_agent = UserAgent().random

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        print(self.user_agent)

```

### process_request

处理请求

+ request通过下载中间件时，该方法被调用

返回值 None

+ 如果所有下载器中间件都返回None给引擎，则请求最终传给下载器处理，否则继续通过引擎传递给其他权重低的process_reqeust方法

Request对象

+ 如果返回request对象给引擎，则将reqeust对象通过引擎发送给调度器

Response对象

+ 将响应对象交给spider进行解析

### process_response

处理响应数据

+ 下载器完成请求返回响应数据时，该方法被调用

返回值

Request对象

+ 如果返回request对象给引擎，则将reqeust对象通过引擎发送给调度器

Response对象 

+ 将响应对象交给spider进行解析

[scrapy 中间件设置随机UA、随机cookie、以及代理_scrapy ](https://blog.csdn.net/qq_46183423/article/details/128110048)

### 设置随机UA

####  创建中间件类

+ 在middlewares文件定义中间件类

```python
from fake_useragent import UserAgent

# 定义
class RandomUserAgentMiddleware:
    def __init__(self):
        self.user_agent = UserAgent().random

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
```

####  开启中间件

+ 在settings文件中开启中间件(在项目全局启用该中间件)(方式1)

```python
DOWNLOADER_MIDDLEWARES = {
'scrapydownloadertest.middlewares.RandomUserAgentmiddleware': 543
}
```

+ 在spider中启用中间件(方式2)

在spider中是可以覆写setting的，也即sipder中的setting优先级比setting.py优先级要高。
而且，此时的setting是针对单一spider的，不会影响别的spider，可以针对不同的spider进行个性化。
具体实现如下：

```python
# 覆写settings
custom_settings = {
    # 不使用使用cookies
    'COOKIES_ENABLED': 'False',
    # 使用随机UA
    'DOWNLOADER_MIDDLEWARES': {'jkxy.middlewares.RandomUserAgent': 543}
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


免费ip代理:

+ 基本上无法使用，不推荐

#### 代理池

+ 在settings文件配置代理池

```python
PROXIES_POOL = [
{'ip_port': 'http://223.96.90.216:8085'},
{'ip_port': 'http://120.220.220.95:8085'}
]
```

#### 定义中间件类

+ 在middlewares文件定义中间件类
+ 在request的meta中添加proxy属性
+ 含有账号密码的IP需要进行http基本认证
+ 基本认证流程：请求头添加Proxy - Authorization: 'Basic ' + base64编码(user_passwd)
+ 注意：不能漏掉Basic的空格

```python
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

#### 开启下载器中间件

+ 在settings文件开启下载器中间件

```python
DOWNLOADER_MIDDLEWARES = {
'scrapy_proxy.middlewares.ProxyMiddleware': 543,
}
```

### 对接Selenium

#### 定义中间件类

+ 在middlewares文件定义中间件类

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

#### 开启下载器中间件

+ 在settings文件开启下载器中间件

```
DOWNLOADER_MIDDLEWARES = {
'scrapy_selenium.middlewares.SeleniumMiddleware': 543,
}
```

### 随机cookie中间件

.在middlewares.py中设置随机cookie中间件

将获取到的所有cookie存放在一个txt文件中，可一条，可多条

```cobol
# 设置随机cookie
class CookiesMiddleware(object):
    def __init__(self):
        with open('cookie.txt', 'rt', encoding='utf-8') as f:
            COOKIE = f.readlines()
            self.COOKIE_LIST = [d.strip() for d in COOKIE]
 
    def process_request(self, request, spider):
        cookie = random.choice(self.COOKIE_LIST)
        request.headers['Cookie'] = cookie
```

## 日志信息及日志级别

### 日志级别

+ CRITICAL：严重错误
+ ERROR：一般错误
+ WARNING：警告
+ INFO：一般信息
+ DEBUG：调试信息

### 设置日志级别

+ 在settings文件中设置

```
LOG_LEVEL = 'DEBUG'
```

### 保存日志文件

+ 在settings文件中设置

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

####  批量下载图片

继续豆瓣

爬虫的基本结构跟之前的一样：

```python
# -*- coding: utf-8 -*-
import scrapy
from douban_images.items import DoubanImagesItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        doubanItem = DoubanImagesItem()
        items = response.xpath('//div[@class="item"]')
        for item in items:
            name = item.xpath('.//span[@class="title"]/text()').extract_first()
            pic_url = item.xpath('./div[@class="pic"]/a/img/@src').extract_first()
            doubanItem['name'] = name
            doubanItem['pic_url'] = pic_url
            yield doubanItem

        next = response.xpath('//div[@class="paginator"]//span[@class="next"]/a/@href').extract_first()
        if next is not None:
            next = response.urljoin(next)
            yield scrapy.Request(next, callback=self.parse)
```

items.py 也一样：

```python

# -*- coding: utf-8 -*-
import scrapy


class DoubanImagesItem(scrapy.Item):
    name = scrapy.Field()
    pic_url = scrapy.Field()
```

pipelines.py

```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class DoubanImagesPipeline(ImagesPipeline):
	# 获取图片资源
    def get_media_requests(self, item, info):
        name = item['name']
        pic_url = item['pic_url']
        # 请求传过来的图片地址以获取图片资源
        yield Request(pic_url, meta={'name': name})

	# 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        ext = request.url.split('.')[-1]
        name = request.meta['name'].strip()
        filename = 
```

继承了scrapy的：ImagesPipeline这个类，我们需要在里面实现： get_media_requests(self, item, info) 这个方法，这个方法主要是把蜘蛛 yield 过来的图片链接执行下载。

主体代码准备完毕，还需要修改配置文件settings.py：

```python
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

ROBOTSTXT_OBEY = False

# 启动图片下载中间件
ITEM_PIPELINES = {
   'douban_images.pipelines.DoubanImagesPipeline': 300,
}

# 设置图片存储目录
IMAGES_STORE = 'F:/images'
```

scrapy 提供了一个常量：IMAGES_STORE，用于定义存储图片的路径, 可以是绝对路径也可以是相对路径, 相对路径相对于项目根目录。

开启爬虫：scrapy crawl images

爬取完毕，可以看到目标文件夹里已经获取了250张图片：

![img](Python%E7%88%AC%E8%99%AB.assets/1597110918330-d2e3bc9d-1910-412e-a6f6-11bcb8dadcef.png)

#### **登录逻辑处理**

##### 登录逻辑分析

跟网上看到的不太一样，网上基本上都是抓取页面，获取到登录页表单，检测时候有验证码，如果有则下载，没有则直接表单提交登录。而通过我自己对豆瓣登录页的分析，并没有看到页面包括表单元素，豆瓣的登录是通过Ajax提交的。

登录页地址：https://accounts.douban.com/passport/login

使用Ajax登录豆瓣

![img](Python%E7%88%AC%E8%99%AB.assets/1597111877539-91d46092-36e7-4ff9-b621-e383d46a27a3-169984268310112.png)

既然找出了登录接口，那么要使用程序登录也不在话下了，我们先使用postman测试一下

![img](Python%E7%88%AC%E8%99%AB.assets/1597111899308-352db83d-1082-4ad3-8ec6-204cb2732c04-169984272260914.png)

第一次发送请求，服务器返回参数错误，查看了下cookie，发现服务器种了一个cookie：

<img src="Python%E7%88%AC%E8%99%AB.assets/1597111911134-06087fc9-13d4-49bc-96b3-5ec9fe51b9f4-169984273275016.png" alt="img" style="zoom: 67%;" />

再次发送请求，将会携带这个cookie，发现登录成功了：

![img](Python%E7%88%AC%E8%99%AB.assets/1597111929996-a5eec56f-89fd-4afd-8c95-4f9f6b444f7e-169984275304318.png)

ok，到此，登录逻辑已经捋顺了，需要调用登录接口两次：第一次获取cookie，第二次携带cookie访问

登录接口如下：

```
https://accounts.douban.com/j/mobile/login/basic
```

使用POST请求发送，携带以下头部信息：

```
Content-Type: application/x-www-form-urlencoded
Cookie: ...
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68
```

传递以下几个参数：

```
name 用户名
password 密码
remember 是否记住密码
```

##### 登录前后页面分析

我们以豆瓣首页为例：https://www.douban.com/

在登录前访问豆瓣首页，看到页面长这样：

![img](Python%E7%88%AC%E8%99%AB.assets/1597111966336-695c138b-5548-4e8c-8904-8c474a168782-169984285712120.png)

有一个登录框，顶部有一行菜单：“读书”、“电影”等等

在登录后访问豆瓣首页，看到页面长这样：

![img](Python%E7%88%AC%E8%99%AB.assets/1597111974257-7e9eed0a-ac3b-41a4-852f-ad1bc3c1b771-169984285712222.png)





顶部菜单变为了“首页”、“我的豆瓣”等等，没有了输入框

我们点击“我的豆瓣”，可以看到豆瓣个人主页：

![img](Python%E7%88%AC%E8%99%AB.assets/1597111984060-a0da15eb-166b-4a41-8e39-1805212af872-169984285712724.png)

在豆瓣主页中可以看到我们的昵称等信息。

我们退出登录，再次输入个人主页地址：https://www.douban.com/mine/，可以看到会被重定向到登录页面。

好的，所有逻辑都明了了，如果登录，我们跳转到个人主页，看下能不能获取到个人昵称，如果获取得到，说明登录成功了。

##### 具体程序实现

spider程序如下：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 10:46
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : login.py
import json

import scrapy


class LoginSpider(scrapy.Spider):
    # 类变量(静态)
    name = 'login'
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'name': 'your name',
        'password': 'your password',
        'remember': "true"
    }

    # 携带cookies请求和post请求
    def start_requests(self):
        # 第一次登录，由于缺少cookie，会返回登录错误，并设置cookie
        yield scrapy.FormRequest(
            url=self.url,
            formdata=self.data,
            method='POST',
            callback=self.getCookie  # 调用
        )

    def getCookie(self, response):
        # scrapy会自动携带上一个请求设置的cookie
        yield scrapy.FormRequest(
            url=self.url,
            formdata=self.data,
            method='POST',
            callback=self.parse,  # 调用
            # 添加以防止出现：Filtered duplicate request
            dont_filter=True
        )

    def parse(self, response):
        res = json.loads(response.body.decode())
        print("========")
        print(res)
        print("========")
        url = "https://www.douban.com/"
        yield scrapy.Request(url, callback=self.getHomePage)

    def getHomePage(self, response):
        navs = response.xpath("//div[@class='nav-items']//li")
        for nav in navs:
            title = nav.xpath(".//a/text()").extract_first().strip()
            url = nav.xpath(".//a/@href").extract_first()
            print(title.strip())
            print(url)
            if '我的豆瓣' in title:
                yield scrapy.Request(url, callback=self.getMyPage)

    def getMyPage(self, response):
        name = response.xpath("//div[@class='info']//h1/text()").extract_first().strip()
        print("====start: getMyPage====")
        print(name)
        print("====end: getMyPage====")

```

这里值得说明的是，第一次登录成功后，scrapy会保存获取到的cookie，在第二次访问登录接口的时候，会自动携带cookie访问。

第二次调用登录接口的时候，需要在请求中配置参数dont_filter=True，否则，Scrapy会认为此接口已经访问过了，不需要重新访问，返回一个Debug信息：Filtered duplicate request

登录成功后，获取顶部导航栏菜单，访问“我的豆瓣”，查看是否能够获取到昵称。

运行爬虫，看到控制台打印出以下数据（主要是要看到自己的昵称），说明登录成功了：

![img](Python%E7%88%AC%E8%99%AB.assets/1597112182078-767e745b-b490-4da9-a95d-c6e70cc2857e.png)

注意需要在settings.py中进行以下配置：

```python
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
```

## 使用splash抓取动态网页数据

+ 为了加速页面的加载速度，页面的很多部分都是用JS生成的
+ 而对于用scrapy爬虫来说就是一个很大的问题，因为scrapy没有JS engine，所以爬取的都是静态页面
+ 对于JS生成的动态页面直接使用scrapy的Request请求都无法获得，需要使用scrapy-splash

scrapy-splash 加载js数据是基于Splash来实现的，Splash是一个Javascript渲染服务。它是一个实现了HTTP API的轻量级浏览器，Splash是用Python实现的，同时使用Twisted和QT，而我们使用scrapy-splash最终拿到的response相当于是在浏览器全部渲染完成以后，拿到的渲染之后的网页源代码。

#### 通过Dockers安装splash

```python
ocker pull scrapinghub/splash
docker run -p 8050:8050 --name splash scrapinghub/splash
```

浏览器访问 [http://localhsot:8050](http://localhsot:8050/)，看到界面：

![image-20231113105639733](Python%E7%88%AC%E8%99%AB.assets/image-20231113105639733.png)

#### 在Python中的准备工作

安装 scrapy-splash

```
pip install scrapy-splash
```

创建项目：

```
scrapy startproject taobao_splash
cd taobao_splash
scrapy genspider taobao s.taobao.com
```

配置文件 settings.py：

```python

# -*- coding: utf-8 -*-

BOT_NAME = 'taobao_splash'

SPIDER_MODULES = ['taobao_splash.spiders']
NEWSPIDER_MODULE = 'taobao_splash.spiders'

# 渲染服务的url
SPLASH_URL = 'http://localhost:8050'

# 去重过滤器
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapy_splash.SplashCookiesMiddleware': 723,
   'scrapy_splash.SplashMiddleware': 725,
   'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
}

# 使用Splash的Http缓存
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

#### 分析淘宝页面

我们先在Postman中测试一下：

直接访问搜索页面： http://s.taobao.com/search?q=iphone，发现会被重定向到首页，而不是搜索页面，说明需要登录才能进行接下来的操作。

![img](Python%E7%88%AC%E8%99%AB.assets/1597112527136-23944832-124b-467a-9668-5e2a9575ac82.png)

我们到浏览器中找找登录接口：

![img](Python%E7%88%AC%E8%99%AB.assets/1597112546174-b85c539c-1f06-4ed9-a1dc-8cf4e3e218e7.png)

发现是这个接口：https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0

我们在Postman中进行登录：

![img](Python%E7%88%AC%E8%99%AB.assets/1597112567160-338a987f-5223-4cf6-9cc5-5f002fd897b9.png)

再次访问搜索页面，发现能够正常获取：

![img](Python%E7%88%AC%E8%99%AB.assets/1597112585553-920c27fb-ce73-49d5-8cb6-5b6bfedcb211.png)

#### 爬虫编写

```python

# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']

    #二级爬虫
    def start_requests(self):
        loginUrl = "https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0"
        yield scrapy.FormRequest(loginUrl, formdata={
            "loginId": "your phone",
            "password2": "your password(已加密)"
        }, callback=self.parse)

    def parse(self, response):
        print(response.body)
        url = 'https://s.taobao.com/search?q=iphone'
        # 如果直接请求，内容还未来得及渲染就返回了
        # yield scrapy.Request(url, callback=self.getContent)
        # 通过SplashRequest请求，等待解析0.1秒后返回（时间可适当增加以保证页面完全解析渲染完成）
        yield SplashRequest(url, self.getContent, args={'wait': 0.1})

    def getContent(self, response):
        titles = response.xpath('//div[@class="row row-2 title"]/a/text()').extract()
        for title in titles:
            print(title.strip())
```

这个地方使用了SplashRequest，传递了一个参数wait，表示等待splash解析0.1秒后返回解析后的结果，等待时间可以自己适当调整。

如果我们将请求换为普通的 scrapy.Request，则可以看到返回结果为空，说明数据是异步解析加载渲染的。

执行爬虫：

```
scrapy crawl taobao
```

![img](Python%E7%88%AC%E8%99%AB.assets/1597112633338-f51742e5-e3a0-4b9e-8c71-dd4146e65736.png)

## **伪装headers构造假IP**

我们先分析下 https://www.ip138.com/ 这个网站，它可以获取到我们的IP及所在区域：

![img](Python%E7%88%AC%E8%99%AB.assets/1597112790630-ee68597e-4109-470b-ae54-2586ce331729.png)

#### 分析

可知，其嵌套一个iframe，将 [2020.ip138.com](https://www.yuque.com/xiaoyulive/python_crawl/2020.ip138.com) 的内容嵌入。

我们的目的是伪造一个headers，骗过此网站，让其解析伪造的IP。

首先我们编写一个正常的爬虫，返回我们当前的IP：

```python
import scrapy


class IpSpider(scrapy.Spider):
    name = "ip"
    allowed_domains = ["ip138.com"]
    start_urls = ['https://2023.ip138.com/']

    def parse(self, response):
        print("=" * 40)
        print(response.xpath('/html/body/p[1]/a[1]/text()').extract_first())
        print("=" * 40)

```

在未伪造headers的时候，启动爬虫程序，会正常返回我的ip及所在地区

![img](Python%E7%88%AC%E8%99%AB.assets/1597112810257-b0ae8294-15ee-4b97-b50f-8cb72ede4c70.png)

#### 伪造IP

首先我们创建一个工具类，提供要给方法，用于伪造headers信息：

```python
#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import random
from ip138_fake_headers.settings import USER_AGENT_LIST


class Utils(object):

    @staticmethod
    def get_header(host, ip=None):
        if ip is None:
            ip = str(
                '%s.%s.%s.%s' % (
                    random.choice(list(range(255))),
                    random.choice(list(range(255))),
                    random.choice(list(range(255))),
                    random.choice(list(range(255)))
                )
            )
        return {
            'Host': host,
            'User-Agent': random.choice(USER_AGENT_LIST),
            'server-addr': '',
            'remote_user': '',
            'X-Client-IP': ip,
            'X-Remote-IP': ip,
            'X-Remote-Addr': ip,
            'X-Originating-IP': ip,
            'x-forwarded-for': ip,
            'Origin': 'http://' + host,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://" + host + "/",
            'Content-Length': '0',
            "Connection": "keep-alive"
        }
```

这里引入了配置文件，我们需要在settings.py中配置USER_AGENT_LIST：(注意不要设置这个, 去使用下载中间件去设置动态Ua)

```python
USER_AGENT_LIST=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0
]
```

然后配置中间件：

```python
# -*- coding: utf-8 -*-

from ip138_fake_headers.libs.utils import Utils
from scrapy.http.headers import Headers


class Ip138FakeHeadersDownloaderMiddleware(object):

    def process_request(self, request, spider):
        request.headers = Headers(Utils.get_header('2020.ip138.com'))
```

在配置文件中启用中间件：

```python
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
   'ip138_fake_headers.middlewares.Ip138FakeHeadersDownloaderMiddleware': 1,
}
```

启动爬虫程序，可以看到，伪造IP成功：

![img](Python%E7%88%AC%E8%99%AB.assets/1597112828805-bed22806-ff9f-46f4-8a9b-97cca9914e70.png)

## **在爬虫程序中设置代理**

方法一：在meta中设置

我们可以直接在自己具体的爬虫程序中设置proxy字段，直接在构造Request里面加上meta字段即可：

```python
# -*- coding: utf-8 -*-
import scrapy


class Ip138Spider(scrapy.Spider):
    name = 'ip138'
    allowed_domains = ['ip138.com']
    start_urls = ['http://2020.ip138.com']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={'proxy': 'http://163.125.69.29:8888'}, callback=self.parse)

    def parse(self, response):
        print("response text: %s" % response.text)
        print("response headers: %s" % response.headers)
        print("response meta: %s" % response.meta)
        print("request headers: %s" % response.request.headers)
        print("request cookies: %s" % response.request.cookies)
        print("request meta: %s" % response.request.meta)
```

方法二：在中间件中设置

中间件middlewares.py的写法如下：

```python
# -*- coding: utf-8 -*-
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://proxy.your_proxy:8888"
```

这里有两个问题:

●一是proxy一定是要写号http://前缀的否则会出现to_bytes must receive a unicode, str or bytes object, got NoneType的错误。
●二是官方文档中写到process_request方法一定要返回request对象，response对象或None的一种，但是其实写的时候不用return

另外如果代理有用户名密码等就需要在后面再加上一些内容:

```python
# Use the following lines if your proxy requires authentication
proxy_user_pass = "USERNAME:PASSWORD"

# setup basic authentication for the proxy
encoded_user_pass = base64.encodestring(proxy_user_pass)
request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_
```

如果想要配置多个代理，可以在配置文件中添加一个代理列表：

```
PROXIES = [
    '163.125.69.29:8888'
]
```

然后在中间件中引入：

```

# -*- coding: utf-8 -*-
import random
from ip138_proxy.settings import PROXIES

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://%s" % random.choice(PROXIES)
        return None
```

在settings.py的DOWNLOADER_MIDDLEWARES中开启中间件：

```
DOWNLOADER_MIDDLEWARES = {
    'myCrawler.middlewares.ProxyMiddleware': 1,
}
```

运行程序，可以看到设置的代理生效了：

![img](Python%E7%88%AC%E8%99%AB.assets/1597113047749-40c9cd65-43a3-4740-9652-0f02801d7435.png)

如果想要找到一些免费的代理可以到[快代理](https://www.kuaidaili.com/free/)中寻找

## **伪造headers的多种实现**

本文以前面的ip138爬虫为例，爬虫程序不再赘述。

### 方法一：修改配置文件

可以通过修改settings.py配置文件，很容易地为爬虫程序设置头部数据

修改User-Agent：

```
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
```

修改headers：

```python
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    'Content-Length': '0',
    "Connection": "keep-alive"
}
```

### 方法二：在爬虫程序中设置(推荐)

在请求的时候设置：

```python
# -*- coding: utf-8 -*-
import scrapy


class Ip138Spider(scrapy.Spider):
    name = 'ip138'
    allowed_domains = ['www.ip138.com','2018.ip138.com']
    start_urls = ['http://2018.ip138.com/ic.asp']
    
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Content-Length': '0',
        "Connection": "keep-alive"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers ,callback=self.parse)

    def parse(self, response):
        print("*" * 40)
        print("response text: %s" % response.text)
        print("response headers: %s" % response.headers)
        print("response meta: %s" % response.meta)
        print("request headers: %s" % response.request.headers)
        print("request cookies: %s" % response.request.cookies)
        print("request meta: %s" % response.request.meta)
```

除了可以在 settings.py 中设置，我们也可以为爬虫单独设置headers，例如：

```
class Ip138Spider(scrapy.Spider):
	custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            'Content-Length': '0',
            "Connection": "keep-alive"
        }
    }
```

### 方法三：在中间件中设置

我们可以在DownloaderMiddleware中间件中设置headers

```
class TutorialDownloaderMiddleware(object):
    def process_request(self, request, spider):
    	request.headers.setdefault('User-Agent', 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5')
```

当然我们也可以设置完整的headers

```
from scrapy.http.headers import Headers
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    'Content-Length': '0',
    "Connection": "keep-alive"
}
class TutorialDownloaderMiddleware(object):
    def process_request(self, request, spider):
        request.headers = Headers(headers)
```

在settings.py中启动中间件

```
# Enable or disable downloader middlewares

# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.TutorialDownloaderMiddleware': 1,
}
```

### 方法四：使用fake-useragent切换User-Agent(推荐)

middlewares.py

```python
from fake_useragent import UserAgent
class RandomUserAgentMiddleware(object):
    def __init__(self,crawler):
    super(RandomUserAgentMiddleware, self).__init__()
    self.ua = UserAgent()
    self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        def get_ua():
            return getattr(self.ua,self.ua_type)
        request.headers.setdefault('User-Agent',get_ua())
```

在settings.py中启用中间件

```python
RANDOM_UA_TYPE= 'random'

DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.RandomUserAgentMiddleware': 543,
}
```

[scrapy实战：伪造headers的多种实现](https://blog.csdn.net/weixin_43430036/article/details/84851714)

## scrapy 中间件设置随机UA、随机cookie、以及代理

1、在middlewares.py中定义随机[UA](https://so.csdn.net/so/search?q=UA&spm=1001.2101.3001.7020)中间件

```python
import random
 
# 随机请求头
class UserAgentMiddleware(object):
    def __init__(self):
        self.user_agents_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        ]
    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agents_list)
        request.headers['User-Agent'] = user_agent
```

2.在middlewares.py中设置随机cookie中间件

将获取到的所有cookie存放在一个txt文件中，可一条，可多条

```cobol
# 设置随机cookie
class CookiesMiddleware(object):
    def __init__(self):
        with open('cookie.txt', 'rt', encoding='utf-8') as f:
            COOKIE = f.readlines()
            self.COOKIE_LIST = [d.strip() for d in COOKIE]
 
    def process_request(self, request, spider):
        cookie = random.choice(self.COOKIE_LIST)
        request.headers['Cookie'] = cookie
```

3.在middlewares.py中设置代理中间件

```python
class IPProxyMiddleware(object):
 
    @staticmethod
    def fetch_proxy():
        """
        获取一个代理IP
        """
        # You need to rewrite this function if you want to add proxy pool
        # the function should return an ip in the format of "ip:port" like "12.34.1.4:9090"
        return None
 
    def process_request(self, request, spider):
        """
        将代理IP添加到request请求中
        """
        proxy_data = self.fetch_proxy()
        if proxy_data:
            current_proxy = f'http://{proxy_data}'
            spider.logger.debug(f"current proxy:{current_proxy}")
            request.meta['proxy'] = current_proxy
```

4.最后在setting中启动自定义中间件

```cobol
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'middlewares.UserAgentMiddleware': 543,
    'middlewares.CookiesMiddleware': 743,
}
```

5.测试效果

```
在def parse中
print('--------------------------------------', response.request.headers)
```

![img](Python%E7%88%AC%E8%99%AB.assets/9cccce989d81449786305c0a369dfca2.png)

## 使用Selenium模拟用户操作浏览器

selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。

selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。

**准备工作**

安装Selenium：

```
pip install selenium
```

安装chromedriver：到http://chromedriver.storage.googleapis.com/index.html中下载跟自己Chrome版本匹配的驱动。

<img src="Python%E7%88%AC%E8%99%AB.assets/1597113318605-2793c212-33c2-4a83-9ab3-afe661506c49.png" alt="img" style="zoom:67%;" />

<img src="Python%E7%88%AC%E8%99%AB.assets/1597113323323-20e14aca-e1f5-464e-99a4-c64184a6dddd.png" alt="img" style="zoom:67%;" />

**新建爬虫**

```
scrapy startproject zhihu_selenium
cd zhihu_selenium
scrapy genspider zhihu www.zhihu.com
```

**使用selenium模拟用户操作**

先放上完整的爬虫程序：

```
# -*- coding: utf-8 -*-
import scrapy
import json
import time
from selenium import webdriver
from pathlib import Path


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    # 模拟请求的headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72",
        "HOST": "www.zhihu.com"
    }

    # scrapy请求的开始时start_request
    def start_requests(self):
        zhihu_findUrl = 'https://www.zhihu.com/people/edit'
        if not Path('zhihuCookies.json').exists():
            self.loginZhihu()  # 先执行login，保存cookies之后便可以免登录操作

        # 毕竟每次执行都要登录还是挺麻烦的，我们要充分利用cookies的作用
        # 从文件中获取保存的cookies
        with open('zhihuCookies.json', 'r', encoding='utf-8') as f:
            listcookies = json.loads(f.read())  # 获取cookies

        # 把获取的cookies处理成dict类型
        cookies_dict = dict()
        for cookie in listcookies:
            # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
            cookies_dict[cookie['name']] = cookie['value']

        # Scrapy发起其他页面请求时，带上cookies=cookies_dict即可，同时记得带上header值，
        yield scrapy.Request(url=zhihu_findUrl, cookies=cookies_dict, callback=self.parse, headers=self.headers)

    def parse(self, response):
        # 打印出设置页面中登录者的昵称
        print("*" * 40)
        print(response.xpath('//span[@class="FullnameField-name"]/text()').extract_first())
        print("*" * 40)
        # print("response text: %s" % response.text)
        # print("response headers: %s" % response.headers)
        # print("response meta: %s" % response.meta)
        # print("request headers: %s" % response.request.headers)
        # print("request cookies: %s" % response.request.cookies)
        # print("request meta: %s" % response.request.meta)

    # 使用selenium登录知乎并获取登录后的cookies，后续需要登录的操作都可以利用cookies
    @staticmethod
    def loginZhihu():
        # 登录网址
        loginurl = 'https://www.zhihu.com/signin'
        # 加载webdriver驱动，用于获取登录页面标签属性
        driver = webdriver.Chrome('D:/Software/chromedriver.exe')
        # 加载页面
        driver.get(loginurl)

        time.sleep(3)  # 执行休眠3s等待浏览器的加载

        # 方式1 通过填充用户名和密码
        # driver.find_element_by_name('username').clear()  # 获取用户名框
        # driver.find_element_by_name('username').send_keys(u'username')  # 填充用户名
        # driver.find_element_by_name('password').clear()  # 获取密码框
        # driver.find_element_by_name('password').send_keys(u'password')  # 填充密码
        # input("检查网页是否有验证码要输入，有就在网页输入验证码，输入完后，控制台回车；如果无验证码，则直接回车")
        # # 点击登录按钮,有时候知乎会在输入密码后弹出验证码，这一步之后人工校验
        # driver.find_element_by_css_selector("button[class='Button SignFlow-submitButton Button--primary Button--blue']").click()
        #
        # input_no = input("检查网页是否有验证码要输入，有就在网页输入验证码，输入完后，控制台输入1回车；如果无验证码，则直接回车")
        # if int(input_no) == 1:
        #     # 点击登录按钮
        #     driver.find_element_by_css_selector(
        #         "button[class='Button SignFlow-submitButton Button--primary Button--blue']").click()

        # 方式2 直接通过扫描二维码，如果不是要求全自动化，建议用这个，非常直接，毕竟我们这一步只是想保存登录后的cookies，至于用何种方式登录，可以不必过于计较
        driver.find_element_by_css_selector("div[class='SignFlow-qrcodeTab']").click()
        input("请扫描页面二维码，并确认登录后，点击回车：")  # 点击二维码手机扫描登录

        time.sleep(3)  # 同样休眠3s等待登录完成

        input("检查网页是否有完成登录跳转，如果完成则直接回车")

        # 通过上述的方式实现登录后，其实我们的cookies在浏览器中已经有了，我们要做的就是获取
        cookies = driver.get_cookies()  # Selenium为我们提供了get_cookies来获取登录cookies
        driver.close()  # 获取cookies便可以关闭浏览器
        # 然后的关键就是保存cookies，之后请求从文件中读取cookies就可以省去每次都要登录一次的
        # 当然可以把cookies返回回去，但是之后的每次请求都要先执行一次login没有发挥cookies的作用
        jsonCookies = json.dumps(cookies)  # 通过json将cookies写入文件
        with open('zhihuCookies.json', 'w') as f:
            f.write(jsonCookies)
        print(cookies)
```

执行爬虫程序，第一次执行的时候，selenium会自动打开浏览器，模拟用户点击，用户登录后，获取到cookies，存储到zhihuCookies.json文件中。

![img](Python%E7%88%AC%E8%99%AB.assets/1597113362339-0e9071fa-6819-49ea-864e-2581d4f62ba7.png)

以后执行，程序都将从zhihuCookies.json文件中读取cookies，执行后续操作，这里，我们获取知乎用户信息编辑页面中的用户名：

![img](Python%E7%88%AC%E8%99%AB.assets/1597113378018-f51018a5-d52a-43c8-9be1-b9baac4ecb40.png)



![img](Python%E7%88%AC%E8%99%AB.assets/1597113389639-33741618-5024-40a2-9ff6-80c5c9083e85.png)

至此，一个模拟用户操作浏览器的爬虫程序就完成了。



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

# **Selenium的使用**

```python
from selenium import webdriver

# 设置浏览器路径和驱动路径
browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Chrome 浏览器路径
driver_path = "C:/path/to/chromedriver.exe"  # ChromeDriver 驱动路径

# 设置 Chrome 浏览器选项
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = browser_path

# 创建 Chrome WebDriver 对象
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
```

如果安装了 Chrome 浏览器，并且已经将 ChromeDriver 添加到系统的 PATH 中

```python
pythonCopy Codefrom selenium import webdriver

# 创建 Chrome WebDriver 对象
driver = webdriver.Chrome()
```

## Selenium的介绍

+ Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，类型像我们玩游戏用的按键精灵，可以按指定的命令自动操作，不同是 Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）

+ Selenium可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生

+ Selenium自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器

##  Selenium的环境配置

1 安装模块

```
pip install selenium
```

2 安装驱动

●驱动地址：http://chromedriver.storage.googleapis.com/index.html

●驱动要对应浏览器版本，否则会无法启动

●禁止浏览器更新 打开 cmd 输入 services.msc 打开后台服务，把浏览器自动更新给禁止

## 浏览器对象

+ Selenium 支持非常多的浏览器，如 Chrome、 Firefox、Edge 等，还有Android、BlackBerry 等手机端的浏览器。另外,也支持无界面浏览器 PhantomJS

| 谷歌浏览器对象   | webdriver.Chrome()    |
| ---------------- | --------------------- |
| 火狐浏览器对象   | webdriver.Firefox()   |
| Edge浏览器对象   | webdriver.Edge()      |
| 无头浏览器对象   | webdriver.PhantomJs() |
| Safari浏览器对象 | webdriver.Safari()    |

## 创建浏览器对象

```python
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

path = 'tools/chromedriver.exe'
browser = webdriver.Chrome(path)
```

## 配置浏览器对象

配置参数：https://peter.sh/experiments/chromium-command-line-switches/

**创建 ChromeOptions 对象**

```
options = ChromeOptions()
```

**无头浏览器**

```
options.add_argument('--headless')
options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'")
```

**禁用图片**

```
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option('prefs', prefs)
```

**User-Agent设置**
移动端User-Agent：http://www.fynas.com/ua

```
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
options.add_argument('user-agent=%s' % user_agent)
```

**隐藏自动化测试提示**

```
options.add_experimental_option('excludeSwitches', ['enable-automation'])
```

**防止检测**

```
设置window.navigator.webdriver为False
options.add_argument('--disable-blink-features=AutomationControlled')
```

**设置代理**

```
options.add_argument('--proxy-server=http://121.13.252.60:41564')
```

**隐藏滚动条**

```
options.add_argument('--hide-scrollbars')
```

**禁用JavaScript**

```
options.add_argument('--disable-javascript')
```

**文件下载**

+ download.default_directory：指定路径

+ profile.default_content_settings.popups：0为屏蔽弹窗，1 为开启弹窗

```
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\'}
options.add_experimental_option('prefs', prefs)
```

 **配置浏览器**

```
path = 'tools/chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, options=options)
```

**访问网页**

+ 使用 browser.get()方法 访问指定网页

```
browser.get('https://www.baidu.com')
```

**获取网页源码**

+ 通过 browser.page_source 属性 获取 页面源码

```
source = browser.page_source
print(source)
```



## 元素定位

> 只演示常用的方法

```python
driver.find_element_by_id()                 # 通过id属性定位(唯一)；常用
driver.find_element_by_xpath()              # 通过xpath表达式定位；常用
driver.find_element_by_class_name()         # 通过类名定位；常用
driver.find_element_by_name()               # 通过name属性定位
driver.find_element_by_tag_name()           # 通过标签名定位
driver.find_element_by_css_selector()       # 通过css选择器定位
driver.find_element_by_link_text()          # 通过链接标签的text类容定位
driver.find_element_by_partial_link_text()  # 通过匹配链接标签的text类容定位
```

以百度首页的搜索框节点为例，**搜索python**

<img src="Python%E7%88%AC%E8%99%AB.assets/image-20231110100418776.png" alt="image-20231110100418776" style="zoom:67%;" />

搜索框的`html`结构：

```cobol
<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
```

### id定位

```
find_element_by_id()  `根据`id`属性获取，这里`id`属性是 `kw
```

```python
from selenium import webdriver
import time  
 
browser = webdriver.Chrome()
 
browser.get(r'https://www.baidu.com')  
time.sleep(2)
 
# 在搜索框输入 python
browser.find_element_by_id('kw').send_keys('python')
time.sleep(2)
 
# 关闭浏览器
browser.close()
```

<img src="Python%E7%88%AC%E8%99%AB.assets/image-20231110100335452.png" alt="image-20231110100335452" style="zoom: 80%;" />

### xpath定位

```
find_element_by_xpath()
```

```python
from selenium import webdriver
import time  
 
browser = webdriver.Chrome()
 
browser.get(r'https://www.baidu.com')  
time.sleep(2)
 
# 在搜索框输入 python
browser.find_element_by_xpath("//*[@id='kw']").send_keys('python')
time.sleep(2)
 
# 关闭浏览器
browser.close()
```

### **携带链接的文本选择器**

```python
more = browser.find_element(By.LINK_TEXT, '更多')
print(more)
```

### **携带链接的部分文本选择器**

```python
hao123 = browser.find_element(By.PARTIAL_LINK_TEXT, 'hao')
print(hao123)
```

### 定位多元素

使用 find_elements(by,text) 方法 以列表形式返回所有元素

```python
Input = browser.find_elements(By.TAG_NAME, 'input')
print(Input)
```

## 获取元素属性

### 获取元素文本

<img src="Python%E7%88%AC%E8%99%AB.assets/image-20231110101315893.png" alt="image-20231110101315893" style="zoom: 50%;" />

```
<a class="title-content tag-width c-link c-font-medium c-line-clamp1" href="https://www.baidu.com/s?cl=3&amp;tn=baidutop10&amp;fr=top1000&amp;wd=%E5%90%84%E5%9C%B0%E8%B4%AF%E5%BD%BB%E5%8D%81%E4%B9%9D%E5%B1%8A%E5%85%AD%E4%B8%AD%E5%85%A8%E4%BC%9A%E7%B2%BE%E7%A5%9E%E7%BA%AA%E5%AE%9E&amp;rsv_idx=2&amp;rsv_dl=fyb_n_homepage&amp;sa=fyb_n_homepage&amp;hisfilter=1" target="_blank"><span class="title-content-index c-index-single c-index-single-hot1">1</span><span class="title-content-title">各地贯彻十九届六中全会精神纪实</span></a>
```

```python
from selenium import webdriver
import time  
 
browser = webdriver.Chrome()
 
browser.get(r'https://www.baidu.com')  
 
logo = browser.find_element_by_css_selector('#hotsearch-content-wrapper > li:nth-child(1) > a')
print(logo.text)  #通过 text 属性 获取 元素文本

# 关闭浏览器
browser.close()
```

输出

```python
各地贯彻十九届六中全会精神纪实
```

### 获取元素属性值

<img src="Python%E7%88%AC%E8%99%AB.assets/image-20231110100406152.png" alt="image-20231110100406152" style="zoom:67%;" />

```
<img hidefocus="true" id="s_lg_img" class="index-logo-src" src="//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" width="270" height="129" onerror="this.src='//www.baidu.com/img/flexible/logo/pc/index.png';this.onerror=null;" usemap="#mp">
```

```python
from selenium import webdriver
import time  
 
browser = webdriver.Chrome()
 
browser.get(r'https://www.baidu.com')  
 
logo = browser.find_element_by_class_name('index-logo-src')
print(logo.get_attribute('src')) #获取 元素的属性值
 
# 关闭浏览器
browser.close()
```

输出：

```cobol
https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
```

### 获取其他属性

除了属性和文本值外，还有id、位置、标签名和大小等属性。

```python
from selenium import webdriver
import time  
 
browser = webdriver.Chrome()
 
browser.get(r'https://www.baidu.com')  
 
logo = browser.find_element_by_class_name('index-logo-src')
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)
 
# 关闭浏览器
browser.close()
```

输出：

```cobol
6af39c9b-70e8-4033-8a74-7201ae09d540
{'x': 490, 'y': 46}
img
{'height': 129, 'width': 270}
```

## 元素操作

模拟输入
点击元素
清空输入
元素截图
元素检查
判断元素是否可见
判断元素是否可点击
判断元素是否被选中

### 模拟输入
使用 send_keys(value)方法 指定元素输入内容

```
kw = browser.find_element(By.ID, 'kw')
kw.send_keys('python')
```

### 点击元素
使用 click()方法 点击元素

```
su = browser.find_element(By.ID, 'su')
su.click()
time.sleep(2)
```

### 回车确认

```python
from selenium import webdriver
import time  
 
browser = webdriver.Chrome()
browser.get(r'https://www.baidu.com')  
time.sleep(2)
 
# 定位搜索框
input = browser.find_element_by_class_name('s_ipt')
# 输入python
input.send_keys('python')
time.sleep(2)
# 回车查询
input.submit()
time.sleep(5)
 
# 关闭浏览器
browser.close()
```

### 清空输入

使用 clear()方法 清空元素内容

```
kw = browser.find_element(By.ID, 'kw')
# 输入python
kw.send_keys('python')
time.sleep(2)
# 清除python
kw.clear()
time.sleep(2)
```

### 元素截图

使用screenshot(path)方法截图元素

+ 通过 screenshot_as_base64 属性 获取截图元素 base64

```
su = browser.find_element(By.ID, 'su')
su.screenshot('search.png')

b64_img = su.screenshot_as_base64
print(b64_img)
```

### **元素检查**

#### 判断元素是否可见

使用 is_displayed()方法 判断元素是否可见

```
kw = browser.find_element(By.ID, 'kw')
print(kw.is_displayed())
```

#### 判断元素是否可点击

使用 is_enabled()方法 判断元素是否可点击

```
su = browser.find_element(By.ID, 'su')
print(su.is_enabled())
```

#### 判断元素是否被选中

使用is_selected()方法 判断元素是否被选中

```
kw = browser.find_element(By.ID, 'kw')
print(kw.is_selected())
```

## 获取浏览器属性

获取浏览器标题
获取浏览器尺寸
获取当前网页地址
获取cookies
删除cookies
添加cookie

### 获取浏览器标题

通过 title 属性获取网页标题

```
title = browser.title
print(title)
```

### 获取浏览器尺寸

使用 get_window_size()方法 获取浏览器尺寸

```
size = browser.get_window_size()
win_width = size.get('width')
win_height = size.get('height')
```

### 获取当前网页地址

通过 current_url 获取 网页地址

```
url = browser.current_url
print(url)
```

### 获取cookies

使用get_cookie(name)方法 获取指定 cookie
使用 get_cookies（）方法 获取列表形式的 cookies

```
cookie = browser.get_cookie('BA_HECTOR')
cookies = browser.get_cookies()
print(cookie)
print(cookies)
```

### 删除cookies

使用 delete_cookie(name)方法 删除指定 cookie
使用 delete_cookies()方法 删除所有 cookie

```
browser .delete_cookie('BA_HECTOR')
browser.delete_all_cookies()
```

### 添加cookie

使用add_cookie()方法添加指定cookie

```
for cookie in cookies:
print(cookie)
browser.add_cookie(cookie)
browser.refresh()
```

## 浏览器操作

设置浏览器尺寸
最小化浏览器
最大化浏览器
返回
前进
刷新
关闭浏览器
屏幕截图

### 设置浏览器尺寸

使用 set_window_size(width,height) 方法 设置浏览器尺寸

```
browser.set_window_size(1920, 1080)
```

### 最小化浏览器

使用 minimize_window()方法 最小化浏览器

```
browser.minimize_window()
```

### 最大化浏览器

使用 maximize_window() 方法 最大化浏览器

```
browser.maximize_window()
```

### 返回

使用back()方法 返回上一个页面

```
browser.back()
time.sleep(2)
```

### 前进

使用forward()方法 前进到下一个页面

```
browser. forward()
time.sleep(2)
```

### 刷新

使用 refresh()方法 刷新页面

```
browser.refresh()
time.sleep(2)
```

### 关闭浏览器

```
browser.quit()
```

### 屏幕截图

使用get_screenshot_as_file保存当前页面截图
使用 get_screenshot_as base64获取当前页面截图的base64

```
browser.get_screenshot_as_file('driver.png')
b64_img = browser.get_screenshot_as_base64()
print(b64_img)
```

## 文件上传

```
browser.get('https://imgse.com/')
time.sleep(2)
filepath = r'C:\Users\Administrator\PycharmProjects\pythonProject\Python高级爬虫\19.Session的使用\images\pic.png'
upload = browser.find_element(By.XPATH, '//input[@type="file"]')
upload.send_keys(filepath)
time.sleep(2)
```

## 执行JavaScript

```
2
3
单步执行
使用 execute_script(js)方法 执行 js
1
2
browser.get('https://www.baidu.com')
time.sleep(2)
3
4
browser.execute_script("document.getElementById("su").style["display"]="none"')
time.sleep(2)
异步执行
使用 execute_async_script(js)方法 异步执行 js
1
browser .execute_async_script('setTimeout (function() {debugger) , 2000)' )
2
3
time.sleep(2)
设置元素文本内容
1
2
browser.execute_script("document.querySelector("#kw").value ="selenium"")
time.sleep(2)\

传递参数执行
su = browser.find_element(By.ID, 'su')
browser.execute_script("arguments[0].style["display"]="block"", su)
su.click()
time.sleep(20)
```



## 页面滚动

```
3
火面滚动
获取当前滚动条高度
1
2
scrollTop = browser.execute_script('return document.documentElement.scrollTop')
print(scrollTop)
滚动到指定位置
绝对路径
1
2
scrollTo 中参数1 为 横向滚动条 ，参数2 为 竖向滚动条
browser .execute_script( 'window.scrollTo(0,document .body . scrollHeight)')
time.sleep(2)
相对路径
1
2
browser .execute_script('window.scrollBy(0, -1000) ')
time.sleep(2)

3
滚动到底部
1
2
browser .execute_script('document.documentElement.scrollTop=10000' )
time.sleep(2)
4
滚动到顶部
1
2
browser .execute_script('document.documentElement.scrollTop=o')
time.sleep(2)
```

## 视频操作

```
1
获取视频地址
1
2
browser.get('https://haokan.baidu.com/v?vid=4759456910754957111')
video = browser.find_element(By.TAG_NAME, 'video')
3
4
video_url = browser.execute_script('return arguments[0].currentsrc', video)
print(video_url)
2
3
播放视频
1
2
browser.execute_script('arguments[0].play()', video)
time.sleep(2)
暂停播放
1
2
browser.execute_script("arguments[0].pause()', video)
time.sleep(2)
```



## 选项卡管理

```
四火下目庄
1
打开新标签页
1
browser.execute_script("window.open("https://www.baidu.com")")
2
获取当前标签句柄
1
2
current_handle = browser.current_window_handle
print(current_handle)
3
获取所有标签句柄
1
2
handles = browser.window_handles
print(handles)
4
切换标签页
1
2
browser.switch_to.window(handles[-1])
time.sleep(3)
关闭当前标签页
1
browser.close()
```



## 模拟键盘操作

````
 全选 

●使用 Keys.CONTROL 方法 模拟键入CTRL



1

2

3

4

5

6

7

8

```
from selenium.webdriver.common.keys import Keys

kw = browser.find_element(By.ID, 'kw')

kw.send_keys('python')

time.sleep(2)

kw.send_keys(Keys.CONTROL, 'a')

time.sleep(2)
```



 2 复制 



1

2

kw.send_keys(Keys.CONTROL, 'c')

time.sleep(2)

 3 剪切 



1

2

kw.send_keys(Keys.CONTROL, 'x')

time.sleep(2)

 4 粘贴 



1

2

kw.send_keys(Keys.CONTROL, 'v')

time.sleep(2)

 5 空格 



1

2

kw.send_keys(Keys.SPACE)

time.sleep(2)

 6 后退键 



1

2

kw.send_keys(Keys.BACKSPACE)

time.sleep(2)

 7 回车键 



1

2

kw.send_keys(Keys.ENTER)

time.sleep(2)

 8 TAB键 



1

2

3

kw = browser.find_element(By.ID, 'kw')

kw.send_keys(Keys.TAB)

time.sleep(2)

 9 F5键 



1

2

kw.send_keys(Keys.F5)

time.sleep(2)
````



## IFrame切换

我们知道网页中有一种节点叫作 iframe，也就是子 Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。Selenium 打开页面后，它默认是在父级 Frame 里面操作，而此时如果页面中还有子 Frame，它是不能获取到子 Frame 里面的节点的。这时就需要使用 switch to.frame() 方法来切换 Frame



```
 切换到子页面 

●使用 switch_to.frame(iframe) 方法 切换到子页面



1

2

3

4

5

browser.get('https://www.douban.com/')

time.sleep(2)

IFrame = browser.find_element(By.TAG_NAME, 'iframe')

browser.switch_to.frame(IFrame)

browser.find_element(By.NAME, 'phone').send_keys('123')

 2 切换到初始主页面 

●使用 switch.default_content() 方法 切换到主页面



1

2

3

browser.switch_to.default_content()

browser.find_element(By.CSS_SELECTOR, '.inp input').send_keys('python')

time.sleep(2)


```



## 选择框操作

```
browser.get(

r'file:///C:\Users\Administrator\PycharmProjects\pythonProject\Python高级爬虫\19.Session的使用\tools\selenium.html')

time.sleep(2)



 单选框 



1

2

3

radios = browser.find_elements(By.CSS_SELECTOR, 'input[name="r1"]')

radios[1].click()

time.sleep(2)

2 多选框

 1 取消已选项目 



1

2

3

4

checkbox = browser.find_elements(By.CSS_SELECTOR, '#checkbox input[checked]')

for cb in checkbox:

​    cb.click()

​    time.sleep(2)

2 选中多选框项目



1

2

3

checkbox = browser.find_elements(By.CSS_SELECTOR, '#checkbox input')

checkbox[1].click()

time.sleep(2)

3 下拉框

 1 创建下拉框对象 

●使用 Select(element) 方法 将元素 转换为下拉框对象



1

2

3

from selenium.webdriver.support.select import Select

select = Select(browser.find_element(By.ID, 'pro'))

2 通过索引选中下拉框项目



1

2

select.select_by_index(1)

time.sleep(2)

 3 通过可见文本选中下拉框项目 



1

2

select.select_by_visible_text('广东')

time.sleep(2)

 4 通过value属性值选中下拉框 



1

2

select.select_by_value('bj')

time.sleep(2)
```

## 对话框处理

```
 对话框处理 

●使用 browser.switch_to.alert 方法 切换 到对话框

 1 警示框 

●使用 accept() 方法 确认 警示框



1

2

3

4

browser.find_element(By.ID, 'bu1').click()

time.sleep(2)

alert = browser.switch_to.alert

alert.accept()

 2 确认框 

●使用 dismiss() 方法 取消 确认框



1

2

3

4

5

browser.find_element(By.ID, 'bu2').click()

time.sleep(2)

confirm = browser.switch_to.alert

confirm.dismiss()

confirm.accept()

 3 提示框 

●使用 send_keys(value) 方法 输入内容



1

2

3

4

5

6

browser.find_element(By.ID, 'bu3').click()

prompt = browser.switch_to.alert

print(prompt.text)

time.sleep(2)

prompt.send_keys('python')

prompt.accept()
```



## 延时等待

现在的网页越来越多采用了 Ajax 技术，这样程序便不能确定何时某个元素完全加载出来了。如果实际页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常
●为了避免这种元素定位困难而且会提高产生 ElementNotVisibleException 的概率。所以 Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待



```
强制等待
●使用 time.sleep(second) 方法 阻塞等待



1

2

3

4

5

6

7

start = time.time()

browser.get('https://www.baidu.com')

time.sleep(2)

news = browser.find_elements(By.CLASS_NAME, 'title-content-title')

for item in news:

​    print(item.text)

​    print(time.time() - start)

 2 隐式等待 

●隐式等待是等待特定的时间，一个浏览器对象只需调用一次，获取的元素如果在指定时间内加载完毕则继续执行，否则报错

●使用 implicitly_wait(second) 方法 隐式等待



1

2

3

4

5

6

7

start = time.time()

browser.get('https://www.baidu.com')

browser.implicitly_wait(20)

news = browser.find_elements(By.CLASS_NAME, 'title-content-title')

for item in news:

​    print(item.text)

​	print(time.time() - start)
```



3 显式等待

●显式等待指定某个条件，然后设置最长等待时间，如果在指定时间还没有符合条件，则报错

4 等待条件

| title_is                                   | 标题是某内容                                       |
| ------------------------------------------ | -------------------------------------------------- |
| title contains                             | 标题包含某内容                                     |
| presence of element located                | 节点加载出，传入定位元组，如(By.ID,p')             |
| visibility of element located              | 节点可见，传入定位元组                             |
| visibility_of                              | 可见，传入节点对象                                 |
| presence_of all elements located           | 所有节点加载出                                     |
| text to be_present in element              | 某个节点文本包含某文字                             |
| text to_be_present in element_value        | 某个节点值包含某文字                               |
| frame to be available and switch to iframe | 加载并切换                                         |
| invisibility_of element located            | 节点不可见                                         |
| element to be clickable                    | 节点可点击                                         |
| staleness of                               | 判断一个节点是否仍在 DOM，可判断页面是否已经刷新   |
| element to be selected                     | 节点可选择，传节点对象                             |
| element located to be selected             | 节点可选择，传入定位元组                           |
| element selection state to be              | 传入节点对象以及状态，相等返回 True，否则返回False |
| element located selection state to be      | 传入定位元组以及状态，相等返回 True，否则返回False |
| alert is present                           | 是否出现 Alert                                     |

5 创建WebDriverWait对象

WebDriverWait(driver,timeout,poll_frequency,ignored_exceptions)

driver：浏览器对象

timeout：最大超时时间(秒)

poll_frequency：执行间隔(秒)

ignored_exceptions：忽略的异常

```
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(browser, 10, 0.2)
```

等待指定条件符合
●使用 wait.until(method) 方法 等待指定条件符合，直到返回值的计算结果 为 True
●使用 EC.presence_of_element_located(locator) 方法 判断元素是否加载完毕
●使用 EC.presence_of_all_elements_located(locator) 方法 判断所有元素加载完毕

```

start = time.time()
browser.get('https://www.baidu.com')
news = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'title-content-title')))
for item in news:
    print(item.text)
    print(time.time() - start)

kw = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
kw.send_keys('python')
```

等待指定条件不符合
●使用 wait.until_not(method) 方法 等待指定元素不符合条件，直到返回值的计算结果 为 False
●使用 EC.element_to_be_clickable(locator) 方法 判断元素是否可点击
●使用 EC.visibility_of_element_located(locator) 方法 判断元素是否可见

```
wait.until(EC.element_to_be_clickable((By.ID, 'su'))).click()
wait.until_not(EC.visibility_of_element_located((By.ID, 's_lg_img_new')))
```



## 动作链

```
 创建动作链对象
●
使用 ActionChains(driver) 方法 创建动作链对象
2
 点击元素
●
使用 actions.click(element) 方法 点击元素
●
使用 perform() 方法 执行动作链
3
 模拟输入
4
 指定元素模拟输入
5
 双击元素
1
2
action.double_click(user).perform()
time.sleep(2)
6
 右击元素
1
2
action.context_click(user).perform()
time.sleep(2)
7
 长按元素
1
2
3
login_btn = browser.find_element(By.XPATH, '//*[@id="J-login"]')
action.click_and_hold(login_btn).perform()
time.sleep(0.5)
8
 释放
1
2
action.release().perform()
time.sleep(2)
9
 移动到元素
1
2
3
note_btn = browser.find_element(By.LINK_TEXT, '短信验证')
action.move_to_element(note_btn).click().perform()
time.sleep(2)
10
 移动到元素偏移量
1
2
3
4
5
block = browser.find_element(By.LINK_TEXT, '滑块验证')
width = block.size.get('width')
height = block.size.get('height')
action.move_to_element_with_offset(block, width / 2, height / 2).click().perform()
time.sleep(2)
11
 拖动元素
1
 拖动到元素
1
2
3
4
block = browser.find_element(By.XPATH, '//*[@class="nc_iconfont btn_slide"]')
bar = browser.find_element(By.XPATH, '//*[@class="nc-lang-cnt"]')
action.drag_and_drop(block, bar).perform()
time.sleep(2)
2
 拖动到偏移量
1
2
action.drag_and_drop_by_offset(block, bar.size.get('width'), 0).perform()
time.sleep(10)
```



## 异常处理

```
TimeoutException
1
2
3
4
5
6
from selenium.common.exceptions import TimeoutException, NoSuchElementException

try:
browser.get('https://www.baidu.com')
except TimeoutException:
print('执行超时！')
2
 NoSuchElementException
1
2
3
4
try:
    browser.find_element(By.ID, 'python')
except NoSuchElementException:
	print('该元素不存在！')


```

## 使用selenium爬百度文库ppt

百度文库共享文档要下载券下载真的是烦死人，但是一个个图片点击保存又太麻烦。所以就只能有劳python爬虫大人出马了。不过鉴于我技术不过关，写出的爬虫等级比较低下.

下面介绍下我在写这个简单爬虫的过程.

概览：

图片ppt合成pdf分析网页必要编码步骤编写过程

这里的例子是爬高数答案ppt

网址：https://wenku.baidu.com/view/78deda6ac381e53a580216fc700abb68a882ad56.html?from=search 

### 1.分析网页

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

### 2.编码

直接在代码中解释，没有注释的地方可以当作模板，直接跳过

结果：

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255203.png)

### 3.把图片合成pdf

全部选择：

![img](https://raw.githubusercontent.com/Auroraol/Drawing-bed/main/img/202311081255204.png)

## 报错

[python selenium报错ValueError: Timeout value connect was ＜...＞, but it must be an int, float or None.](https://blog.csdn.net/liu_liu_123/article/details/131146119)

最初安装的Selenium版本是3.141.0，Urllib3的版本是2.0.3，这两个版本的库是不兼容的，如果安装的是这两个库，那么在使用selenium时，就会显示上述错误。

 方案二：根据文末BH4EOD的评论，将selenium降为3.3.1，也可以解决问题。没自己试验过，如果方法一解决不了，也可以试下这个方法。

   方案三：因python版本不对应，导致出错。根据[weixin_38686363](https://blog.csdn.net/weixin_38686363)在文末评论，他直接调用conda虚拟环境用的python3.10会出错，后来换成python 3.8.10，问题就解决了。

   方案二和三，我没亲身体验过，不过是别的网友成功过的。如果方案一解决不了，可以试一下二和三。希望遇到问题的网友把解决这一问题的办法能在留言里写一下。我会把留言中的问题解决办法归集在一起，让大家的经验帮助更多的人。

   **其他问题及解决方案：**

​    **1、urllib3版本无法降到1.26.2。**根据网友Th3Shine在文末的评论，把python版本降到3.10可顺利将urllib3版本降到1.262。

   **2、显示错误‘No module named 'urllib3.packages.six.moves'。**根据网友[tomniu8998](https://blog.csdn.net/tomniu8998)和[weixin_46250057](https://blog.csdn.net/weixin_46250057)在文末的回复，把selenium版本调整到3.3.1配合urllib3版本1.26.2，这一问题基本都能解决。若仍无法解决，可更换selenium版本：pip install urllib3==2.1.0
pip install selenium==4.8.0

# **多线程的使用**

## 封装线程类

```python
import requests
import threading
import pymongo
from queue import Queue


class Spider:
    def __init__(self):
        # 连接数据库
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        # 创建数据库集合
        self.collection = self.client['spider']['spider_coll']
        # 定义网页信息
        self.url = '要获取的网页地址'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }
        # 创建队列
        self.params_queue = Queue()  # 请求参数 队列
        self.data_queue = Queue()  # 网页数据 队列
        self.result_queue = Queue()  # 解析数据 队列
        
    # 请求参数
    def get_params(self):
        # 获取页数设置
        for page in range(1, 2):  #页面参数
            # 处理请求参数
            params = {'page': page}
            # 将 请求参数 放入 params队列，该队列计数加一
            self.params_queue.put(params)

   # 响应数据
    def get_data(self):
        while True:
            # 从 params队列 取出 params参数，该队列计数不变
            params = self.params_queue.get()
            # 获取网页数据
            response = requests.get(url=self.url, params=params, headers=self.headers)
            print(response.json())
            # 将 响应数据 放入 data队列，该队列计数加一
            self.data_queue.put(response.json())
            # params队列计数减一，队列使用 get 与 task_done 方法后计数才会减少
            self.params_queue.task_done()

    # 解析数据        	
    def parse_data(self):
        while True:
            # 从 data队列 中 取出 响应数据
            data = self.data_queue.get()
            # 解析 响应数据
            for item in data:
                item_info = {}
                item_info['title'] = '获取的标题'
                item_info['follow'] = '获取的关注量'
                item_info['url'] = '获取的详情地址'
                # 将 解析数据 放入 result队列，该队列计数加一
                self.result_queue.put(item_info)
                # data队列计数减一
                self.data_queue.task_done()

    def save_data(self):
        while True:
            # 从 result队列 中 取出 解析数据
            result = self.result_queue.get()
            # 将 解析数据 保存 到 mongo数据库
            self.collection.insert_one(result)
            # result队列计数减一
            self.result_queue.task_done()

    def main(self):
        # 定义一个线程列表
        thread_list = []

        # 创建 get_params 子线程，一般创建一个子线程即可
        for i in range(1):
            td_get_params = threading.Thread(target=self.get_params)
            thread_list.append(td_get_params)  # 将 子线程 放入 线程列表

        # 创建 get_data 子线程，该线程用于获取数据，可创建多个线程
        for i in range(3):
            td_get_data = threading.Thread(target=self.get_data)
            thread_list.append(td_get_data)

        # 创建 parse_data 子线程
        for i in range(1):
            td_parse_data = threading.Thread(target=self.parse_data)
            thread_list.append(td_parse_data)

        # 创建 save_data 子线程
        for i in range(1):
            td_save_data = threading.Thread(target=self.save_data)
            thread_list.append(td_save_data)

        # 遍历 线程列表
        for t in thread_list:
            t.setDaemon(True)  # 设置 为 守护主线程，主线程结束，子线程也结束
            t.start()  # 启动线程

        # 主线程阻塞，等待所有队列计数为零
        for q in [self.params_queue, self.data_queue, self.result_queue]:
            q.join()


if __name__ == '__main__':
    spider = Spider()  # 实例化线程类
    spider.main()  # 执行程序
```

## 多线程爬虫案例

使用多线程获取到爱奇艺视频电视剧的信息

目标网址:  [内地电视剧大全-好看的内地电视剧排行榜-爱奇艺](https://list.iqiyi.com/www/2/15-------------11-1-1-igiyi--.html?s_source=PCW_SC)

+ 获取标题、链接、描述信息并保存到mongo数据库

```python
import threading
import time

import pymongo
import requests
from retrying import retry
from queue import Queue


class IQiYi:
    def __init__(self):
        self.client = pymongo.MongoClient(
            host='localhost',
            port=27017
        )
        self.collection = self.client['spider']['iqy']
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }
        self.params_queue = Queue()  # 创建处理params参数的队列
        self.data_queue = Queue()  # 创建存储网页数据的队列
        self.result_queue = Queue()  # 创建存储解析数据的队列

    def get_params(self):
        for page in range(1, 20):
            params = {
                'channel_id': '2',
                'data_type': '1',
                'mode': '11',
                'page_id': page,
                'ret_num': '48',
                'session': '63bd9816bc423d33355fcf0333b55637',
                'three_category_id': '15;must',
            }
            # 将各页数的 params参数 放入 params队列
            self.params_queue.put(params)
            
    def get_data(self):
            while True:
                # 从 params队列 中取出params参数
                params = self.params_queue.get()
                # 获取网页数据
                response = requests.get(url=self.url, params=params)
                print(response.json())
                # 将 响应数据 放入 data队列
                self.data_queue.put(response.json())
                # params队列的计数-1
                self.params_queue.task_done()

    def parse_data(self):
        while True:
            # 从data队列中取出data参数
            response = self.data_queue.get()
            # 解析数据
            data = response['data']['list']
            for item in data:
                item_info = {}
                item_info['title'] = item['title']
                item_info['playUrl'] = item['playUrl']
                item_info['description'] = item['description'].replace('\n', '')
                # print(item_info)
                # 将 解析的数据 放入result队列
                self.result_queue.put(item_info)
            # data队列计数-1
            self.data_queue.task_done()

    def save_data(self):
        while True:
            # 从result队列中取出result参数
            result = self.result_queue.get()
            # 插入数据到mongo数据库
            self.collection.insert_one(result)
            # result队列计数-1
            self.result_queue.task_done()

    def main(self):
        thread_list = []

        # 创建 get_params子线程
        for i in range(1):
            td_get_params = threading.Thread(target=self.get_params)
            thread_list.append(td_get_params)

        # 创建 get_data 子线程
        for i in range(3):
            td_get_data = threading.Thread(target=self.get_data)
            thread_list.append(td_get_data)

        # 创建 parse_data 子线程
        for i in range(1):
            td_parse_data = threading.Thread(target=self.parse_data)
            thread_list.append(td_parse_data)

        # 创建 save_data 子线程
        for i in range(1):
            td_save_data = threading.Thread(target=self.save_data)
            thread_list.append(td_save_data)

        # 遍历 子线程 列表
        for t in thread_list:
            t.setDaemon(True)  # 设置 为 守护主线程 主线程结束，子线程也结束
            t.start()  # 启动线程

        # 主线程阻塞，等待队列的计数为零
        for q in [self.params_queue, self.data_queue, self.result_queue]:
            q.join()


if __name__ == '__main__':
    start = time.time()
    iqy = IQiYi()
    iqy.main()
    end = time.time()
    print(end - start)
```

## **线程池实现爬虫**

### 线程池介绍

+ 线程池，是一种线程的使用模式，它为了降低线程使用中频繁的创建和销毁所带来的资源消耗与代价。通过创建一定数量的线程，让他们时刻准备就绪等待新任务的到达，而任务执行结束之后再重新回来继续待命

### 线程池的使用

#### 定义线程任务

```
def task():
    print('running task...')
	time.sleep(1)
	return 'success'
```

#### 创建一个线程池

●调用 ThreadPoolExecutor 类的构造器创建一个线程池

●使用 max_workers 方法 设置创建的线程数量

```
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=5)
```

#### 提交线程任务

●调用 ThreadPoolExecutor 对象的 submit 方法来提交线程任务

●使用 result 方法返回线程任务的返回值

```
result_list = []
for i in range(10):
    response = pool.submit(task)
	result_list.append(response)

for res in result_list:
    print(res.result())
```

#### 关闭线程池

●调用 ThreadPoolExecutor 对象的 shutdown 方法来关闭线程池

```
pool.shutdown()
```

### **封装进程池类**

```python
import time
import pymysql


class Spider:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123123',
            db='spider'
        )
        self.cursor = self.db.cursor()
        self.url = '要获取的地址'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }

    def create_table(self):
        sql = """CREATE TABLE name(
            id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            title VARCHAR(255) NOT NULL,
            pageUrl TEXT NOT NULL,
            desc TEXT NOT NULL
        )"""
        try:
            self.cursor.execute(sql)
            print('CREATE SUCCESS')
        except Exception as e:
            print('CREATE FAILED,CASE:', e)

    def get_data(self, page):
        params = {
            'page': page
        }
        response = requests.get(url=self.url, params=params, headers=self.headers)
        return response.json()

    def parse_data(self, response):
        for item in data:
            title = item.get('title')
            pageUrl = item.get('pageUrl')
            desc = item.get('desc')

            self.save_data(name, title, pageUrl, desc)

    def save_data(self, name, title, pageUrl, desc):
        sql = 'INSERT INTO name(id,title,pageUrl,desc) VALUES (%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, args=(0, name, title, pageUrl, desc))
            self.db.commit()
            print('INSERT SUCCESS')
        except Exception as e:
            self.db.rollback()
            print('INSERT FAILED,CASE:', e)

    def run(self):
        page = 10
        # 创建线程池对象，设置5个线程
        with ThreadPoolExecutor(5) as pool:
            for p in range(1, page + 1):
                # 线程池提交线程任务
                response = pool.submit(self.get_data, p)
                # 获取线程任务的返回值，并且解析数据
                self.parse_data(response.result())


if __name__ == '__main__':
    spider = Spider()
    spider.run()
```

### 进程池案例

 使用线程池获取百度招聘Python岗位信息

目标地址：[百度招聘](https://talent.baidu.com/external/baidu/index.html)

+ 获取名称、工作条件、工作内容、工作地点

```python
# 目标地址：https://talent.baidu.com/external/baidu/index.html
# 
import time
from concurrent.futures import ThreadPoolExecutor

import pymysql
import requests


class Baidu:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123123',
            db='spider'
        )
        self.cursor = self.db.cursor()
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            'Referer': 'https://talent.baidu.com',
            'Cookie': 'BIDUPSID=6DAE2BE6DE41A36518E0802F1B820BAA; PSTM=1672477071; BAIDUID=6DAE2BE6DE41A365056D0C9618163E37:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=6DAE2BE6DE41A365056D0C9618163E37:FG=1; Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1672559377,1672559564; RT="z=1&dm=baidu.com&si=7w2nasej03r&ss=lcd2o1kb&sl=5&tt=342&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=1672559581',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS baidu2(
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                serviceCondition TEXT NOT NULL,
                workContent TEXT NOT NULL,
                workPlace VARCHAR(255) NOT NULL                          
        )"""
        try:
            self.cursor.execute(sql)
            print('CREATE TABLE SUCCESS')
        except Exception as e:
            print('CREATE TABLE FAILED,CASE:', e)


    def get_data(self, keyword, page):
        data = {
            'recruitType': 'SOCIAL',
            'pageSize': '10',
            'keyWord': keyword,
            'curPage': page,
            'projectType': '',
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        # print(response.json())
        return response.json()

    def parse_data(self, response):
        data = response['data']['list']
        for item in data:
            name = item.get('name', '无')
            serviceCondition = item.get('serviceCondition', '无')
            workContent = item.get('workContent', '无')
            workPlace = item.get('workPlace', '无')
            # print(name, serviceCondition, workContent, workPlace)
            # 数据库插入数据
            self.save_data(name, serviceCondition, workContent, workPlace)

    def save_data(self, name, serviceCondition, workContent, workPlace):
        sql = 'INSERT INTO baidu2(id,name,serviceCondition, workContent, workPlace) values(%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, args=(0, name, serviceCondition, workContent, workPlace))
            self.db.commit()  # 提交
            print('INSERT SUCCESS')
        except Exception as e:
            self.db.rollback()  # 回滚
            print('INSERT FAILED,CASE:', e)

    def run(self):
        keyword = input('请输入招聘岗位：')
        page = int(input('请输入页数：'))
        self.create_table()
        start = time.time()
        # 创建线程池对象[同时创建五个线程]
        with ThreadPoolExecutor(5) as pool:
            for page in range(1, page + 1):
                # 提交线程任务给线程池
                response = pool.submit(self.get_data, keyword, page)
                # 使用result方法获取线程
                self.parse_data(response.result())
        self.cursor.close()
        self.db.close()
        print(time.time() - start)


if __name__ == '__main__':
    baidu = Baidu()
    baidu.run()
```

# 多进程爬虫

+  由于GIL全局锁的存在，多线程在python3下可能只是个摆设，对应的解释器执行其中的内容的时候仅仅是顺序执行，此时我们可以考虑多进程的方式实现，思路和多线程相似，只是对应的api不相同

## **封装多进程类**

```python
import time
from multiprocessing import Process, JoinableQueue as Queue

import pymongo
import requests

# 连接数据库，需要将mongo定义为全局变量，因为进程之间不共享
client = pymongo.MongoClient(
    host='localhost',
    port=27017,
)
# 创建数据库集合
collection = client['spider']['tencent_video']


class Spider:
    def __init__(self):
        self.start = None
        # 定义网页信息
        self.url = '要获取的网页地址'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }
        # 创建队列
        self.params_queue = Queue()
        self.data_queue = Queue()
        self.result_queue = Queue()

    def get_params(self, page):
        for i in range(page):
            # 批量处理data参数
            data = {"page": page}
            # 将 data参数 放入 params队列，该队列计数加一
            self.params_queue.put(data)

    def get_data(self):
        while True:
            # 从 params队列 取出 data参数，该队列计数不变
            data = self.params_queue.get()
            # 获取网页数据
            response = requests.post(url=self.url, headers=self.headers, json=data)
            print(response.json())
            # 将 响应数据 放入 data队列
            self.data_queue.put(response.json())
            # params队列计数减一
            self.params_queue.task_done()

    def parse_data(self):
        while True:
            # 从 data队列 中 取出 响应数据
            data = self.data_queue.get()
            # 解析响应数据
            for item in data:
                item_info = {}
                item_info['title'] = item.get('title')
                item_info['pageUrl'] = item.get('pageUrl')
                item_info['desc'] = item.get('desc')
                print(item_info)
                # 将 解析数据 放入 result队列
                self.result_queue.put(item_info)
            # data队列计数减一
            self.data_queue.task_done()

    def save_data(self):
        while True:
            # 从 result队列 中 取出 解析数据
            result = self.result_queue.get()
            # 数据库插入数据
            collection.insert_one(result)
            # result队列计数减一
            self.result_queue.task_done()

    def run(self):
        page = 5
        self.start = time.time()
        # 定义进程列表
        process_list = []
        # 创建 get_params 子进程
        for i in range(1):
    print(time.time() - spider.start)
```

##  多进程爬虫案例 

 使用多进程获取腾讯视频电视剧一栏里的电视剧信息 

目标网址：[腾讯视频 - 中国领先的在线视频媒体平台,海量高清视频在线观看](https://v.qq.com/channel/tv?channel=tv&feature=7&iarea=814&listpage=1)

+ 提取名称、集数、描述，获取20个页面

```python
import time
            # 批量处理data参数
            data = {"page_context": {"page_index": page},
                    "page_params": 
                    {"page_id": "channel_list_second_page", "page_type": "operation",
                     "channel_id": "100113", "filter_params": "", "page": page}}
            # 将 data参数 放入 params队列，该队列计数加一
            self.params_queue.put(data)

    def get_data(self):
        while True:
            # 从 params队列 取出 data参数，该队列计数不变
            data = self.params_queue.get()
            # 获取网页数据
            response = requests.post(url=self.url, headers=self.headers, json=data)
            print(response.json())
            # 将 响应数据 放入 data队列
            self.data_queue.put(response.json())
            # params队列计数减一
            self.params_queue.task_done()

    def parse_data(self):
        while True:
            # 从 data队列 中 取出 响应数据
            response = self.data_queue.get()
            # 解析响应数据
            try:
                data = response["CardList"][1]["children_list"]["list"]["cards"]
            except:
                data = response["CardList"][0]["children_list"]["list"]["cards"]
            for item in data:
                item_info = {}
                item_info['title'] = item.get('params').get('title', '无')
                item_info['second_title'] = item.get('params').get('second_title', '无')
                item_info['timelong'] = item.get('params').get('timelong', '无')
                print(item_info)
                # 将 解析数据 放入 result队列
                self.result_queue.put(item_info)
            # data队列计数减一
            self.data_queue.task_done()

    def save_data(self):
        while True:
            # 从 result队列 中 取出 解析数据
            result = self.result_queue.get()
            # 数据库插入数据
            collection.insert_one(result)
            # result队列计数减一
            self.result_queue.task_done()

    def run(self):
        page = int(input('请输入页数：'))
        self.start = time.time()
        # 定义进程列表
        process_list = []
        # 创建 get_params 子进程
        for i in range(1):
            p_get_params = Process(target=self.get_params, args=(page,))
            process_list.append(p_get_params)
        # 创建 get_data 子进程，可创建多个进程
        for i in range(5):
            p_get_data = Process(target=self.get_data)
            process_list.append(p_get_data)
        # 创建 parse_data 子进程，可创建多个进程
        for i in range(1):
            p_parse_data = Process(target=self.parse_data)
            process_list.append(p_parse_data)
        # 创建 save_data 子进程
        for i in range(1):
            p_save_data = Process(target=self.save_data)
            process_list.append(p_save_data)
        # 遍历 进程列表
        for p in process_list:
            p.daemon = True  # 设置为守护进程，主进程结束，子进程也结束
            p.start()  # 启动进程
            time.sleep(0.5)

        # 主进程堵塞，等待所有队列为零
        for q in [self.params_queue, self.data_queue, self.result_queue]:
            q.join()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
    print(time.time() - spider.start)
```

# **异步协程爬虫:crossed_swords:**

##  异步协程介绍

  **异步** 

●为完成某个任务，不同程序单元之间过程中无需通信协调，也能完成任务的方式，不相关的程序单元之间可以是异步的，例如：爬虫下载网页

●调度程序调用下载程序后，即可调度其他任务，而无需与该下载任务保持通信以协调行为，不同网页的下载、保存等操作都是无关的，也无需相互通知协调，这些异步操作的完成时刻并不确定

 **同步** 

●不同程序单元为了完成某个任务，在执行过程中需靠某种通信方式以协调一致，我们称这些程序单元是同步执行的

 **阻塞** 

●阻塞状态指程序未得到所需计算资源时被挂起的状态。程序在等待某个操作完成期间，自身无法继续处理其他的事情，则称该程序在该操作上是阻塞的

 **非阻塞** 

●程序在等待某操作过程中，自身不被阳塞，可以继续处理其他的事情，则称该程序在该操作上是非阻塞的

●同步/异步关注的是消息通信机制

●阻塞/非阻塞关注的是程序在等待调用结果(消息，返回值) 时的状态

## Aiohttp介绍 

●aiohttp是一个为Python提供异步HTTP客户端/服务端编程，基于asyncio用于支持异步编程的标准库)的异步库asyncio可以实现单线程并发I/O操作，其实现了TCP、UDP、SSL等协议，aiohttp就是基于asyncio实现的http框架。

●async 用来声明一个函数为异步函数

●await 用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异先程序

## Aiohttp的使用

### **单线程发送请求**

```
import time
import requests


def main():
    for i in range(50):
        res = requests.get('https://www.baidu.com')
        print(i, res.status_code)

if __name__ == '__main__':
    t1 = time.time()
    main()
    print(time.time() - t1)
```

###  Aiohttp发送请求

调用协程对象

```python
import asyncio
import time


async def request(client, i):
    # 使用 client 对象的 get 方法 发送请求，通过await关键字阻塞
    res = await client.get('https://www.baidu.com')
    return i, res.status


async def main():
    # 使用 上下文管理器 创建 aiohttp.ClientSession 对象
    async with aiohttp.ClientSession() as client:
        for i in range(50):
            # 使用await关键字阻塞，调用 协程对象，传递 client 对象
            res = await request(client, i)
            print(res)


t1 = time.time()
# 使用 asyncio.run 方法 调用 协程对象
asyncio.run(main())
print(time.time() - t1)
```

**调用task对象**

```python
import asyncio
import aiohttp
import time


async def request(client, i):
    # 使用 client 对象 的 get 方法 发送请求，通过await关键字阻塞
    res = await client.get('https://www.baidu.com')
    return i, res.status


async def main():
    # 使用 上下文管理器 创建 aiohttp.ClientSession 对象
    async with aiohttp.ClientSession() as client:
        task_list = []
        for i in range(50):
            # 创建 协程对象
            req = request(client, i)
            # 创建 task对象
            task = asyncio.create_task(req)
            task_list.append(task)

        # 将 协程列表转换为可等待的对象，使用await关键字阻塞
        # wait对象返回一个元组：task集合、各协程任务的状态
        done, pending = await asyncio.wait(task_list)
        for item in done:
            # 使用 result 方法 获取协程任务的返回值
            print(item.result())


t1 = time.time()
# 使用 asyncio.run 方法 调用 协程对象
asyncio.run(main())
print(time.time() - t1)
```

##  异步协程爬虫案例 

 采集王者荣耀官网里面所有的图片信息 

目标网址:[英雄资料列表页-英雄介绍-王者荣耀官方网站-腾讯游戏](https://pvp.qq.com/web201605/herolist.shtml)

<img src="Python%E7%88%AC%E8%99%AB.assets/image-20231110153040459.png" alt="image-20231110153040459" style="zoom: 50%;" />

```python
import asyncio
import aiohttp
import os


class WzRy:
    def __init__(self):
        self.url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

    async def download_img(self, session, ename, cname):
        for i in range(1,11):
            print(self.skin_url.format(ename, ename, i))
            filename = f'王者荣耀/{cname}-{i+1}.jpg'
            print(f'开始下载：{filename}')
            # 使用 session.get 方法 获取 发送图片链接请求
            response = await session.get(self.skin_url.format(ename, ename, i))
            if response.status == 200:  # 获取 响应状态码
                # 使用 response.read方法 获取 二进制数据，通过 await关键字 阻塞
                content = await response.read()
                with open(filename, mode='wb') as f:
                    f.write(content)
            else:
                break

    async def run(self):
        # 创建 aiohttp.ClientSession 对象
        async with aiohttp.ClientSession() as session:
            # 使用 await关键字 阻塞，使用 session.get 方法 返回 响应数据
            response = await session.get(url=self.url, headers=self.headers)
            # 使用 response.json 方法 获取 响应数据，乱码数据报错，则content_type参数设置为None
            data = await response.json(content_type=None)
            task_list = []
            for item in data:
                ename = item['ename']
                cname = item['cname']
                # 创建 task对象，将 session对象、ename、cname传递给 download_img 方法
                task = asyncio.create_task(self.download_img(session, ename, cname))
                task_list.append(task)

            # 将协程列表转换为wait对象，使用 await关键字 阻塞 并 执行
            await asyncio.wait(task_list)


if __name__ == '__main__':
    if not os.path.exists('王者荣耀'):
        os.mkdir('王者荣耀')
    wzry = WzRy()
    asyncio.run(wzry.run())
```

 通过异步的方式获取到英雄联盟官网的英雄皮肤图片 

目标网址: [攻略中心-英雄联盟官方网站-腾讯游戏](https://101.qq.com/#/hero)

```py
import asyncio
import os

import aiohttp


class LOL:
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2787894'
        self.skin_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2788293'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

    async def parse_data(self, session, heroId):
        # 使用 await 关键字阻塞，使用 session.get 方法 获取 响应数据
        response = await session.get(url=self.skin_url.format(heroId))
        # 使用 await 关键字阻塞，使用 response.json 方法 获取 json数据
        data = await response.json(content_type=None)
        task_list = []
        for skin in data.get('skins'):
            title = skin.get('name')
            img_url = skin.get('mainImg')
            if img_url:
                # 创建 download_img 方法 的 task对象，传递session, img_url, title
                task = asyncio.create_task(self.download_img(session, img_url, title))
                task_list.append(task)
        # 使用 await 关键字阻塞，使用asyncio.wait方法 将 task_list 列表 转换为 可等待的对象
        await asyncio.wait(task_list)

    async def download_img(self, session, url, title):
        # 使用 await 关键字阻塞，使用 session.get 方法 请求图片链接
        response = await session.get(url, headers=self.headers)
        if response.status == 200:
            filename = f'英雄联盟/{title}.jpg'
            print(f'正在下载：{filename}')
            # 使用 await 关键字阻塞，使用 response.read() 方法 获取 响应二进制数据
            content = await response.read()
            with open(filename, mode='wb') as f:
                f.write(content)

    async def run(self):
        # 使用 上下文管理器 创建 aiohttp.ClientSession 对象
        async with aiohttp.ClientSession() as session:
            # 使用 await 关键字阻塞，使用 session.get 方法 获取 响应数据
            response = await session.get(url=self.url, headers=self.headers)
            # 使用 await 关键字阻塞，使用 response.json 方法 获取 json数据
            data = await response.json(content_type=None)
            task_list = []
            for hero in data.get('hero'):
                heroId = hero.get('heroId')
                # 创建 parse_data 方法 的 task对象，传递session、heroId
                task = asyncio.create_task(self.parse_data(session, heroId))
                task_list.append(task)
            # 使用 await 关键字阻塞，使用asyncio.wait方法 将 task_list 列表 转换为 可等待的对象
            await asyncio.wait(task_list)


if __name__ == '__main__':
    if not os.path.exists('英雄联盟'):
        os.mkdir('英雄联盟')
    lol = LOL()
    # 使用 asyncio.run 方法 调用 协程对象
    asyncio.run(lol.run())
```



# 网站分析方法:crossed_swords:

## Ajax数据或请求json数据

### 分析网站数据是否是Ajax请求

当我们需要运用爬虫程序爬取网站信息数据时，最先需要分析数据到底是在服务器端组成好发回给浏览器的？还是通过Ajax请求进行发送的？
 验证方法：

1.  点击要爬取的网页数据的下一页，观察地址栏是否发生变化。如果没有发生变化，则说明是[Ajax](https://so.csdn.net/so/search?q=Ajax&spm=1001.2101.3001.7020)请求。
2. 在开发者模式下（F12），单击左上角小箭头，去在网页中找他的element，如果在element真实存在；在网页中单击右键，查看网页源代码，（ctrl+F）查找element中div的属性名，发现不存在，或者被注释掉了，则证明是一个Ajax请求。

![image-20231110154723886](Python%E7%88%AC%E8%99%AB.assets/image-20231110154723886.png)

![image-20231110154732950](Python%E7%88%AC%E8%99%AB.assets/image-20231110154732950.png)

### 案例

**以拉钩网招聘为例以POST方法获取数据**

获取图中数据集，此页面地址：[拉勾网招聘页面演示地址](https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput=) 

![img](Python%E7%88%AC%E8%99%AB.assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjUwNTc2,size_16,color_FFFFFF,t_70.png)

分析页面数据发现是ajax

 **找到Ajax请求数据体**

![在这里插入图片描述](Python%E7%88%AC%E8%99%AB.assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjUwNTc2,size_16,color_FFFFFF,t_70-16996048347592.png)

 **分析请求提构造**

![在这里插入图片描述](Python%E7%88%AC%E8%99%AB.assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjUwNTc2,size_16,color_FFFFFF,t_70-16996048347603.png)

![在这里插入图片描述](Python%E7%88%AC%E8%99%AB.assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjUwNTc2,size_16,color_FFFFFF,t_70-16996048347604.png)

 **模拟代码演示（requests）**

```python
def getData(city_quote):
    """
    通过post请求解析拉勾网对应城市的json数据集
    :param city_quote:
    :return:
    """
    url = "https://www.lagou.com/jobs/positionAjax.json"

    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "user_trace_token=20200301114810-40556cbd-ac17-4854-ae50-e5aacdaa9aab; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217094356904f1-0fb4889adf6cd1-4313f6b-2073600-17094356905660%22%2C%22%24device_id%22%3A%2217094356904f1-0fb4889adf6cd1-4313f6b-2073600-17094356905660%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1282471430.1583034493; LGUID=20200301114811-928d49c2-4465-439a-a16c-cef8b834998e; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABAGABFA87D814047DE2D9143FD964F13B5CF011; WEBTJ-ID=04252020%2C131057-171afbeee7a243-0ec1918b465381-7373667-2073600-171afbeee7c720; _gid=GA1.2.1088974098.1587791458; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586235118,1586925135,1587791458; X_MIDDLE_TOKEN=24ef3fd0e84859d0a3e459bed747ee45; X_HTTP_TOKEN=bdbd8729e637bc9f38740878512e3fbecc22034874; _gat=1; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20200425165304-fee9bb75-b8ee-4185-a4ba-bf572108bdba; PRE_SITE=; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587804804; LGRID=20200425165323-082cddcd-7423-4062-ab39-0b278dc1013e; SEARCH_ID=87417fff66354d1b9447aaaf07b17309",
        "origin": "https://www.lagou.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
        "referer": "https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput=",
    }
    data = {
        "first": "true",
        "pn": "1",
    }

    response = requests.post(url, data=data, headers=headers)
    print(response.json())
```

**运行结果**

```python
{'success': True, 'msg': None, 'code': 0, 'content': {'showId': 'd1f137337c3c4a70b331cd8a0e73c016', 'hrInfoMap': {'6803717': {'userId': 8733067, 'portrait': 'i/image3/M01/76/66/CgpOIF5we4CANS4qAACEOd1RoFw526.jpg', 'realName': 'muqianwen', 'positionName': '招聘HR', 'phone': None, 'receiveEmail': None, 'userLevel': 'G1', 'canTalk': True}, '7057096': {'userId': 418919, 'portrait': 'i/image2/M01/CE/15/CgotOVw4V1uAUpmqAADltxspyMM863.png', 'realName': 'HR', 'positionName': '', 'phone': None, 'receiveEmail': None, 'userLevel': 'G1', 'canTalk': True}, '6213467': {'userId': 14461756, 'portrait': 'i/image2/M01/6A/D6/CgotOV09IlGAPd6xAAcpgmuy6II576.png', 'realName': '马超', 'positionName': '理财规划师', 'phone': None, 'receiveEmail': None, 'userLevel': 'G1', 'canTal2020-05-03 12:43:23', 'formatCreateTime': '12:43发布', 'city': '郑州', 'district': None, 'businessZones': None, 'salary': '5k-10k', 'workYear': '不限', 'jobNature': '兼职', 'education': '不限', 'positionAdvantage': '工作轻松，简单易学上手快，佣金超高', 'imState': 'disabled', 'lastLogin': '2020-05-03 12:33:30', 'publisherId': 17211066, 'approve': 0, 'subwayline': None, 'stationname': None, 'linestaion': None, 'latitude': None, 'longitude': None, 'hitags': None, 'resumeProcessRate': 0, 'resumeProcessDay': 0, 'score': 1, 'newScore': 0.0, 'matchScore': 1.0, 'matchScoreExplain': None, 'query': None, 'explain': None, 'isSchoolJob': 0, 'adWord': 0, 'plus': None, 'pcShow': 0, 'appShow': 0, 'deliver': 0, 'gradeDescription': None, 'promotionScoreExplain': None, 'companySize': '少于15人', 'industryField': '消费生活', 'financeStage': '未融资', 'companyLabelList': [], 'firstType': '服务业', 'secondType': '百货|零售', 'thirdType': '西点师|面包糕点加工', 'skillLables': [], 'positionLables': ['其他'], .....
```

**以腾讯招聘为例GET方法获取json数据集**

获取图中数据集，此页面地址：[腾讯招聘技术类第一页](https://careers.tencent.com/search.html?pcid=40001)

![](Python%E7%88%AC%E8%99%AB.assets/image-20231110160123635.png)

**在开发者模式下, 网络选项中找到对应部分的数据请求（如下图，返回的数据与页面上看到的一样)**

<img src="Python%E7%88%AC%E8%99%AB.assets/image-20231110160027969.png" style="zoom:79%;" />

 **解析请求体的组成**

![](Python%E7%88%AC%E8%99%AB.assets/image-20231110160437183.png)

 **请求头部分解析**

![image-20231110160638874](Python%E7%88%AC%E8%99%AB.assets/image-20231110160638874.png)

 **使用requests模拟代码演示**

```python
# coding: utf8

import requests

def job_list_page():
    """
    职位类目下的具体列表
    :return: None
    """
    url = "https://careers.tencent.com/tencentcareer/api/post/Query"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "cookie": "pgv_pvi=9760113664; _ga=GA1.2.1166311162.1578063723; _gcl_au=1.1.294868577.1586227694; loading=agree",
        "referer": "https://careers.tencent.com/",
    }
    params = {
        "timestamp": "1588476060003",
        "parentCategoryId": "40001",
        "pageIndex": "1",
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn"
    }

    resp = requests.get(url, params=params, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    job_list_page()

```

## 结合js逆向方法

见[js逆向](..\逆向\js逆向.md)



