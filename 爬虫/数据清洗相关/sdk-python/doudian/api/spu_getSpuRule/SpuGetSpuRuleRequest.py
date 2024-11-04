# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_getSpuRule.param.SpuGetSpuRuleParam import SpuGetSpuRuleParam


class SpuGetSpuRuleRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuGetSpuRuleParam()

	def getUrlPath(self, ):
		return "/spu/getSpuRule"

	def getParams(self, ):
		return self.params



