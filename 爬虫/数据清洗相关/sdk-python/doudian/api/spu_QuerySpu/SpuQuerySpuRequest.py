# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_QuerySpu.param.SpuQuerySpuParam import SpuQuerySpuParam


class SpuQuerySpuRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuQuerySpuParam()

	def getUrlPath(self, ):
		return "/spu/QuerySpu"

	def getParams(self, ):
		return self.params



