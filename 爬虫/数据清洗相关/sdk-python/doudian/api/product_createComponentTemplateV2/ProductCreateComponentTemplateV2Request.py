# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_createComponentTemplateV2.param.ProductCreateComponentTemplateV2Param import ProductCreateComponentTemplateV2Param


class ProductCreateComponentTemplateV2Request(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductCreateComponentTemplateV2Param()

	def getUrlPath(self, ):
		return "/product/createComponentTemplateV2"

	def getParams(self, ):
		return self.params



