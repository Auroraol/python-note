# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_list.param.SkuListParam import SkuListParam


class SkuListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuListParam()

	def getUrlPath(self, ):
		return "/sku/list"

	def getParams(self, ):
		return self.params



