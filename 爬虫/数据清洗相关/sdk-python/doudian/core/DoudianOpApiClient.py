import hashlib
import json
import threading
import time

from doudian.core.Constant import DOUDIAN_SDK_VERSION
from doudian.core.DoudianOpResponse import DoudianOpResponse
from doudian.core.http.DefaultHttpClient import DefaultHttpClient, HttpRequest
from doudian.exeception.DoudianOpException import DoudianOpException

log_key = "x-tt-logid"


def calsSign(appKey, appSecret, method, timestamp, sortedParamJson):
    patternString = appSecret + "app_key" + str(appKey) + "method" + method + "param_json" + sortedParamJson + "timestamp" + str(timestamp) + "v2" + appSecret
    print(patternString)
    return hashlib.md5(patternString.encode(encoding="utf-8")).hexdigest()


class DoudianOpApiClient:
    def __init__(self):
        self.httpClient = DefaultHttpClient()

    def request(self, request, accessToken):
        appKey = request.getConfig().appKey
        appSecret = request.getConfig().appSecret
        paramJsonObj = request.getParams()
        requestUrl = request.getConfig().openRequestUrl
        timestamp = int(time.time())
        method = request.getUrlPath()[1:].replace("/", ".")
        sortedParamJson = json.dumps(obj=paramJsonObj.__dict__, sort_keys=True, separators=(',', ':'), ensure_ascii=False, default=lambda obj: obj.__dict__)
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
            httpRequest.params["access_token"] = accessToken.getAccessToken()
        else:
            httpRequest.params["access_token"] = ""

        httpRequest.headers["from"] = "sdk"
        httpRequest.headers["sdk-type"] = "python"
        httpRequest.headers["sdk-version"] = DOUDIAN_SDK_VERSION
        httpRequest.headers["x-open-no-old-err-code"] = "1"

        log_id = threading.current_thread().__dict__.get(log_key, '')
        if log_id is not None and len(log_id) > 0:
            httpRequest.headers[log_key] = log_id

        httpResponse = self.httpClient.post(httpRequest)
        if httpResponse.statusCode != 200:
            raise DoudianOpException(DoudianOpException.HTTP_RESPONSE_STATUS_CODE_NOT_2XX)

        if len(httpResponse.body) == 0:
            return {}

        respMap = json.loads(httpResponse.body)
        opResp = DoudianOpResponse()
        opResp.__dict__ = respMap
        return opResp
