# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_template_delete.param.SmsTemplateDeleteParam import SmsTemplateDeleteParam


class SmsTemplateDeleteRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsTemplateDeleteParam()

	def getUrlPath(self, ):
		return "/sms/template/delete"

	def getParams(self, ):
		return self.params



