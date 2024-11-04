# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_GetRecommendCategory.param.ProductGetRecommendCategoryParam import ProductGetRecommendCategoryParam


class ProductGetRecommendCategoryRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductGetRecommendCategoryParam()

	def getUrlPath(self, ):
		return "/product/GetRecommendCategory"

	def getParams(self, ):
		return self.params



