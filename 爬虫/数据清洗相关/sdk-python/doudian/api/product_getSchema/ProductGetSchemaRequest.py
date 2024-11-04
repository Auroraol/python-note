# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_getSchema.param.ProductGetSchemaParam import ProductGetSchemaParam


class ProductGetSchemaRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductGetSchemaParam()

	def getUrlPath(self, ):
		return "/product/getSchema"

	def getParams(self, ):
		return self.params



