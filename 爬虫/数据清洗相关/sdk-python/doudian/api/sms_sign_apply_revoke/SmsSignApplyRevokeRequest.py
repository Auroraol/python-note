# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_sign_apply_revoke.param.SmsSignApplyRevokeParam import SmsSignApplyRevokeParam


class SmsSignApplyRevokeRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSignApplyRevokeParam()

	def getUrlPath(self, ):
		return "/sms/sign/apply/revoke"

	def getParams(self, ):
		return self.params



