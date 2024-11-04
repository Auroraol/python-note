# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_stockNum.param.SkuStockNumParam import SkuStockNumParam


class SkuStockNumRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuStockNumParam()

	def getUrlPath(self, ):
		return "/sku/stockNum"

	def getParams(self, ):
		return self.params



