# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_editComponentTemplate.param.ProductEditComponentTemplateParam import ProductEditComponentTemplateParam


class ProductEditComponentTemplateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductEditComponentTemplateParam()

	def getUrlPath(self, ):
		return "/product/editComponentTemplate"

	def getParams(self, ):
		return self.params



