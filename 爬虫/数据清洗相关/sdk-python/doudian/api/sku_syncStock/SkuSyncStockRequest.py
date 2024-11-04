# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_syncStock.param.SkuSyncStockParam import SkuSyncStockParam


class SkuSyncStockRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuSyncStockParam()

	def getUrlPath(self, ):
		return "/sku/syncStock"

	def getParams(self, ):
		return self.params



