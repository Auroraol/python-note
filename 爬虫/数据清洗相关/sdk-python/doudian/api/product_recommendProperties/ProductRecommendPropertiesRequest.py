# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_recommendProperties.param.ProductRecommendPropertiesParam import ProductRecommendPropertiesParam


class ProductRecommendPropertiesRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductRecommendPropertiesParam()

	def getUrlPath(self, ):
		return "/product/recommendProperties"

	def getParams(self, ):
		return self.params



