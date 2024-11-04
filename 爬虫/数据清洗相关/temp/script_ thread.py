#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/24 16:37
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : script.py
import concurrent
from itertools import islice
from time import sleep

import requests
import json
from http.cookies import SimpleCookie
from tqdm import tqdm
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

from main import save_to_json, extract_product_ids


def generate_configurations(urls, rawdata_list, product_ids_files):
    return [
        {
            'url': url,
            'rawdata': rawdata,
            'product_ids_file': product_ids_file
        }
        for url, rawdata, product_ids_file in zip(urls, rawdata_list, product_ids_files)
    ]


def gen_url(url):
    return 'http://' + url + '/api/admin/goods/v2/list_v2'


def list_files_in_directory(directory_path):
    path = Path(directory_path)
    return [file for file in path.iterdir() if file.is_file()]


def fetch_product_details(url, rawdata, product_ids_file):
    # 解析 cookie
    cookie_jar = SimpleCookie()
    cookie_jar.load(rawdata)
    cookies = {key: morsel.value for key, morsel in cookie_jar.items()}

    # 读取商品 ID
    with open(product_ids_file, 'r') as f:
        goods_ids = json.load(f)

    # 请求参数模板
    param_template = {
        "goods_category_id": "",
        "bound_to_chart": "all",
        "bound_to_activity": "",
        "keyword": "",  # 将在循环中更新
        "keyword_type": "link",
        "sort": "update_time_desc",
        "skip": 0,
        "limit": 10,
        "cid": "",
        "seller_cid": "",
        "status": 0
    }
    results = []  # 用于保存请求的结果
    flag = False  # 标志变量
    for goods_id in tqdm(goods_ids, desc='Processing'):
        param_template["keyword"] = str(goods_id)
        rsp = requests.post(url, json=param_template, cookies=cookies)
        j = rsp.json()
        if not flag:
            print(j)
            results.append(url)  # 保存结果
            flag = True
        if rsp.status_code != 200:
            print(j)
            continue


def fetch_product_details2(url, rawdata, product_ids_file):
    # 解析 cookie
    cookie_jar = SimpleCookie()
    cookie_jar.load(rawdata)
    cookies = {key: morsel.value for key, morsel in cookie_jar.items()}

    # 读取商品 ID
    with open(product_ids_file, 'r') as f:
        goods_ids = json.load(f)

    # 请求参数模板
    param_template = {
        "goods_category_id": "",
        "bound_to_chart": "all",
        "bound_to_activity": "",
        "keyword": "",  # 将在循环中更新
        "keyword_type": "link",
        "sort": "update_time_desc",
        "skip": 0,
        "limit": 10,
        "cid": "",
        "seller_cid": "",
        "status": 0
    }

    results = []  # 用于保存请求的结果
    flag = False  # 标志变量
    for goods_id in tqdm(goods_ids, desc='Processing'):
        param_template["keyword"] = str(goods_id)
        rsp = requests.post(url, json=param_template, cookies=cookies)
        j = rsp.json()
        if not flag:
            print(j)
            # 检查 goodss 是否为空
            goodss = j.get('data', {}).get('goodss', [])
            if not goodss:
                results.append(url)  # 保存结果
            flag = True
        if rsp.status_code != 200:
            print(j)
            continue
    return results


def fetch_product_details_thread(configs):
    results = []

    # 为每个配置运行 fetch_product_details
    with ThreadPoolExecutor(max_workers=len(configs)) as executor:
        futures = {
            executor.submit(fetch_product_details, config['url'], config['rawdata'],
                            config['product_ids_file']): config
            for config in islice(configs, 0, None)}  # 忽略前两条 #不忽略填0

        for future in tqdm(concurrent.futures.as_completed(futures), total=len(configs), desc='Processing Configs'):
            config = futures[future]
            try:
                result = future.result()
                results.append((config, result))
            except Exception as e:
                print(f"Error processing config {config}: {e}")

    return results


