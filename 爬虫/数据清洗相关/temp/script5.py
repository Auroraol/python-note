#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/24 16:37
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : script.py
from time import sleep

import requests
import json
from http.cookies import SimpleCookie
from tqdm import tqdm

if __name__ == '__main__':
    ###
    '''
    curl "https://4eac46eaaef34fe9.pdd4.myjjing.com/api/admin/goods/v2/list_v2" ^
      -H "Accept: application/json" ^
      -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" ^
      -H "Connection: keep-alive" ^
      -H "Content-Type: application/json" ^
      -H "Cookie: gr_user_id=12efe853-5ce6-4395-b9f7-cf6fb0e6e13d; sensorsdata2015jssdkcross=^%^7B^%^22^%^24device_id^%^22^%^3A^%^221761e2c1e5f88b-07b016474e5d41-c791e37-2073600-1761e2c1e6072e^%^22^%^7D; session_id_csm=MTY3MjEzMzM2N3xOd3dBTkZSSk1rczNOamRUTlU5U01rMU5Tak5TUlVwTlJGaERRMU5aV1RSSFdVUllXVTVaVms1WFdEWXlRVnBTUkRZelNsWkhRVkU9fIv-weijTeBmDcAehxzlCL-zKB6cytoyBwDBY1zJqVUg; Hm_lvt_103e9b51f831e7a08a4e57fae4d0fb05=1673253389; sa_jssdk_2015_3f516f31d69f7222_jd4_xiaoduoai_com=^%^7B^%^22distinct_id^%^22^%^3A^%^22^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj^%^22^%^2C^%^22first_id^%^22^%^3A^%^2218595ac91bd6ad-07106f3fd78bb18-26021151-2073600-18595ac91be76b^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^7D^%^2C^%^22identities^%^22^%^3A^%^22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1OTVhYzkxYmQ2YWQtMDcxMDZmM2ZkNzhiYjE4LTI2MDIxMTUxLTIwNzM2MDAtMTg1OTVhYzkxYmU3NmIiLCIkaWRlbnRpdHlfbG9naW5faWQiOiLoib7mvozlhYvvvIjljZfkuqzvvInnlJ^%^2Fniannp5HmioDmnInpmZDlhazlj7g6YXNrbmoifQ^%^3D^%^3D^%^22^%^2C^%^22history_login_id^%^22^%^3A^%^7B^%^22name^%^22^%^3A^%^22^%^24identity_login_id^%^22^%^2C^%^22value^%^22^%^3A^%^22^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj^%^22^%^7D^%^7D; isGoodsDetailBackGoodsList=false; source_data=^%^7B^%^22person^%^22:^%^22^%^E5^%^86^%^AF^%^E5^%^8D^%^9A^%^22^%^7D; xd-metadata=shop_id=63aa6a18ba26910015d0553d; sso_token=token:f478eb95cebb42d2ac4bb954ad058d8f; SID=2^|1:0^|10:1673434386^|3:SID^|44:ZjdkMmZhZmM3OTE5NDIxMDhmNDY0YTBkNWZmZDllNTg=^|7bdea4a0ade891a5dc543ca8cd75ec8e4bd96be8fe41a5bd4cf82d1e75309205; Hm_lpvt_103e9b51f831e7a08a4e57fae4d0fb05=1673434387; 934a89823bed3e05_gr_last_sent_sid_with_cs1=fd747257-336a-4669-9bd7-b4bf6a2a633d; 934a89823bed3e05_gr_last_sent_cs1=^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj; 934a89823bed3e05_gr_cs1=^%^E8^%^89^%^BE^%^E6^%^BE^%^8C^%^E5^%^85^%^8B^%^EF^%^BC^%^88^%^E5^%^8D^%^97^%^E4^%^BA^%^AC^%^EF^%^BC^%^89^%^E7^%^94^%^9F^%^E7^%^89^%^A9^%^E7^%^A7^%^91^%^E6^%^8A^%^80^%^E6^%^9C^%^89^%^E9^%^99^%^90^%^E5^%^85^%^AC^%^E5^%^8F^%^B8^%^3Aasknj; 934a89823bed3e05_gr_session_id=fd747257-336a-4669-9bd7-b4bf6a2a633d; 934a89823bed3e05_gr_session_id_fd747257-336a-4669-9bd7-b4bf6a2a633d=true" ^
      -H "Origin: https://3f516f31d69f7222.jd4.xiaoduoai.com" ^
      -H "Referer: https://3f516f31d69f7222.jd4.xiaoduoai.com/goods/list" ^
      -H "Sec-Fetch-Dest: empty" ^
      -H "Sec-Fetch-Mode: cors" ^
      -H "Sec-Fetch-Site: same-origin" ^
      -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36" ^
      -H "X-B3-Spanid: fc6545f4117343c7" ^
      -H "X-B3-Traceid: fc6545f4117343c70000001673434428" ^
      -H "XX-Platform: jdzy" ^
      -H "sec-ch-ua: ^\^"Not?A_Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"108^\^", ^\^"Google Chrome^\^";v=^\^"108^\^"" ^
      -H "sec-ch-ua-mobile: ?0" ^
      -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
      --data-raw "^{^\^"goods_category_id^\^":^\^"^\^",^\^"bound_to_chart^\^":^\^"all^\^",^\^"bound_to_activity^\^":^\^"^\^",^\^"keyword^\^":^\^"100003457272^\^",^\^"keyword_type^\^":^\^"plat_goods_id^\^",^\^"sort^\^":^\^"list_time_desc^\^",^\^"skip^\^":0,^\^"limit^\^":10,^\^"cid^\^":^\^"^\^",^\^"seller_cid^\^":^\^"^\^",^\^"status^\^":0^}" ^
      --compressed
    '''
    # c3e19b73c8c95e44.pdd4.myjjing.com 替换为店铺地址
    url = 'http://219b3c385a823369.pdd4.myjjing.com/api/admin/goods/v2/list_v2'
    # rawdata为token
    rawdata = 'source_data=%7B%22person%22:%22%E5%88%98%E4%B8%B0%E6%B4%81%22%7D; xd-metadata=shop_id=66e29a8543246d8d9e56ad13; sajssdk_2015_new_user_219b3c385a823369_pdd4_myjjing_com=1; sa_jssdk_2015_219b3c385a823369_pdd4_myjjing_com=%7B%22distinct_id%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AFJEANSWEST%E7%91%9E%E6%AC%A2%E7%91%B6%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd74578728430%22%2C%22first_id%22%3A%221923b7498741c0-0266f63cd26b2d-4c657b58-1328640-1923b749875197d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcustomer.xiaoduoai.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyM2I3NDk4NzQxYzAtMDI2NmY2M2NkMjZiMmQtNGM2NTdiNTgtMTMyODY0MC0xOTIzYjc0OTg3NTE5N2QiLCIkaWRlbnRpdHlfbG9naW5faWQiOiLnnJ%2Fnu7Tmlq9KRUFOU1dFU1TnkZ7mrKLnkbbkuJPljZblupc6cGRkNzQ1Nzg3Mjg0MzAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%E7%9C%9F%E7%BB%B4%E6%96%AFJEANSWEST%E7%91%9E%E6%AC%A2%E7%91%B6%E4%B8%93%E5%8D%96%E5%BA%97%3Apdd74578728430%22%7D%7D; isGoodsDetailBackGoodsList=false; SID=2|1:0|10:1727584439|3:SID|44:MjBjMWMxYzQ2ZjNiNGExYThlMWNkZmE1ZmViNzhlMjg=|de5c4035032aaa2d2f61f1584e10a4a2993b5fc68dc8d46b0b4375c380bf12bf'
    cookie_jar = SimpleCookie()
    cookie_jar.load(rawdata)
    cokies = {}
    for key, morsel in cookie_jar.items():
        cokies[key] = morsel.value

    f = open("29/json/product_ids_text4.json", 'r')
    goods_ids = json.load(f)
    # print(goods_ids)
    param = json.loads('''{
      "goods_category_id": "",
      "bound_to_chart": "all",
      "bound_to_activity": "",
      "keyword": "162371044481",
      "keyword_type": "link",
      "sort": "update_time_desc ",
      "skip": 0,
      "limit": 10,
      "cid": "",
      "seller_cid": "",
      "status": 0
    }''')
    flag = False  # 标志变量
    for goods_id in tqdm(goods_ids, desc='Processing'):
        param["keyword"] = str(goods_id)
        rsp = requests.post(url, json=param, cookies=cokies)
        j = rsp.json()
        if not flag:
            print(j)
            flag = True
        if rsp.status_code != 200:
            print(j)
            continue