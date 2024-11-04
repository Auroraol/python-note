# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_createSpu.param.SpuCreateSpuParam import SpuCreateSpuParam


class SpuCreateSpuRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuCreateSpuParam()

	def getUrlPath(self, ):
		return "/spu/createSpu"

	def getParams(self, ):
		return self.params



