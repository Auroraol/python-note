# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_public_template.param.SmsPublicTemplateParam import SmsPublicTemplateParam


class SmsPublicTemplateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsPublicTemplateParam()

	def getUrlPath(self, ):
		return "/sms/public/template"

	def getParams(self, ):
		return self.params



