# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_sign_search.param.SmsSignSearchParam import SmsSignSearchParam


class SmsSignSearchRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsSignSearchParam()

	def getUrlPath(self, ):
		return "/sms/sign/search"

	def getParams(self, ):
		return self.params



