# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_editCbProduct.param.ProductEditCbProductParam import ProductEditCbProductParam


class ProductEditCbProductRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductEditCbProductParam()

	def getUrlPath(self, ):
		return "/product/editCbProduct"

	def getParams(self, ):
		return self.params



