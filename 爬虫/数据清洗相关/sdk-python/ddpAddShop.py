#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/11/5 11:43
# @Author  : IngDao
# @Email   : 1665834268@qq.com
# @File    : ddpAddShop.py


# 数据推送，添加数据推送店铺(已授权)
import json
import threading
import time

import requests

from doudian.core.Constant import DOUDIAN_SDK_VERSION
from doudian.core.DoudianOpApiClient import log_key, calsSign
from doudian.core.DoudianOpResponse import DoudianOpResponse
from doudian.core.http.DefaultHttpClient import HttpRequest
from doudian.exeception.DoudianOpException import DoudianOpException


def request(request, accessToken):
    appKey = request.appKey
    appSecret = request.appSecret
    paramJsonObj = request.getParams()
    requestUrl = request.openRequestUrl
    timestamp = int(time.time())
    method = request.getUrlPath()[1:].replace("/", ".")
    sortedParamJson = json.dumps(paramJsonObj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, default=lambda obj: obj.__dict__)

    sign = calsSign(appKey, appSecret, method, timestamp, sortedParamJson)

    httpRequest = HttpRequest()
    httpRequest.host = requestUrl
    httpRequest.path = request.getUrlPath()
    httpRequest.useHttps = request.getConfig().useHttps
    httpRequest.body = sortedParamJson
    httpRequest.params["app_key"] = appKey
    httpRequest.params["method"] = method
    httpRequest.params["sign"] = sign
    httpRequest.params["timestamp"] = timestamp
    httpRequest.params["v"] = 2
    if accessToken is not None:
        httpRequest.params["access_token"] = accessToken
    else:
        httpRequest.params["access_token"] = ""

    httpRequest.headers["from"] = "sdk"
    httpRequest.headers["sdk-type"] = "python"
    httpRequest.headers["sdk-version"] = DOUDIAN_SDK_VERSION
    httpRequest.headers["x-open-no-old-err-code"] = "1"

    log_id = threading.current_thread().__dict__.get(log_key, '')
    if log_id is not None and len(log_id) > 0:
        httpRequest.headers[log_key] = log_id

    httpResponse = httpClient.post(httpRequest)
    if httpResponse.statusCode != 200:
        raise DoudianOpException(DoudianOpException.HTTP_RESPONSE_STATUS_CODE_NOT_2XX)

    if len(httpResponse.body) == 0:
        return {}

    respMap = json.loads(httpResponse.body)
    opResp = DoudianOpResponse()
    opResp.__dict__ = respMap
    return opResp


class Request:
    def __init__(self, appKey, appSecret, openRequestUrl):
        self.appKey = appKey
        self.appSecret = appSecret
        self.openRequestUrl = openRequestUrl

    def getParams(self):
        # Return parameters as a dictionary or custom object
        return {
            "param1": "value1",
            "param2": "value2"
        }

    def getUrlPath(self):
        # Example URL path, this will be part of the method
        return "/api/v1/resource"


if __name__ == '__main__':
    req = Request(appKey="6891458366200186375", appSecret="02f11349-4d31-4f73-9361-6a3e81c2818f",
                  openRequestUrl="/openCloud/ddpGetShopList ")
    accessToken = "9947115y5ep-1gcw23vsdf2870000smg02u"

    payload = request(req, accessToken)
    print(payload)
    #
    # url = "https://op.jinritemai.com/captain/charge/getApiCallRecord?"
    #
    # # 自定义请求头
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    #     'Cookie': "csrf_session_id=25c252bbaaaf6be05d2ebb5fbd96cf74; x-jupiter-uuid=17288744533943404; passport_csrf_token=4f15ec9feb9725794ea85606ecaf174b; passport_csrf_token_default=4f15ec9feb9725794ea85606ecaf174b; s_v_web_id=verify_m28fazxf_6291d2bd_6cf3_772e_a46b_605de816f7a6; odin_tt=d9eb11558aefa5e72ff006f0620377c0af373000670fa0d8cc024ad2ffda2d107857526fca6f7280c2f4686b5341f163e3e002d72bb854f9099dc30b1e95494a; uid_tt_op=c8005ad7edae12e217b4599f128d728d; uid_tt_ss_op=c8005ad7edae12e217b4599f128d728d; sid_tt_op=68fda269a22072e2202266088a2cac6a; sessionid_op=68fda269a22072e2202266088a2cac6a; sessionid_ss_op=68fda269a22072e2202266088a2cac6a; is_staff_user_op=false; store-region=cn-sc; store-region-src=uid; need_choose_shop=0; op_session=a5ec510219b8a61fcf498da0058863c2:7274478cf99a21f4e8d1c8efdf9bcb701631f313a7dd4908f488f1819977dda6; ttwid=1%7C98va07-1WyGGKSM4VLD1f-BbHPFwcX-4CQJox48LzGo%7C1728887380%7Ccf163e028e309d1cd6aaef93ae8e7217950ed442cfeb682d16acc5d2772018f1; ucas_c0_op=CkEKBTEuMC4wEIqIiOD2ya6GZxjBPiC7oIDk44xaKL8-ML704Kjy9PUEQNT0srgGSNSo77oGUIS8kaKkue-xYViHARIUx8zLfJSyNsaxUtLDdOSJUelezW4; ucas_c0_ss_op=CkEKBTEuMC4wEIqIiOD2ya6GZxjBPiC7oIDk44xaKL8-ML704Kjy9PUEQNT0srgGSNSo77oGUIS8kaKkue-xYViHARIUx8zLfJSyNsaxUtLDdOSJUelezW4; sid_guard_op=68fda269a22072e2202266088a2cac6a%7C1728887380%7C5184000%7CFri%2C+13-Dec-2024+06%3A29%3A40+GMT; sid_ucp_v1_op=1.0.0-KDQyNTM3YjllNDBlNTQ1MTFjOTZmZTdhMjAzOTY3MWEwYzQ2MzZmNDAKGQi-9OCo8vT1BBDU9LK4BhiwISAMOAFA6wcaAmxmIiA2OGZkYTI2OWEyMjA3MmUyMjAyMjY2MDg4YTJjYWM2YQ; ssid_ucp_v1_op=1.0.0-KDQyNTM3YjllNDBlNTQ1MTFjOTZmZTdhMjAzOTY3MWEwYzQ2MzZmNDAKGQi-9OCo8vT1BBDU9LK4BhiwISAMOAFA6wcaAmxmIiA2OGZkYTI2OWEyMjA3MmUyMjAyMjY2MDg4YTJjYWM2YQ"
    # }
    #
    #
    # data = {"date": ts, "pageNo": 1, "pageSize": 10, "appId": "6891458366200186375"}
    #
    # # 发送 POST 请求
    # response = requests.post(url, headers=headers, data=data)
    #
    # res = response.json()
