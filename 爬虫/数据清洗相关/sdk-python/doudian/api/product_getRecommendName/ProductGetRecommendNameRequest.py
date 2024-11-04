# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_getRecommendName.param.ProductGetRecommendNameParam import ProductGetRecommendNameParam


class ProductGetRecommendNameRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductGetRecommendNameParam()

	def getUrlPath(self, ):
		return "/product/getRecommendName"

	def getParams(self, ):
		return self.params



