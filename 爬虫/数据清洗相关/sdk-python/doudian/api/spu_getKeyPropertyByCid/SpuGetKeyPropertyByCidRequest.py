# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_getKeyPropertyByCid.param.SpuGetKeyPropertyByCidParam import SpuGetKeyPropertyByCidParam


class SpuGetKeyPropertyByCidRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuGetKeyPropertyByCidParam()

	def getUrlPath(self, ):
		return "/spu/getKeyPropertyByCid"

	def getParams(self, ):
		return self.params



