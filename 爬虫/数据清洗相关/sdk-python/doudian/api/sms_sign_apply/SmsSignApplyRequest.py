# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_sign_apply.param.SmsSignApplyParam import SmsSignApplyParam


class SmsSignApplyRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSignApplyParam()

	def getUrlPath(self, ):
		return "/sms/sign/apply"

	def getParams(self, ):
		return self.params



