# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_getComponentTemplate.param.ProductGetComponentTemplateParam import ProductGetComponentTemplateParam


class ProductGetComponentTemplateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductGetComponentTemplateParam()

	def getUrlPath(self, ):
		return "/product/getComponentTemplate"

	def getParams(self, ):
		return self.params



