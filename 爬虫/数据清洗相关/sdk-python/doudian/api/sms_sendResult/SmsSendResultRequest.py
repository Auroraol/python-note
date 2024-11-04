# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_sendResult.param.SmsSendResultParam import SmsSendResultParam


class SmsSendResultRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSendResultParam()

	def getUrlPath(self, ):
		return "/sms/sendResult"

	def getParams(self, ):
		return self.params



