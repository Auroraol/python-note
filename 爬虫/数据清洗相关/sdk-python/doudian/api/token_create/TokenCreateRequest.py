# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.token_create.param.TokenCreateParam import TokenCreateParam


class TokenCreateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = TokenCreateParam()

	def getUrlPath(self, ):
		return "/token/create"

	def getParams(self, ):
		return self.params



