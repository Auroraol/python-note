# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_addSchema.param.ProductAddSchemaParam import ProductAddSchemaParam


class ProductAddSchemaRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductAddSchemaParam()

	def getUrlPath(self, ):
		return "/product/addSchema"

	def getParams(self, ):
		return self.params



