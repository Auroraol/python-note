#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/14 15:59
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : test2.py

import pandas as pd
import re

import chardet
import json



if __name__ == '__main__':

    # 读取 filtered_output.csv 文件
    df_filtered = pd.read_csv('unique_to_output11.csv')

    for d in df_filtered:
        print(d)

    # 检测文件编码
    with open('unique_to_output11.csv', 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    # 使用检测到的编码读取文件
    plat_user_ids = []
    with open('unique_to_output11.csv', 'r', encoding=encoding) as file:
        for line in file:
            data = json.loads(line.strip())
            plat_user_ids.append(data['plat_user_id'])

    print(plat_user_ids)


    # # 定义一个函数来判断是否包含中文字符
    # def contains_chinese(text):
    #     return bool(re.search(r'[\u4e00-\u9fa5]', str(text)))
    #
    # # 过滤掉包含中文字符的行
    # df_no_chinese = df_filtered[~df_filtered.apply(lambda row: row.astype(str).apply(contains_chinese).any(), axis=1)]
    #
    # # 将过滤后的结果写入新的 CSV 文件
    # df_no_chinese.to_csv('unique_to_output_no_chinese.csv', index=False)