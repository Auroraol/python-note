# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_detail.param.ProductDetailParam import ProductDetailParam


class ProductDetailRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductDetailParam()

	def getUrlPath(self, ):
		return "/product/detail"

	def getParams(self, ):
		return self.params



