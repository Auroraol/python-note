# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_batchSend.param.SmsBatchSendParam import SmsBatchSendParam


class SmsBatchSendRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsBatchSendParam()

	def getUrlPath(self, ):
		return "/sms/batchSend"

	def getParams(self, ):
		return self.params



