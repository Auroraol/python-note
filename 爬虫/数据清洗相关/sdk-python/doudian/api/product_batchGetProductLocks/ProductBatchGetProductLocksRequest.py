# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_batchGetProductLocks.param.ProductBatchGetProductLocksParam import ProductBatchGetProductLocksParam


class ProductBatchGetProductLocksRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductBatchGetProductLocksParam()

	def getUrlPath(self, ):
		return "/product/batchGetProductLocks"

	def getParams(self, ):
		return self.params



