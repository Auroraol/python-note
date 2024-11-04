# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_template_revoke.param.SmsTemplateRevokeParam import SmsTemplateRevokeParam


class SmsTemplateRevokeRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsTemplateRevokeParam()

	def getUrlPath(self, ):
		return "/sms/template/revoke"

	def getParams(self, ):
		return self.params



