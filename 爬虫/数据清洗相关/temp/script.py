#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/24 16:37
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : script.py
import concurrent
from time import sleep

import requests
import json
from http.cookies import SimpleCookie
from tqdm import tqdm
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

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

    # 遍历商品 ID 并发送请求
    flag = False  # 标志变量
    for goods_id in tqdm(goods_ids, desc='Processing'):
        param = param_template.copy()  # 复制模板，避免修改原始字典
        param["keyword"] = str(goods_id)

        try:
            rsp = requests.post(url, json=param, cookies=cookies)
            rsp.raise_for_status()  # 如果响应状态码不是 200，将引发异常

            j = rsp.json()
            if not flag:
                print(j)
                flag = True
            if rsp.status_code != 200:
                print(j)
                continue
        except requests.RequestException as e:
            print(f"Error fetching details for {goods_id}: {e}")


def generate_configurations(urls, rawdata_list, product_ids_files):
    return [
        {
            'url': url,
            'rawdata': rawdata,
            'product_ids_file': product_ids_file
        }
        for url, rawdata, product_ids_file in zip(urls, rawdata_list, product_ids_files)
    ]

def genUrl(url):
    return 'https://' + url + '/api/admin/goods/v2/list_v2',

def list_files_in_directory(directory_path):
    path = Path(directory_path)
    return [file for file in path.iterdir() if file.is_file()]

def fetch_product_details_Thread(url, rawdata, product_ids_file):
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

    def fetch_detail(goods_id):
        param = param_template.copy()  # 复制模板，避免修改原始字典
        param["keyword"] = str(goods_id)

        try:
            rsp = requests.post(url, json=param, cookies=cookies)
            rsp.raise_for_status()  # 如果响应状态码不是 200，将引发异常

            j = rsp.json()
            return j, goods_id
        except requests.RequestException as e:
            print(f"Error fetching details for {goods_id}: {e}")
            return None, goods_id

    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:  # 使用线程池
        futures = {executor.submit(fetch_detail, goods_id): goods_id for goods_id in goods_ids}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(goods_ids), desc='Processing'):
            result, goods_id = future.result()
            if result:
                results.append(result)

    return results

