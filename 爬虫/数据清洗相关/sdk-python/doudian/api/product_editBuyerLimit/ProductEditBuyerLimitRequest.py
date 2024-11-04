# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_editBuyerLimit.param.ProductEditBuyerLimitParam import ProductEditBuyerLimitParam


class ProductEditBuyerLimitRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductEditBuyerLimitParam()

	def getUrlPath(self, ):
		return "/product/editBuyerLimit"

	def getParams(self, ):
		return self.params



