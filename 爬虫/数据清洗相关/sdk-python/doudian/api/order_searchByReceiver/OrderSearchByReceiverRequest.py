# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_searchByReceiver.param.OrderSearchByReceiverParam import OrderSearchByReceiverParam


class OrderSearchByReceiverRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderSearchByReceiverParam()

	def getUrlPath(self, ):
		return "/order/searchByReceiver"

	def getParams(self, ):
		return self.params



