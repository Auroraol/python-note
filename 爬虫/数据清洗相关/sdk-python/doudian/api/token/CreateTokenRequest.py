from doudian.api.token.CreateTokenParam import CreateTokenParam
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest


class CreateTokenRequest(DoudianOpApiRequest):

    def __init__(self):
        DoudianOpApiRequest.__init__(self)
        self.params = CreateTokenParam()

    def getParams(self):
        return self.params

    def getUrlPath(self):
        return "/token/create"
