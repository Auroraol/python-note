# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_getMCToken.param.OrderGetMCTokenParam import OrderGetMCTokenParam


class OrderGetMCTokenRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderGetMCTokenParam()

	def getUrlPath(self, ):
		return "/order/getMCToken"

	def getParams(self, ):
		return self.params



