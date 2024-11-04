# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_qualificationConfig.param.ProductQualificationConfigParam import ProductQualificationConfigParam


class ProductQualificationConfigRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductQualificationConfigParam()

	def getUrlPath(self, ):
		return "/product/qualificationConfig"

	def getParams(self, ):
		return self.params



