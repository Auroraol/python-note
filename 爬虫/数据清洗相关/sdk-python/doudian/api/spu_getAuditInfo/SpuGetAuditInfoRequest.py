# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_getAuditInfo.param.SpuGetAuditInfoParam import SpuGetAuditInfoParam


class SpuGetAuditInfoRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuGetAuditInfoParam()

	def getUrlPath(self, ):
		return "/spu/getAuditInfo"

	def getParams(self, ):
		return self.params



