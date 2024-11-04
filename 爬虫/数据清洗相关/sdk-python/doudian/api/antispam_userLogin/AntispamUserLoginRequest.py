# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.antispam_userLogin.param.AntispamUserLoginParam import AntispamUserLoginParam


class AntispamUserLoginRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = AntispamUserLoginParam()

	def getUrlPath(self, ):
		return "/antispam/userLogin"

	def getParams(self, ):
		return self.params



