# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_getSpu.param.SpuGetSpuParam import SpuGetSpuParam


class SpuGetSpuRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuGetSpuParam()

	def getUrlPath(self, ):
		return "/spu/getSpu"

	def getParams(self, ):
		return self.params



