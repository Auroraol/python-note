# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_publishPreCheck.param.ProductPublishPreCheckParam import ProductPublishPreCheckParam


class ProductPublishPreCheckRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductPublishPreCheckParam()

	def getUrlPath(self, ):
		return "/product/publishPreCheck"

	def getParams(self, ):
		return self.params



