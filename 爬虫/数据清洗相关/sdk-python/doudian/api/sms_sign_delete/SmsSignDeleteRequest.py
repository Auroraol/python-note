# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_sign_delete.param.SmsSignDeleteParam import SmsSignDeleteParam


class SmsSignDeleteRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSignDeleteParam()

	def getUrlPath(self, ):
		return "/sms/sign/delete"

	def getParams(self, ):
		return self.params



