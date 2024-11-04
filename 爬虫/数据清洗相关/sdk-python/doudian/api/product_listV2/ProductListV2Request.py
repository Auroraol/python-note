# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_listV2.param.ProductListV2Param import ProductListV2Param


class ProductListV2Request(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductListV2Param()

	def getUrlPath(self, ):
		return "/product/listV2"

	def getParams(self, ):
		return self.params



