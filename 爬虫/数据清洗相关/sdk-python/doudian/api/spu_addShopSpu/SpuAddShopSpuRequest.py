# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_addShopSpu.param.SpuAddShopSpuParam import SpuAddShopSpuParam


class SpuAddShopSpuRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuAddShopSpuParam()

	def getUrlPath(self, ):
		return "/spu/addShopSpu"

	def getParams(self, ):
		return self.params



