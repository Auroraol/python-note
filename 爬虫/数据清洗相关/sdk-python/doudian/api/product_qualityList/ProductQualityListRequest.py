# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_qualityList.param.ProductQualityListParam import ProductQualityListParam


class ProductQualityListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductQualityListParam()

	def getUrlPath(self, ):
		return "/product/qualityList"

	def getParams(self, ):
		return self.params



