# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.open_openId_replace.param.OpenOpenIdReplaceParam import OpenOpenIdReplaceParam


class OpenOpenIdReplaceRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OpenOpenIdReplaceParam()

	def getUrlPath(self, ):
		return "/open/openId/replace"

	def getParams(self, ):
		return self.params



