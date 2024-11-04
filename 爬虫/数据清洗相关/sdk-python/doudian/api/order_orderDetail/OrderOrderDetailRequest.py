# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_orderDetail.param.OrderOrderDetailParam import OrderOrderDetailParam


class OrderOrderDetailRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderOrderDetailParam()

	def getUrlPath(self, ):
		return "/order/orderDetail"

	def getParams(self, ):
		return self.params



