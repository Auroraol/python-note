# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.token_refresh.param.TokenRefreshParam import TokenRefreshParam


class TokenRefreshRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = TokenRefreshParam()

	def getUrlPath(self, ):
		return "/token/refresh"

	def getParams(self, ):
		return self.params



