# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.open_getAuthInfo.param.OpenGetAuthInfoParam import OpenGetAuthInfoParam


class OpenGetAuthInfoRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OpenGetAuthInfoParam()

	def getUrlPath(self, ):
		return "/open/getAuthInfo"

	def getParams(self, ):
		return self.params



