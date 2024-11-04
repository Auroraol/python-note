# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_send.param.SmsSendParam import SmsSendParam


class SmsSendRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSendParam()

	def getUrlPath(self, ):
		return "/sms/send"

	def getParams(self, ):
		return self.params



