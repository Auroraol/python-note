import json
import os
import re
import urllib.parse
import urllib.parse

import requests


def save_page(sulg, book_id, file_path):
    '''
    定义了一个名为save_page的函数，它接受三个参数：book_id、sulg和path。
    这个函数使用requests库发送GET请求，下载指定URL的文档内容，并将其保存到指定的路径。
    '''
    url = 'https://www.yuque.com/api/docs/' + sulg + '?book_id=' + book_id + '&merge_dynamic_data=false&mode=markdown'
    docsdata = requests.get(url)
    if (docsdata.status_code != 200):
        print("文档下载失败 页面可能被删除 ", book_id, sulg, docsdata.content)
        return

    docsjson = json.loads(docsdata.content)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(docsjson['data']['sourcecode'])


# 将生成目录结构的逻辑封装在一个名为generate_directory_structure的函数
def generate_directory_structure(docsjson):
    md = ""
    dict = {}
    temp = {}  # 路径
    table = str.maketrans('\\/:*?"<>|', '_________')  # windows操作系统中规定文件名中不能含有的符号是, 出现了用_________替换

    def generate_md_link(title, url):
        return f"* [{title}]({urllib.parse.quote(url)})\n"

    def generate_md_folder(title):
        return f"## {title}\n"

    def generate_md_file(title, indent_level):
        return f"{'  ' * indent_level}* {title}\n"

    for doc in docsjson['book']['toc']:
        if doc['type'] == 'TITLE' or doc['child_uuid'] != '':
            filename = ''
            dict[doc['uuid']] = {'0': doc['title'], '1': doc['parent_uuid']}
            uuid = doc['uuid']
            temp[doc['uuid']] = ''
            while True:
                if dict[uuid]['1'] != '':
                    if temp[doc['uuid']] == '':
                        temp[doc['uuid']] = doc['title'].translate(table)
                    else:
                        temp[doc['uuid']] = dict[uuid]['0'].translate(table) + '/' + temp[doc['uuid']]
                    uuid = dict[uuid]['1']
                else:
                    temp[doc['uuid']] = dict[uuid]['0'].translate(table) + '/' + temp[doc['uuid']]
                    break

            folder_path = os.path.join("download", str(docsjson['book']['id']), temp[doc['uuid']])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            if doc['url'] != '':
                if doc['parent_uuid'] != '':
                    parent_folder_path = temp[doc['parent_uuid']]
                    if parent_folder_path.endswith("/"):
                        md += " " * parent_folder_path.count("/") + generate_md_link(doc['title'],
                                                                                     os.path.join(parent_folder_path,
                                                                                                  doc[
                                                                                                      'title'].translate(
                                                                                                      table) + '.md'))
                    else:
                        md += "  " * parent_folder_path.count("/") + generate_md_link(doc['title'],
                                                                                      os.path.join(parent_folder_path,
                                                                                                   doc[
                                                                                                       'title'].translate(
                                                                                                       table) + '.md'))
                    save_page(doc['url'], str(docsjson['book']['id']),
                              os.path.join(folder_path, doc['title'].translate(table) + '.md'))
                else:
                    md += " " + generate_md_link(doc['title'], doc['title'].translate(table) + '.md')
                    save_page(doc['url'], str(docsjson['book']['id']),
                              os.path.join(folder_path, doc['title'].translate(table) + '.md'))

    summary_file_path = os.path.join("download", str(docsjson['book']['id']), "SUMMARY.md")
    with open(summary_file_path, 'w', encoding='utf-8') as f:
        f.write(md)


def get_book(url="https://www.yuque.com/aceld/mo95lb/frv2c9"):
    docs_data = requests.get(url)
    """
    使用正则表达式模式decodeURIComponent\(\"(.+)\"\)\);来匹配满足以下条件的字符串：
        - 以decodeURIComponent("开头
        - 以");结尾
        - 中间包含一个或多个任意字符（使用(.+)表示）
    """
    data = re.findall(r"decodeURIComponent\(\"(.+)\"\)\);", docs_data.content.decode('utf-8'))
    docs_json = json.loads(urllib.parse.unquote(data[0]))  # 进行URL解码, 再将json转化成字典

    generate_directory_structure(docs_json)


if __name__ == '__main__':
    get_book('https://www.yuque.com/yuque/developer/api')
