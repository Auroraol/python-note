# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_getSpuInfoBySpuId.param.SpuGetSpuInfoBySpuIdParam import SpuGetSpuInfoBySpuIdParam


class SpuGetSpuInfoBySpuIdRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuGetSpuInfoBySpuIdParam()

	def getUrlPath(self, ):
		return "/spu/getSpuInfoBySpuId"

	def getParams(self, ):
		return self.params