if __name__ == '__main__':
    urls = [
        # genUrl('8230f937d0f0cb8d.pdd4.myjjing.com'),
        # genUrl('20c5e337118d89bb.pdd4.myjjing.com'),
        '',
        '',
        genUrl('24f88b55e30abde4.pdd4.myjjing.com'),
        genUrl('d5b785b1b2a22b6a.pdd4.myjjing.com'),
        genUrl('410abd2fd6506415.pdd4.myjjing.com'),
        genUrl('e85a391ec0e8742f.pdd4.myjjing.com'),
        genUrl('e7b4a2d055d8d378.pdd4.myjjing.com'),
        genUrl('7030d5ac4149d4f1.pdd4.myjjing.com'),
    ]

    rawdata_list = [
        '',
        '',
        # "source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727321429|3:SID|44:Y2Q3MjM3OGZmYjdmNGZiYTkxNWY4MzkxMGJlYjZjZmY=|2753c919cb972b4ca8e20dc7dc0242671e53c764d5cf223a969139672a09b5e9; xd-metadata=shop_id=66e262d90ce282fbabf87f47; sajssdk_2015_new_user_8230f937d0f0cb8d_pdd4_myjjing_com=1; sa_jssdk_2015_8230f937d0f0cb8d_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22MINISO%E5%90%8D%E5%88%9B%E4%BC%98%E5%93%81%E5%A5%B3%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd32121130053%22%2C%22first_id%22%3A%221922c615a4256a-00fd42cab168b7b8-4c657b58-1328640-1922c615a431162%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM2MTVhNDI1NmEtMDBmZDQyY2FiMTY4YjdiOC00YzY1N2I1OC0xMzI4NjQwLTE5MjJjNjE1YTQzMTE2MiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6Ik1JTklTT%2BWQjeWIm%2BS8mOWTgeWls%2BijheaXl%2BiIsOW6lzpwZGQzMjEyMTEzMDA1MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22MINISO%E5%90%8D%E5%88%9B%E4%BC%98%E5%93%81%E5%A5%B3%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd32121130053%22%7D%7D; isGoodsDetailBackGoodsList=false"        ,
        # 'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727321965|3:SID|44:OTE3Yjk2MmU2NzAwNDdhNmFjODhiZmQ5OTMzODg0MjY=|f9c6fabfb5f694695fb30dcaf9642c4c6811a5d3ad47895da9db3bba418020e4; xd-metadata=shop_id=66e26253e1ad0366fb91ac11; sajssdk_2015_new_user_20c5e337118d89bb_pdd4_myjjing_com=1; sa_jssdk_2015_20c5e337118d89bb_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E6%A3%89%E8%87%B4%E6%9C%8D%E9%A5%B0%E6%97%97%E8%88%B0%E5%BA%97%3Apdd66024768662%22%2C%22first_id%22%3A%221922c6988c5581-0190f618dcd02bd-4c657b58-1328640-1922c6988c612db%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM2OTg4YzU1ODEtMDE5MGY2MThkY2QwMmJkLTRjNjU3YjU4LTEzMjg2NDAtMTkyMmM2OTg4YzYxMmRiIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoi5qOJ6Ie05pyN6aWw5peX6Iiw5bqXOnBkZDY2MDI0NzY4NjYyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E6%A3%89%E8%87%B4%E6%9C%8D%E9%A5%B0%E6%97%97%E8%88%B0%E5%BA%97%3Apdd66024768662%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727322847|3:SID|44:ZjM0ZTAyNTRiZmFlNDVjMWI4ZDRhYWMzNmMwNzU0ODI=|bfff95d7f51df4dcfb4c8ddb6b945052e367a16550f3c3c059a76dec3db072ed; xd-metadata=shop_id=66e261f5ec34072abf957cef; sajssdk_2015_new_user_24f88b55e30abde4_pdd4_myjjing_com=1; sa_jssdk_2015_24f88b55e30abde4_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22MH%E4%BC%91%E9%97%B2%E6%9C%8D%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd73516935517%22%2C%22first_id%22%3A%221922c76fbce1109-04e9748451c05e8-4c657b58-1328640-1922c76fbcf180a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM3NmZiY2UxMTA5LTA0ZTk3NDg0NTFjMDVlOC00YzY1N2I1OC0xMzI4NjQwLTE5MjJjNzZmYmNmMTgwYSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6Ik1I5LyR6Zey5pyN6KOF5peX6Iiw5bqXOnBkZDczNTE2OTM1NTE3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22MH%E4%BC%91%E9%97%B2%E6%9C%8D%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd73516935517%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727323063|3:SID|44:YTkzYWJhNjE1OTk3NGM0MzliOTM3NWViNmZhY2U3ODM=|ca1420b73ea3b13101fb80fecd020dfc756dd0c77fc51c332539c3290a7bdd57; xd-metadata=shop_id=66e260731534e4887e798977; sajssdk_2015_new_user_d5b785b1b2a22b6a_pdd4_myjjing_com=1; sa_jssdk_2015_d5b785b1b2a22b6a_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E6%A3%89%E8%87%B4%E4%BC%91%E9%97%B2%E5%A5%B3%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd15854995958%22%2C%22first_id%22%3A%221922c7a47c560c-0a12d28f229ffe-4c657b58-1328640-1922c7a47c61427%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM3YTQ3YzU2MGMtMGExMmQyOGYyMjlmZmUtNGM2NTdiNTgtMTMyODY0MC0xOTIyYzdhNDdjNjE0MjciLCIkaWRlbnRpdHlfbG9naW5faWQiOiLmo4noh7TkvJHpl7LlpbPoo4Xml5foiLDlupc6cGRkMTU4NTQ5OTU5NTgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E6%A3%89%E8%87%B4%E4%BC%91%E9%97%B2%E5%A5%B3%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd15854995958%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727323130|3:SID|44:MWE5MmJjODFhMTJhNDY1N2JlNTdlZTA4ZmQzZjRjNzY=|31039e5ca62a8aa0e6d6b3e7f1bdf2f3c5a31dafb84c755bba61513b49610ba9; xd-metadata=shop_id=66e25a0cec34072abf957c82; sajssdk_2015_new_user_410abd2fd6506415_pdd4_myjjing_com=1; sa_jssdk_2015_410abd2fd6506415_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E5%94%90%E7%8B%AETONLION%E4%BC%91%E9%97%B2%E6%97%97%E8%88%B0%E5%BA%97%3Apdd79787070310%22%2C%22first_id%22%3A%221922c7b5108581-0fc656aaf295e08-4c657b58-1328640-1922c7b510913a9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM3YjUxMDg1ODEtMGZjNjU2YWFmMjk1ZTA4LTRjNjU3YjU4LTEzMjg2NDAtMTkyMmM3YjUxMDkxM2E5IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoi5ZSQ54uuVE9OTElPTuS8kemXsuaXl%2BiIsOW6lzpwZGQ3OTc4NzA3MDMxMCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E5%94%90%E7%8B%AETONLION%E4%BC%91%E9%97%B2%E6%97%97%E8%88%B0%E5%BA%97%3Apdd79787070310%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727323207|3:SID|44:NTFjODFmM2U2ZTI5NDdlYThkZDIyZDFlNmI5Y2RiM2Y=|35e732eb0056d5dc652abbc4a9c49f9799c2305834f44f8d00d6def16639e366; xd-metadata=shop_id=66e258e08ca0b4d92db3dbe0; sajssdk_2015_new_user_e85a391ec0e8742f_pdd4_myjjing_com=1; sa_jssdk_2015_e85a391ec0e8742f_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AF%E6%97%B6%E5%B0%9A%E6%9C%8D%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd48765617634%22%2C%22first_id%22%3A%221922c7c7993581-03ae6397364a4e8-4c657b58-1328640-1922c7c79941072%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM3Yzc5OTM1ODEtMDNhZTYzOTczNjRhNGU4LTRjNjU3YjU4LTEzMjg2NDAtMTkyMmM3Yzc5OTQxMDcyIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoi55yf57u05pav5pe25bCa5pyN6KOF5peX6Iiw5bqXOnBkZDQ4NzY1NjE3NjM0In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AF%E6%97%B6%E5%B0%9A%E6%9C%8D%E8%A3%85%E6%97%97%E8%88%B0%E5%BA%97%3Apdd48765617634%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727323273|3:SID|44:MjU0OTZjODQwYzQ0NDY3Mjk0ZGYzODJmNGYyYjBlMTk=|c51f30d4c19c45778ac5e0c2f95ae7efe13ec477381ba409b2131761cfc25ed1; xd-metadata=shop_id=66e257b6fb399789cf525ba9; sajssdk_2015_new_user_e7b4a2d055d8d378_pdd4_myjjing_com=1; sa_jssdk_2015_e7b4a2d055d8d378_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AF%E6%97%B6%E5%B0%9A%E8%BF%90%E5%8A%A8%E6%97%97%E8%88%B0%E5%BA%97%3Apdd78523750645%22%2C%22first_id%22%3A%221922c7d7ac19bc-07069a1775381dc-4c657b58-1328640-1922c7d7ac2157c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM3ZDdhYzE5YmMtMDcwNjlhMTc3NTM4MWRjLTRjNjU3YjU4LTEzMjg2NDAtMTkyMmM3ZDdhYzIxNTdjIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoi55yf57u05pav5pe25bCa6L%2BQ5Yqo5peX6Iiw5bqXOnBkZDc4NTIzNzUwNjQ1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AF%E6%97%B6%E5%B0%9A%E8%BF%90%E5%8A%A8%E6%97%97%E8%88%B0%E5%BA%97%3Apdd78523750645%22%7D%7D; isGoodsDetailBackGoodsList=false',
        'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727323320|3:SID|44:NzAwMjE2NDAwY2JjNDJlY2E0YWEzZGE0ZDc1NDI5NzE=|1413c3db94bedbaac2513a3dc8f1cde169473ef5ce1988450b0a0e58413c878d; xd-metadata=shop_id=66e24fee1f769b89aeeb7fea; sajssdk_2015_new_user_7030d5ac4149d4f1_pdd4_myjjing_com=1; sa_jssdk_2015_7030d5ac4149d4f1_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E6%A3%89%E8%87%B4%E6%97%B6%E5%B0%9A%E4%BC%91%E9%97%B2%E6%97%97%E8%88%B0%E5%BA%97%3Apdd32475143029%22%2C%22first_id%22%3A%221922c7e31a1c1-02be0d10394f6f-4c657b58-1328640-1922c7e31a21292%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMmM3ZTMxYTFjMS0wMmJlMGQxMDM5NGY2Zi00YzY1N2I1OC0xMzI4NjQwLTE5MjJjN2UzMWEyMTI5MiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IuajieiHtOaXtuWwmuS8kemXsuaXl%2BiIsOW6lzpwZGQzMjQ3NTE0MzAyOSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E6%A3%89%E8%87%B4%E6%97%B6%E5%B0%9A%E4%BC%91%E9%97%B2%E6%97%97%E8%88%B0%E5%BA%97%3Apdd32475143029%22%7D%7D'
    ]

    directory_path = 'josn'  #
    all_files = list_files_in_directory(directory_path)
    product_ids_files = all_files  # 文件路径列表


    # 生成配置字典集合
    configs = generate_configurations(urls, rawdata_list, product_ids_files)

    # 打印生成的配置
    for config in configs:
        print(config)






    #
    # # Example usage
    # url = 'https://3429e1616b24ea55.pdd4.myjjing.com/api/admin/goods/v2/list_v2'
    # rawdata = 'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=...; ...'
    # product_ids_file = "product_ids_text5.json"
    #
    # fetch_product_details(url, rawdata, product_ids_file)

    # ###
    # '''
    # curl "https://4eac46eaaef34fe9.pdd4.myjjing.com/api/admin/goods/v2/list_v2" ^
    #   -H "Accept: application/json" ^
    #   -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" ^
    #   -H "Connection: keep-alive" ^
    #   -H "Content-Type: application/json" ^
    #   -H "Cookie: gr_user_id=12efe853-5ce6-4395-b9f7-cf6fb0e6e13d; sensorsdata2015jssdkcross=^%^7B^%^22^%^24device_id^%^22^%^3A^%^221761e2c1e5f88b-07b016474e5d41-c791e37-2073600-1761e2c1e6072e^%^22^%^7D; session_id_csm=MTY3MjEzMzM2N3xOd3dBTkZSSk1rczNOamRUTlU5U01rMU5Tak5TUlVwTlJGaERRMU5aV1RSSFdVUllXVTVaVms1WFdEWXlRVnBTUkRZelNsWkhRVkU9fIv-weijTeBmDcAehxzlCL-zKB6cytoyBwDBY1zJqVUg; Hm_lvt_103e9b51f831e7a08a4e57fae4d0fb05=1673253389; sa_jssdk_2015_3f516f31d69f7222_jd4_xiaoduoai_com=^%^7B^%^22distinct_id^%^22^%^3A^%^22^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj^%^22^%^2C^%^22first_id^%^22^%^3A^%^2218595ac91bd6ad-07106f3fd78bb18-26021151-2073600-18595ac91be76b^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^7D^%^2C^%^22identities^%^22^%^3A^%^22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1OTVhYzkxYmQ2YWQtMDcxMDZmM2ZkNzhiYjE4LTI2MDIxMTUxLTIwNzM2MDAtMTg1OTVhYzkxYmU3NmIiLCIkaWRlbnRpdHlfbG9naW5faWQiOiLoib7mvozlhYvvvIjljZfkuqzvvInnlJ^%^2Fniannp5HmioDmnInpmZDlhazlj7g6YXNrbmoifQ^%^3D^%^3D^%^22^%^2C^%^22history_login_id^%^22^%^3A^%^7B^%^22name^%^22^%^3A^%^22^%^24identity_login_id^%^22^%^2C^%^22value^%^22^%^3A^%^22^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj^%^22^%^7D^%^7D; isGoodsDetailBackGoodsList=false; source_data=^%^7B^%^22person^%^22:^%^22^%^E5^%^86^%^AF^%^E5^%^8D^%^9A^%^22^%^7D; xd-metadata=shop_id=63aa6a18ba26910015d0553d; sso_token=token:f478eb95cebb42d2ac4bb954ad058d8f; SID=2^|1:0^|10:1673434386^|3:SID^|44:ZjdkMmZhZmM3OTE5NDIxMDhmNDY0YTBkNWZmZDllNTg=^|7bdea4a0ade891a5dc543ca8cd75ec8e4bd96be8fe41a5bd4cf82d1e75309205; Hm_lpvt_103e9b51f831e7a08a4e57fae4d0fb05=1673434387; 934a89823bed3e05_gr_last_sent_sid_with_cs1=fd747257-336a-4669-9bd7-b4bf6a2a633d; 934a89823bed3e05_gr_last_sent_cs1=^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj; 934a89823bed3e05_gr_cs1=^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj; 934a89823bed3e05_gr_session_id=fd747257-336a-4669-9bd7-b4bf6a2a633d; 934a89823bed3e05_gr_session_id_fd747257-336a-4669-9bd7-b4bf6a2a633d=true" ^
    #   -H "Origin: https://3f516f31d69f7222.jd4.xiaoduoai.com" ^
    #   -H "Referer: https://3f516f31d69f7222.jd4.xiaoduoai.com/goods/list" ^
    #   -H "Sec-Fetch-Dest: empty" ^
    #   -H "Sec-Fetch-Mode: cors" ^
    #   -H "Sec-Fetch-Site: same-origin" ^
    #   -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36" ^
    #   -H "X-B3-Spanid: fc6545f4117343c7" ^
    #   -H "X-B3-Traceid: fc6545f4117343c70000001673434428" ^
    #   -H "XX-Platform: jdzy" ^
    #   -H "sec-ch-ua: ^\^"Not?A_Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"108^\^", ^\^"Google Chrome^\^";v=^\^"108^\^"" ^
    #   -H "sec-ch-ua-mobile: ?0" ^
    #   -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
    #   --data-raw "^{^\^"goods_category_id^\^":^\^"^\^",^\^"bound_to_chart^\^":^\^"all^\^",^\^"bound_to_activity^\^":^\^"^\^",^\^"keyword^\^":^\^"100003457272^\^",^\^"keyword_type^\^":^\^"plat_goods_id^\^",^\^"sort^\^":^\^"list_time_desc^\^",^\^"skip^\^":0,^\^"limit^\^":10,^\^"cid^\^":^\^"^\^",^\^"seller_cid^\^":^\^"^\^",^\^"status^\^":0^}" ^
    #   --compressed
    # '''
    # # c3e19b73c8c95e44.pdd4.myjjing.com 替换为店铺地址
    # url = 'https://3429e1616b24ea55.pdd4.myjjing.com/api/admin/goods/v2/list_v2'
    # # rawdata为token
    # rawdata = 'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; SID=2|1:0|10:1727256436|3:SID|44:MTRiYWY5YjM1MTM2NGYxZjg2MjljYWFlMjg3ZWYxNjU=|0b4a6e4b64251aaa3ce41060c05c4869391b7a50ceefd33853c143b9544bf046; xd-metadata=shop_id=66e25bb71506315b67321ede; sajssdk_2015_new_user_3429e1616b24ea55_pdd4_myjjing_com=1; sa_jssdk_2015_3429e1616b24ea55_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22GENIO%20LAMODE%E7%94%B3%E6%B4%BE%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd17248883539%22%2C%22first_id%22%3A%221922881a7e47b9-00988be78f10a53-4c657b58-1327104-1922881a7e5a53%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMjg4MWE3ZTQ3YjktMDA5ODhiZTc4ZjEwYTUzLTRjNjU3YjU4LTEzMjcxMDQtMTkyMjg4MWE3ZTVhNTMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJHRU5JTyBMQU1PREXnlLPmtL7kuJPljZblupc6cGRkMTcyNDg4ODM1MzkifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22GENIO%20LAMODE%E7%94%B3%E6%B4%BE%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd17248883539%22%7D%7D; isGoodsDetailBackGoodsList=false'
    # cookie_jar = SimpleCookie()
    # cookie_jar.load(rawdata)
    # cokies = {}
    # for key, morsel in cookie_jar.items():
    #     cokies[key] = morsel.value
    #
    # f = open("product_ids_text5.json", 'r')
    # goods_ids = json.load(f)
    # # print(goods_ids)
    # param = json.loads('''{
    #   "goods_category_id": "",
    #   "bound_to_chart": "all",
    #   "bound_to_activity": "",
    #   "keyword": "162371044481",
    #   "keyword_type": "link",
    #   "sort": "update_time_desc ",
    #   "skip": 0,
    #   "limit": 10,
    #   "cid": "",
    #   "seller_cid": "",
    #   "status": 0
    # }''')
    # for goods_id in tqdm(goods_ids, desc='Processing'):
    #     param["keyword"] = str(goods_id)
    #     rsp = requests.post(url, json=param, cookies=cokies)
    #     j = rsp.json()
    #     # print(j)
    #     if rsp.status_code != 200:
    #         print(j)
    #         continue