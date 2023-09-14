# -*- coding: utf-8 -*-
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.request as urllib2
import logging
import os
from os import path as osp


class Enum(tuple):
    __getattr__ = tuple.index


BrowserType = Enum(['FIREFOX', 'CHROME', 'IE', 'SAFARI', 'PHANTOMJS'])


class CartoonCat:
    def __init__(self, site, begin=0, end=-1, save_folder="download", browser=BrowserType.FIREFOX, driver=None):
        """
        :param site: 漫画的首页面
        :param begin: 章节的开始(含),0表示第一章
        :param end: 章节的结束(含),-1表示到结尾
        :param browser: 浏览器类型
        :param driver: 驱动，如果驱动程序在可访问的位置，这个参数非必须，对于PhantomJs，驱动程序就是改程序的地址
        """

        self.__site = site
        self.__begin = begin
        self.__end = end
        self.__save_folder = save_folder
        self.__chapter_list = []
        self.___not_under_list = []

        if not osp.exists(self.__save_folder):
            os.mkdir(self.__save_folder)

        # 初始化支持的浏览器
        if BrowserType.FIREFOX == browser:
            self.__browser = webdriver.Firefox()
        elif BrowserType.CHROME == browser:
            self.__browser = webdriver.Chrome()
        elif BrowserType.IE == browser:
            self.__browser = webdriver.Ie(driver)
        elif BrowserType.SAFARI == browser:
            self.__browser = webdriver.Safari(driver)
        elif BrowserType.PHANTOMJS == browser:
            self.__browser = webdriver.PhantomJS(driver)
        else:
            raise TypeError('UNKNOWN BROWSER TYPE: %s' % browser)

        self.__get_chapter_list()

        if self.__begin >= len(self.__chapter_list) \
                or (0 <= self.__end < self.__begin):
            raise Exception('Chapter start and end indexes are illegal')

        #日志格式
        logging.basicConfig(format='[%(asctime)s] %(levelname)s::%(module)s::%(funcName)s() %(message)s', level=logging.INFO)

    def __del__(self):
        self.__browser.quit() # 关闭浏览器

    def __get_chapter_list(self):
        """
        获取章节信息
        :return: None
        """
        # 初始化浏览器
        self.__browser.get(self.__site)
        # 使用xpath获取所有li标签
        li_elements = self.__browser.find_elements_by_xpath('//div[@id="content"]/li')
        li_elements.reverse()  # 原本的章节是倒叙的

        # 遍历每个li标签
        for li in li_elements:
            # 获取文本内容
            # text = li.text
            # print(text)
            # 获取href属性的值
            href = li.find_element_by_tag_name('a').get_attribute('href')
            # 获取tit1e属性的值
            title = li.find_element_by_tag_name('a').get_attribute('title')
            print("href:", href)
            print("title:", title)
            # 储存章节的信息,元素的text和href属性分别就是章节的名称和地址
            # 向列表中添加列表元素
            self.__chapter_list.append([title, href])

        # # 使用 find_elements_by_xpath 获取所有的 <tr> 元素
        # tr_elements = self.__browser.find_elements_by_xpath('/html/body/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/fieldset/table/tbody/tr')
        #
        # # 遍历 tr_elements
        # for tr in tr_elements:
        #     # 获取当前 tr 元素下的所有 td 元素
        #     td_elements = tr.find_elements_by_xpath('./td')
        #     # 遍历 td_elements, 从索引 1 开始
        #     for i, td in enumerate(td_elements[1:], start=1):
        #         # 查找 td 元素下的 <a> 元素
        #         a_element = td.find_element_by_xpath('./a')
        #
        #         # 获取 <a> 元素的 href 属性和文本内容
        #         href = a_element.get_attribute('href')
        #         text = a_element.text
        #
        #         # 打印 href 和文本内容
        #         # print(f'Tr {tr_elements.index(tr)}, TD {i}')
        #         print('href:', href)
        #         print('text:', text)
        #         # 向列表中添加列表元素
        #         self.__chapter_list.append([text, href])


    def get_chapter_list(self):
        """
        得到章节信息,章节的名称和地址
        :return:章节信息
        """
        return self.__chapter_list


    @staticmethod
    def __download(url, save_path, try_time=3, timeout=30):
        """
        下载
        :param url:
        :param save_path:
        :param try_time:
        :param timeout:
        :return:
        """
        while try_time > 0:
            try:
                content = urllib2.urlopen(url, timeout=timeout).read()
                with open(save_path, 'wb') as fp:
                    fp.write(content)
                break
            except Exception as et:
                logging.error(et, exc_info=True)
                try_time -= 1
                if try_time == 0:
                    logging.error('cannot download: %s to %s' % (url, save_path))

    def findSnapshot(self):
        # 创建子文档,参数:父级目录,子目录名称
        save_folder = osp.join(self.__save_folder, "chapter_title")
        if not osp.exists(save_folder):
            os.mkdir(save_folder)
        self.__browser.get("https://www.cartoonmad.com/comic/122100012051001.html")

        """
        < img
        src = "comicpic.asp?file=/1221/001/001&amp;rimg=1"
        border = "0"
        oncontextmenu = "return false"
        onload = "if(this.width>screen.width-176) {this.resized=true; this.width=screen.width*0.98-180;}" >
        不能直接下载
        """
        # 执行截屏
        self.__browser.save_screenshot('screenshot.png')

        # 使用Pillow库打开截图文件
        screenshot = Image.open('screenshot.png')

        # 获取图片元素位置和大小
        element = self.__browser.find_element_by_css_selector('img[src="comicpic.asp?file=/1221/001/001&rimg=1')  # 使用CSS选择器定位图片元素
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        # 从截图中裁剪所需的图片部分
        image = screenshot.crop((left, top, right, bottom))  # 裁剪图片
        image.save('cropped_image.png')  # 保存裁剪后的图片

    def findClick(self):
        # 找到下一页链接元素
        next_page_link = self.__browser.find_element_by_link_text('下一页')
        return next_page_link

    def findDownload(self):
        image_div = self.__browser.find_element_by_css_selector('#mhpic')
        image_url = image_div.get_attribute('src')
        return image_url
    
    def download_chapter(self, chapter_idx, save_folder=None):
        """
        下载章节
        :param chapter_idx: 章节id
        :param save_folder: 保存路径
        :return:
        """
        if chapter_idx <  174:
            return
        chapter = self.__chapter_list[chapter_idx]

        save_folder = save_folder if save_folder is not None else self.__save_folder  #保存目录

        # 标题 url
        chapter_title = chapter[0]
        chapter_url = chapter[1]

        logging.info('#### START DOWNLOAD CHAPTER %d %s ####' % (chapter_idx, chapter_title))

        #创建子文档,参数:父级目录,子目录名称
        save_folder = osp.join(save_folder, chapter_title)
        if not osp.exists(save_folder):
            os.mkdir(save_folder)

        # 初始化浏览器, 请求chapter_url
        image_idx = 1  #图片数量id
        self.__browser.get(chapter_url)  #请求当前页面
        # 隐式等待，确保动态内容节点被完全加载出来
        self.__browser.implicitly_wait(10)

        while True:
            try:
                image_url = self.findDownload()
                save_image_name = osp.join(save_folder,('%05d' % image_idx) + '.' + osp.basename(image_url).split('.')[-1])  # 取名字保存
                self.__download(image_url, save_image_name)  # 下载
            except NoSuchElementException:
                self.___not_under_list.append(chapter_idx)
                break

            try:
                # 通过模拟点击加载下一页
                # 找到下一页链接元素
                next_page_link = self.findClick()
                # 检查是否存在下一页链接元素
                if next_page_link:
                    # 存在下一页链接元素，进行点击操作
                    next_page_link.click()
                else:
                    # 退出循环
                    break
            except NoSuchElementException:
                # 处理找不到下一页链接元素的情况，退出循环
                break

            # 页面结束不是html结尾，可用于判断章节是否爬取完。
            # if not self.__browser.current_url.endswith('html'):
            #     break
            image_idx += 1

        logging.info('#### DOWNLOAD CHAPTER COMPLETE ####')

    # 显示没下载的
    def show(self):
        for name in self.___not_under_list:
            print(name)

    def start(self):
        begin = self.__begin if self.__begin >= 0 else 0
        end = self.__end if self.__end >= 0 else len(self.__chapter_list)

        #遍历下载所以章节
        for chapter_idx in range(begin, end):
            self.download_chapter(chapter_idx)
