# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_syncStockBatchMultiProducts.param.SkuSyncStockBatchMultiProductsParam import SkuSyncStockBatchMultiProductsParam


class SkuSyncStockBatchMultiProductsRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuSyncStockBatchMultiProductsParam()

	def getUrlPath(self, ):
		return "/sku/syncStockBatchMultiProducts"

	def getParams(self, ):
		return self.params



