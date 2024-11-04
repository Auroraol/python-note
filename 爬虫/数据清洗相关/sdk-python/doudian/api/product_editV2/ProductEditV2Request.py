# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_editV2.param.ProductEditV2Param import ProductEditV2Param


class ProductEditV2Request(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductEditV2Param()

	def getUrlPath(self, ):
		return "/product/editV2"

	def getParams(self, ):
		return self.params



