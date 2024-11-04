# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_qualityTask.param.ProductQualityTaskParam import ProductQualityTaskParam


class ProductQualityTaskRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductQualityTaskParam()

	def getUrlPath(self, ):
		return "/product/qualityTask"

	def getParams(self, ):
		return self.params



