# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_editPrice.param.SkuEditPriceParam import SkuEditPriceParam


class SkuEditPriceRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuEditPriceParam()

	def getUrlPath(self, ):
		return "/sku/editPrice"

	def getParams(self, ):
		return self.params



