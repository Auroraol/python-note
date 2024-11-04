from doudian.api.token.RefreshTokenParam import RefreshTokenParam
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest


class RefreshTokenRequest(DoudianOpApiRequest):
    def __init__(self):
        DoudianOpApiRequest.__init__(self)
        self.params = RefreshTokenParam()

    def getParams(self):
        return self.params

    def getUrlPath(self):
        return "/token/refresh"
