#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/14 15:54
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : test.py

import pandas as pd
from collections import OrderedDict
if __name__ == '__main__':
    # 读取两个 CSV 文件
    df_output = pd.read_csv('output (1).csv', header=None)
    df_dy_shop2 = pd.read_csv('dy_shop.csv', header=None)

    list_output = df_output[0].tolist()  # 获取第一列数据并转换为 list
    list_dy_shop2 = df_dy_shop2[0].tolist()  # 获取第一列数据并转换为 list

    # 使用集合来存储商品ID，自动去重
    product_ids = set(list_dy_shop2)

    # 遍历 list_output 中的元素，找出不在 list_dy_shop2 中的元素
    unique_to_output = [item for item in list_output if item not in product_ids]

    # 将结果保存到新的 DataFrame
    df_unique = pd.DataFrame(unique_to_output, columns=['Unique Data'])

    # 保存为 CSV 文件
    df_unique.to_csv('unique_to_output12.csv', index=False)

    # # 转换为集合进行差集操作
    # set_output = set(df_output[0])
    # set_dy_shop2 = set(df_dy_shop2[0])
    #
    # # 求差集：df_output 中有而 df_dy_shop2 中没有的值
    # diff_set = set_output - set_dy_shop2
    #
    # # 将差集转换回 DataFrame
    # df_diff = pd.DataFrame(list(diff_set), columns=[0])
    #
    # # 保存结果
    # df_diff.to_csv('filtered_diff.csv', index=False, header=False)