# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_datchDelComponentTemplate.param.ProductDatchDelComponentTemplateParam import ProductDatchDelComponentTemplateParam


class ProductDatchDelComponentTemplateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductDatchDelComponentTemplateParam()

	def getUrlPath(self, ):
		return "/product/datchDelComponentTemplate"

	def getParams(self, ):
		return self.params



