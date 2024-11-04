# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_del.param.ProductDelParam import ProductDelParam


class ProductDelRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductDelParam()

	def getUrlPath(self, ):
		return "/product/del"

	def getParams(self, ):
		return self.params



