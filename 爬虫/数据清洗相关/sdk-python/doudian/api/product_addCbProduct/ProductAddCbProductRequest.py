# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_addCbProduct.param.ProductAddCbProductParam import ProductAddCbProductParam


class ProductAddCbProductRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductAddCbProductParam()

	def getUrlPath(self, ):
		return "/product/addCbProduct"

	def getParams(self, ):
		return self.params



