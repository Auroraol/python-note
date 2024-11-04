# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.antispam_orderQuery.param.AntispamOrderQueryParam import AntispamOrderQueryParam


class AntispamOrderQueryRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = AntispamOrderQueryParam()

	def getUrlPath(self, ):
		return "/antispam/orderQuery"

	def getParams(self, ):
		return self.params



