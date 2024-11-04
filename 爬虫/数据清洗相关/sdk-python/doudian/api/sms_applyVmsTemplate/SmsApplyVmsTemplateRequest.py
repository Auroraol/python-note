# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_applyVmsTemplate.param.SmsApplyVmsTemplateParam import SmsApplyVmsTemplateParam


class SmsApplyVmsTemplateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsApplyVmsTemplateParam()

	def getUrlPath(self, ):
		return "/sms/applyVmsTemplate"

	def getParams(self, ):
		return self.params



