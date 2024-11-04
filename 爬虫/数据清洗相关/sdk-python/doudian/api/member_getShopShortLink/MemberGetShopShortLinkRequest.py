# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.member_getShopShortLink.param.MemberGetShopShortLinkParam import MemberGetShopShortLinkParam


class MemberGetShopShortLinkRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = MemberGetShopShortLinkParam()

	def getUrlPath(self, ):
		return "/member/getShopShortLink"

	def getParams(self, ):
		return self.params



