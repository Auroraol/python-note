# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_getCatePropertyV2.param.ProductGetCatePropertyV2Param import ProductGetCatePropertyV2Param


class ProductGetCatePropertyV2Request(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductGetCatePropertyV2Param()

	def getUrlPath(self, ):
		return "/product/getCatePropertyV2"

	def getParams(self, ):
		return self.params



