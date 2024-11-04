# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_template_apply.param.SmsTemplateApplyParam import SmsTemplateApplyParam


class SmsTemplateApplyRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsTemplateApplyParam()

	def getUrlPath(self, ):
		return "/sms/template/apply"

	def getParams(self, ):
		return self.params



