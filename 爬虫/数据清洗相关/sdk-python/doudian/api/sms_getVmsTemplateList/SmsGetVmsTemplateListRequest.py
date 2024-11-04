# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_getVmsTemplateList.param.SmsGetVmsTemplateListParam import SmsGetVmsTemplateListParam


class SmsGetVmsTemplateListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsGetVmsTemplateListParam()

	def getUrlPath(self, ):
		return "/sms/getVmsTemplateList"

	def getParams(self, ):
		return self.params



