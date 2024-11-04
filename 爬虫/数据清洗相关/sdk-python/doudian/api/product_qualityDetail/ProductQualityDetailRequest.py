# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_qualityDetail.param.ProductQualityDetailParam import ProductQualityDetailParam


class ProductQualityDetailRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductQualityDetailParam()

	def getUrlPath(self, ):
		return "/product/qualityDetail"

	def getParams(self, ):
		return self.params



