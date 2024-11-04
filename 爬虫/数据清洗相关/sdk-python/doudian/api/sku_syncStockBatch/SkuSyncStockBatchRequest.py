# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_syncStockBatch.param.SkuSyncStockBatchParam import SkuSyncStockBatchParam


class SkuSyncStockBatchRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuSyncStockBatchParam()

	def getUrlPath(self, ):
		return "/sku/syncStockBatch"

	def getParams(self, ):
		return self.params



