import hashlib
import hmac
import json

from doudian.core.DoudianOpConfig import GlobalConfig
from doudian.core.DoudianOpSpiContext import DoudianOpSpiContext
from doudian.core.DoudianOpSpiParam import DoudianOpSpiParam


class DoudianOpSpiRequest:
    def __init__(self):
        self.spiParam = DoudianOpSpiParam()
        self.bizHandler = None

    def init(self, appKey, timestamp, sign, signV2, signMethod, paramJson):
        self.spiParam.appKey = appKey
        self.spiParam.timestamp = timestamp
        self.spiParam.sign = sign
        self.spiParam.signV2 = signV2
        self.spiParam.signMethod = signMethod
        self.spiParam.paramJson = paramJson

    def registerHandler(self, bizHandler):
        self.bizHandler = bizHandler

    def execute(self, parseAsJsonString=True):
        context = DoudianOpSpiContext()
        context.request = self

        appKey = GlobalConfig.appKey
        appSecret = GlobalConfig.appSecret
        signMethod = self.spiParam.signMethod
        remoteSign = self.spiParam.sign
        remoteSignV2 = self.spiParam.signV2
        paramJson = self.spiParam.paramJson
        timestamp = self.spiParam.timestamp

        # 校验签名
        sign = self.calcSign(appKey, appSecret, paramJson, signMethod, timestamp)
        if sign != remoteSign and sign != remoteSignV2:
            context.wrapError(100001)
            if parseAsJsonString:
                return json.dumps(context.response, default=lambda obj: obj.__dict__)
            return context.response

        # 处理业务逻辑
        self.bizHandler(context)

        if parseAsJsonString:
            return json.dumps(context.response, default=lambda obj: obj.__dict__)
        return context.response

    def getParam(self):
        pass

    def calcSign(self, appKey, appSecret, paramJson, signMethod, timestamp):
        paramJsonObj = json.loads(paramJson)
        sortedParamJson = json.dumps(obj=paramJsonObj, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=False)
        paramPattern = "app_key" + appKey + "param_json" + sortedParamJson + "timestamp" + timestamp
        signPattern = appSecret + paramPattern + appSecret
        if signMethod == "hmac-sha256":
            return hmac.new(appSecret.encode("utf-8"), signPattern.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
        else:
            return hashlib.md5(signPattern.encode("utf-8")).hexdigest()