if __name__ == '__main__':

    directory_path = '29'  # 替换为你的目录路径
    output_path = '29/json'

    all_files = list_files_in_directory(directory_path)
    file_paths = all_files  # 文件路径列表
    # for file_path in file_paths:
    #     str_id = file_path.stem  # 获取文件名，不包括扩展名
    #     json_output_path = f'{output_path}/product_ids_{str_id}.json'
    #
    #     unique_product_ids = extract_product_ids(file_path)
    #     save_to_json(unique_product_ids, json_output_path)
    #
    #     print(f"商品ID已保存到 {json_output_path}")

    # url
    urls = [
        gen_url('b9fc97c24c9c1d23.pdd4.myjjing.com'), #回力
        gen_url('36a938d1cd9ef0cc.pdd4.myjjing.com'), #巨麦
        gen_url('2e143caaf0acfea1.pdd4.myjjing.com'), #逅莱
        gen_url('219b3c385a823369.pdd4.myjjing.com'), #瑞欢瑶
        gen_url('8c9654706e67f925.pdd4.myjjing.com'), #GENIO LAMODE服饰箱包旗舰店
    ]

    # token
    rawdata_list = [
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727573967|3:SID|44:Y2JkZjg3ZjRlOWUxNDk5NmI5MGUzZjJjNzA3OTQyMTc=|e70e821c356056eb8e163fdbda6752334886367fe0fc8e61fb7ae2649f56c94d; xd-metadata=shop_id=66e295c224d6a8feed793bc9; sajssdk_2015_new_user_b9fc97c24c9c1d23_pdd4_myjjing_com=1; sa_jssdk_2015_b9fc97c24c9c1d23_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E5%9B%9E%E5%8A%9B%E9%9F%AC%E5%AE%A2%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd81609676878%22%2C%22first_id%22%3A%221923b6ecfb939e-063f47b54599e18-4c657b58-1328640-1923b6ecfbabb1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyM2I2ZWNmYjkzOWUtMDYzZjQ3YjU0NTk5ZTE4LTRjNjU3YjU4LTEzMjg2NDAtMTkyM2I2ZWNmYmFiYjEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiLlm57lipvpn6zlrqLkuJPljZblupc6cGRkODE2MDk2NzY4NzgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E5%9B%9E%E5%8A%9B%E9%9F%AC%E5%AE%A2%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd81609676878%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727574194|3:SID|44:MmM2NWU1NDVkYTc4NDY1OWE2Mzc5NzBjNThlYzA5NDM=|4154ae1ebcb8e518d65aff8c3bf8d83cffcdc4a0d2dc8edc16fe85cc560c7c72; xd-metadata=shop_id=66e28a983aa1060379793cdb; sajssdk_2015_new_user_36a938d1cd9ef0cc_pdd4_myjjing_com=1; sa_jssdk_2015_36a938d1cd9ef0cc_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22GENIO%20LAMODE%E5%B7%A8%E9%BA%A6%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd25265349746%22%2C%22first_id%22%3A%221923b7246f6ea4-01d5166786133e7-4c657b58-1328640-1923b7246f710c3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyM2I3MjQ2ZjZlYTQtMDFkNTE2Njc4NjEzM2U3LTRjNjU3YjU4LTEzMjg2NDAtMTkyM2I3MjQ2ZjcxMGMzIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiR0VOSU8gTEFNT0RF5beo6bqm5LiT5Y2W5bqXOnBkZDI1MjY1MzQ5NzQ2In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22GENIO%20LAMODE%E5%B7%A8%E9%BA%A6%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd25265349746%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727574298|3:SID|44:YjUxYzdjNjJhNjQ1NDhjZWI2MzE5MDZhOTEwYTZkYmE=|d8c959f4c9eb8b7f1e9462ca8b29691c9cda981fa44f910327b0ff794cb64719; xd-metadata=shop_id=66e28f89d0c22ab5195a8b9d; sajssdk_2015_new_user_2e143caaf0acfea1_pdd4_myjjing_com=1; sa_jssdk_2015_2e143caaf0acfea1_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AFJEANSWEST%E9%80%85%E8%8E%B1%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd77812446064%22%2C%22first_id%22%3A%221923b73d9c5fd8-0dea045abdc525-4c657b58-1328640-1923b73d9c61c2b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyM2I3M2Q5YzVmZDgtMGRlYTA0NWFiZGM1MjUtNGM2NTdiNTgtMTMyODY0MC0xOTIzYjczZDljNjFjMmIiLCIkaWRlbnRpdHlfbG9naW5faWQiOiLnnJ%2Fnu7Tmlq9KRUFOU1dFU1TpgIXojrHkuJPljZblupc6cGRkNzc4MTI0NDYwNjQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AFJEANSWEST%E9%80%85%E8%8E%B1%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd77812446064%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727574346|3:SID|44:MjBjMWMxYzQ2ZjNiNGExYThlMWNkZmE1ZmViNzhlMjg=|653fa366842b58454101ad5b84174a16e0fb499a0a11493bf8969b4ed660e83d; xd-metadata=shop_id=66e29a8543246d8d9e56ad13; sajssdk_2015_new_user_219b3c385a823369_pdd4_myjjing_com=1; sa_jssdk_2015_219b3c385a823369_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AFJEANSWEST%E7%91%9E%E6%AC%A2%E7%91%B6%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd74578728430%22%2C%22first_id%22%3A%221923b7498741c0-0266f63cd26b2d-4c657b58-1328640-1923b749875197d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyM2I3NDk4NzQxYzAtMDI2NmY2M2NkMjZiMmQtNGM2NTdiNTgtMTMyODY0MC0xOTIzYjc0OTg3NTE5N2QiLCIkaWRlbnRpdHlfbG9naW5faWQiOiLnnJ%2Fnu7Tmlq9KRUFOU1dFU1TnkZ7mrKLnkbbkuJPljZblupc6cGRkNzQ1Nzg3Mjg0MzAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AFJEANSWEST%E7%91%9E%E6%AC%A2%E7%91%B6%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd74578728430%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727574463|3:SID|44:OTEwYTk1YjU1YmI5NDI2ZGJkNjVjMDYwMzI3MzRkYzM=|74701207c39ce98211027b1830ffbe504db50dd1ce573b768b6ffaeeda32ae27; xd-metadata=shop_id=66e28a9dff95c28cf35a8d52; sajssdk_2015_new_user_8c9654706e67f925_pdd4_myjjing_com=1; sa_jssdk_2015_8c9654706e67f925_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22GENIO%20LAMODE%E6%9C%8D%E9%A5%B0%E7%AE%B1%E5%8C%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd75718305043%22%2C%22first_id%22%3A%221923b76620140d-0cd0a9aef36da28-4c657b58-1328640-1923b766202dec%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyM2I3NjYyMDE0MGQtMGNkMGE5YWVmMzZkYTI4LTRjNjU3YjU4LTEzMjg2NDAtMTkyM2I3NjYyMDJkZWMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJHRU5JTyBMQU1PREXmnI3ppbDnrrHljIXml5foiLDlupc6cGRkNzU3MTgzMDUwNDMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22GENIO%20LAMODE%E6%9C%8D%E9%A5%B0%E7%AE%B1%E5%8C%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd75718305043%22%7D%7D; isGoodsDetailBackGoodsList=false'
    ]

    # json
    all_files = list_files_in_directory(directory_path)
    product_ids_files = all_files  # 文件路径列表

    # 生成配置字典集合
    configs = generate_configurations(urls, rawdata_list, product_ids_files)
    for c in  configs:
        print(c)

    res = fetch_product_details_thread(configs)
    # for r in res:
    #     print(f"成功url: {r}")
