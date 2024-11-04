# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_isv_scanClue.param.ProductIsvScanClueParam import ProductIsvScanClueParam


class ProductIsvScanClueRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductIsvScanClueParam()

	def getUrlPath(self, ):
		return "/product/isv/scanClue"

	def getParams(self, ):
		return self.params



