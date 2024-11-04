# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_getVmsApplyTemplateStatus.param.SmsGetVmsApplyTemplateStatusParam import SmsGetVmsApplyTemplateStatusParam


class SmsGetVmsApplyTemplateStatusRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsGetVmsApplyTemplateStatusParam()

	def getUrlPath(self, ):
		return "/sms/getVmsApplyTemplateStatus"

	def getParams(self, ):
		return self.params



