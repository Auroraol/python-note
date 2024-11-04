# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_sign_apply_list.param.SmsSignApplyListParam import SmsSignApplyListParam


class SmsSignApplyListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSignApplyListParam()

	def getUrlPath(self, ):
		return "/sms/sign/apply/list"

	def getParams(self, ):
		return self.params



