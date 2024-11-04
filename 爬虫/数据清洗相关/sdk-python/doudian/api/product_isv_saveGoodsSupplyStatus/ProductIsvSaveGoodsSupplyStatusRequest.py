# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_isv_saveGoodsSupplyStatus.param.ProductIsvSaveGoodsSupplyStatusParam import ProductIsvSaveGoodsSupplyStatusParam


class ProductIsvSaveGoodsSupplyStatusRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductIsvSaveGoodsSupplyStatusParam()

	def getUrlPath(self, ):
		return "/product/isv/saveGoodsSupplyStatus"

	def getParams(self, ):
		return self.params



