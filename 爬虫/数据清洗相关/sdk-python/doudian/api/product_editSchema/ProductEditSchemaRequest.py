# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_editSchema.param.ProductEditSchemaParam import ProductEditSchemaParam


class ProductEditSchemaRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductEditSchemaParam()

	def getUrlPath(self, ):
		return "/product/editSchema"

	def getParams(self, ):
		return self.params



