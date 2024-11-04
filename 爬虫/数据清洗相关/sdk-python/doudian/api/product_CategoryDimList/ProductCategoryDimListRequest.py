# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_CategoryDimList.param.ProductCategoryDimListParam import ProductCategoryDimListParam


class ProductCategoryDimListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductCategoryDimListParam()

	def getUrlPath(self, ):
		return "/product/CategoryDimList"

	def getParams(self, ):
		return self.params



