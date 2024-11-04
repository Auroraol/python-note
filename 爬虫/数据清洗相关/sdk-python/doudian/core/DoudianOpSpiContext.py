import json

from doudian.core.DoudianOpSpiResponse import DoudianOpSpiResponse


class DoudianOpSpiContext:
    def __init__(self):
        self.request = None
        self.response = DoudianOpSpiResponse()

    def getParamJson(self):
        return self.request.spiParam.paramJson

    def getParamJsonObject(self):
        paramJsonString = self.getParamJson()
        return json.loads(paramJsonString)

    def setResponseData(self, data):
        self.response.data = data

    def wrapSuccess(self):
        self.response.code = 0

    def wrapError(self, code, message=""):
        self.response.code = code
        self.response.message = message
