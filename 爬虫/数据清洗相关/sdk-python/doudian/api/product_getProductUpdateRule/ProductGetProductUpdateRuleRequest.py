# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_getProductUpdateRule.param.ProductGetProductUpdateRuleParam import ProductGetProductUpdateRuleParam


class ProductGetProductUpdateRuleRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductGetProductUpdateRuleParam()

	def getUrlPath(self, ):
		return "/product/getProductUpdateRule"

	def getParams(self, ):
		return self.params



