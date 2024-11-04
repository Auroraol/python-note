# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_deleteVmsTemplate.param.SmsDeleteVmsTemplateParam import SmsDeleteVmsTemplateParam


class SmsDeleteVmsTemplateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsDeleteVmsTemplateParam()

	def getUrlPath(self, ):
		return "/sms/deleteVmsTemplate"

	def getParams(self, ):
		return self.params



