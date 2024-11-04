# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.antispam_orderSend.param.AntispamOrderSendParam import AntispamOrderSendParam


class AntispamOrderSendRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = AntispamOrderSendParam()

	def getUrlPath(self, ):
		return "/antispam/orderSend"

	def getParams(self, ):
		return self.params



