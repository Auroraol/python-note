# BY @burpheart
# https://www.yuque.com/burpheart/phpaudit
# https://github.com/burpheart

import json
import os
import re
import urllib.parse

import requests

# 创建空列表
tset = []


# 保存
def save_page(sulg, book_id, path):
    '''
        定义了一个名为save_page的函数，它接受三个参数：book_id、sulg和path。
        这个函数使用requests库发送GET请求，下载指定URL的文档内容，并将其保存到指定的路径。
    '''
    docsdata = requests.get(
        'https://www.yuque.com/api/docs/' + sulg + '?book_id=' + book_id + '&merge_dynamic_data=false&mode=markdown')
    if (docsdata.status_code != 200):
        print("文档下载失败 页面可能被删除 ", book_id, sulg, docsdata.content)
        return
    docsjson = json.loads(docsdata.content)

    f = open(path, 'w', encoding='utf-8')
    f.write(docsjson['data']['sourcecode'])
    f.close()


def get_book(url="https://www.yuque.com/aceld/mo95lb/frv2c9"):
    docsdata = requests.get(url)
    """使用正则表达式模式decodeURIComponent\(\"(.+)\"\)\);来匹配满足以下条件的字符串：
        - 以decodeURIComponent("开头
        - 以");结尾
        - 中间包含一个或多个任意字符（使用(.+)表示）
    """
    data = re.findall(r"decodeURIComponent\(\"(.+)\"\)\);", docsdata.content.decode('utf-8'))

    docsjson = json.loads(urllib.parse.unquote(data[0]))  # 进行URL解码, 再将json转化成字典
    test = []
    dict = {}
    temp = {}  # 保存路径
    md = ""  # 保存路径
    """
    这行代码的作用是创建一个字符映射表（translation table），用于将字符串中的特定字符替换为指定的字符。

    具体来说，str.maketrans()函数接受两个参数，第一个参数是要被替换的字符，第二个参数是替换后的字符。在这行代码中，我们传递了两个字符串作为参数：

    - '\/:*?"<>|'：这是要被替换的字符集合，包括斜杠、反斜杠、冒号、星号、问号、双引号、小于号、大于号和竖线。
    - "___________"：这是替换后的字符，用下划线字符替换原始字符串中的特定字符。

    通过调用str.maketrans()函数，我们创建了一个字符映射表table，它将原始字符串中的特定字符映射为下划线字符。这个映射表可以在后续的代码中用于替换字符串中的特定字符。
            
    
    """
    table = str.maketrans('\/:*?"<>|' + "\n\r", "___________")  # windows操作系统中规定文件名中不能含有的符号是
    """
     '\/:*?"<>|'：这是要被替换的字符集合，包括斜杠、反斜杠、冒号、星号、问号、双引号、小于号、大于号和竖线。
     "___________"：这是替换后的字符，用下划线字符替换原始字符串中的特定字符。
    """
    prename = ""
    # 创建下载目录
    if (os.path.exists("download/" + str(docsjson['book']['id'])) == False):
        os.makedirs("download/" + str(docsjson['book']['id']))

    # 这段代码是用于生成目录结构的部分。它遍历docsjson['book']['toc']中的每个元素，并根据条件判断生成相应的目录项。
    for doc in docsjson['book']['toc']:
        # 文件夹
        if (doc['type'] == 'TITLE' or doc['child_uuid'] != ''):
            # 如果doc['type']等于'TITLE'或者doc['child_uuid']不为空
            filename = ''
            # 2. 将doc['title']和doc['parent_uuid']存储到dict[doc['uuid']]字典中，键为'0'和'1'。
            # 3. 将doc['uuid']作为键，初始化temp[doc['uuid']]为空字符串。
            dict[doc['uuid']] = {'0': doc['title'], '1': doc['parent_uuid']}  # 此dict非彼dict
            uuid = doc['uuid']  # 键及当前id
            temp[doc['uuid']] = ''  # 初始化temp[doc['uuid']]为空字符串  //文件夹路径
            while True:
                if (dict[uuid]['1'] != ''):
                    # 在循环中，如果dict[uuid]['1']不为空及doc['parent_uuid']，将执行以下操作
                    if temp[doc['uuid']] == '':
                        # 如果temp[doc['uuid']]为空，将doc['title']经过字符映射表table的替换后赋值给temp[doc['uuid']]。
                        temp[doc['uuid']] = doc['title'].translate(table)
                    else:
                        temp[doc['uuid']] = dict[uuid]['0'].translate(table) + '/' + temp[doc['uuid']]
                    uuid = dict[uuid]['1']  # 将dict[uuid]['1']及当前父id赋值给当前id，继续下一次循环
                else:
                    # doc['parent_uuid']为空表示是父目录
                    temp[doc['uuid']] = dict[uuid]['0'].translate(table) + '/' + temp[doc['uuid']]
                    break
            # 创建文件夹
            if ((os.path.exists("download/" + str(docsjson['book']['id']) + '/' + temp[doc['uuid']])) == False):
                os.makedirs("download/" + str(docsjson['book']['id']) + '/' + temp[doc['uuid']])

            # 创建目录  
            """
                如果temp[doc['uuid']]字符串以斜杠字符"/"结尾，表示当前目录项是一个文件夹。在Markdown格式中，使用##作为文件夹的标题，所以代码会将"## "和去除最后一个字符后的temp[doc['uuid']]字符串拼接起来，并添加到md字符串中。

                如果temp[doc['uuid']]字符串不以斜杠字符"/"结尾，表示当前目录项是一个文件。在Markdown格式中，使用*作为文件的列表项，所以代码会根据斜杠字符的数量来确定文件的缩进级别，然后将"* "和去除路径部分后的temp[doc['uuid']]字符串拼接起来，并添加到md字符串中。

                这段代码的作用是根据目录项的类型（文件夹或文件）和层级关系，生成相应的Markdown格式的目录项。
            """
            if (temp[doc['uuid']].endswith("/")):  # 是根文件夹
                """
                用于检查temp[doc['uuid']]字符串是否以斜杠字符"/"结尾。
                endswith()是字符串的一个方法，用于判断字符串是否以指定的后缀结尾，并返回布尔值。
                """
                md += "## " + temp[doc['uuid']][:-1] + "\n"
            else:  # 不是根文件夹, 通过\判断是几级的
                """
                具体来说，代码使用temp[doc['uuid']].count("/") - 1计算斜杠字符的数量减去1，
                然后使用" " * (temp[doc['uuid']].count("/") - 1)生成对应数量的空格作为缩进。
                接着，使用temp[doc['uuid']][temp[doc['uuid']].rfind("/") + 1:]获取
                最后一个斜杠字符后面的部分作为目录项的标题。最后，将缩进和标题拼接起来，并添加到md字符串中。
                """
                md += "  " * (temp[doc['uuid']].count("/") - 1) + "* " + temp[doc['uuid']][
                                                                         temp[doc['uuid']].rfind("/") + 1:] + "\n"
        # .md                                                                
        if (doc['url'] != ''):
            # 表示是一个md文件
            if doc['parent_uuid'] != "":
                if (temp[doc['parent_uuid']].endswith("/")):  # 以/结尾表示是根文件夹
                    md += " " * temp[doc['parent_uuid']].count("/") + "* [" + doc['title'] + "](" + urllib.parse.quote(
                        temp[doc['parent_uuid']] + "/" + doc['title'].translate(table) + '.md') + ")" + "\n"
                else:
                    md += "  " * temp[doc['parent_uuid']].count("/") + "* [" + doc['title'] + "](" + urllib.parse.quote(
                        temp[doc['parent_uuid']] + "/" + doc['title'].translate(table) + '.md') + ")" + "\n"  # 进行url 编码
                # 保存 传入 sulg 和 book_id
                save_page(doc['url'], str(docsjson['book']['id']),
                          "download/" + str(docsjson['book']['id']) + '/' + temp[doc['parent_uuid']] + "/" + doc[
                              'title'].translate(table) + '.md')
            else:
                md += " " + "* [" + doc['title'] + "](" + urllib.parse.quote(
                    doc['title'].translate(table) + '.md') + ")" + "\n"
                # 保存    
                save_page(doc['url'], str(docsjson['book']['id']),
                          "download/" + str(docsjson['book']['id']) + "/" + doc[
                              'title'].translate(table) + '.md')
    # 把上述得到的目录生成一个摘要                       
    f = open("download/" + str(docsjson['book']['id']) + '/' + "/SUMMARY.md", 'w', encoding='utf-8')
    f.write(md)
    f.close()


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     get_book(sys.argv[1])
    # else:
    #     get_book()
    dict = ["https://www.yuque.com/xiaoyulive/frontend/echarts", "https://www.yuque.com/xiaoyulive/vscode",
            "https://www.yuque.com/xiaoyulive/uniapp/bfn5o2", "https://www.yuque.com/xiaoyulive/cicd/gr55wu",
            "https://www.yuque.com/xiaoyulive/kubernetes/xui5av", "https://www.yuque.com/xiaoyulive/docker/qlh70b",
            "https://www.yuque.com/xiaoyulive/flutter/twcg6y", "https://www.yuque.com/xiaoyulive/typescript/euxhdb"
        , "https://www.yuque.com/xiaoyulive/dart/lbk8fr", "https://www.yuque.com/xiaoyulive/flutter",
            "https://www.yuque.com/xiaoyulive/linux/uuhcbp#sed"]
    for url in dict:
        get_book(url)
