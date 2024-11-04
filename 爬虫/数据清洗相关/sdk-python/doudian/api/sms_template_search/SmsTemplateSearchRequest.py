# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_template_search.param.SmsTemplateSearchParam import SmsTemplateSearchParam


class SmsTemplateSearchRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsTemplateSearchParam()

	def getUrlPath(self, ):
		return "/sms/template/search"

	def getParams(self, ):
		return self.params



