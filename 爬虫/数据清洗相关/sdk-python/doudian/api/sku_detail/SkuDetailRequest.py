# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_detail.param.SkuDetailParam import SkuDetailParam


class SkuDetailRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuDetailParam()

	def getUrlPath(self, ):
		return "/sku/detail"

	def getParams(self, ):
		return self.params



