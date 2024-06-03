参考demo.py，设置相应的参数：

```python
#-*- coding: utf-8 -*-

import cartoon_cat as cc

if __name__ == '__main__':

    site = 'https://m.36mh.com/manhua/yiquanchaoren/'

    crawler = cc.CartoonCat(
        site=site,                                  # 漫画首页
        begin=0,                                    # 起始章节
        end=-1,                                     # 结束章节，为负数表明不设结束章节
        save_folder='/path/to/download',            # 保存路径，不存在会自动创建
        browser=cc.BrowserType.PHANTOMJS,           # 浏览器类型：FIREFOX，CHROME，SAFARI，IE，PHANTOMJS
        driver='path/to/phantomjs')                 # 驱动程序路径，firefox不需要
                                                    #   其他的可以从 https://pypi.python.org/pypi/selenium 下载
    crawler.start()

```

