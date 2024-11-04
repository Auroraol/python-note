# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_addV2.param.ProductAddV2Param import ProductAddV2Param


class ProductAddV2Request(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductAddV2Param()

	def getUrlPath(self, ):
		return "/product/addV2"

	def getParams(self, ):
		return self.params



