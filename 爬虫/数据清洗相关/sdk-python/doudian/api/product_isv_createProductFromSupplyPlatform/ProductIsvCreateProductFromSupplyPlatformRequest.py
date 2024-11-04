# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_isv_createProductFromSupplyPlatform.param.ProductIsvCreateProductFromSupplyPlatformParam import ProductIsvCreateProductFromSupplyPlatformParam


class ProductIsvCreateProductFromSupplyPlatformRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductIsvCreateProductFromSupplyPlatformParam()

	def getUrlPath(self, ):
		return "/product/isv/createProductFromSupplyPlatform"

	def getParams(self, ):
		return self.params



