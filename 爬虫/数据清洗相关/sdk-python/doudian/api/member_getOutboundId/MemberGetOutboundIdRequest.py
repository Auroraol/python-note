# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.member_getOutboundId.param.MemberGetOutboundIdParam import MemberGetOutboundIdParam


class MemberGetOutboundIdRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = MemberGetOutboundIdParam()

	def getUrlPath(self, ):
		return "/member/getOutboundId"

	def getParams(self, ):
		return self.params



