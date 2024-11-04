# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_getSpuTpl.param.SpuGetSpuTplParam import SpuGetSpuTplParam


class SpuGetSpuTplRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuGetSpuTplParam()

	def getUrlPath(self, ):
		return "/spu/getSpuTpl"

	def getParams(self, ):
		return self.params



