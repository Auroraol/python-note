# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_addOrderRemark.param.OrderAddOrderRemarkParam import OrderAddOrderRemarkParam


class OrderAddOrderRemarkRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderAddOrderRemarkParam()

	def getUrlPath(self, ):
		return "/order/addOrderRemark"

	def getParams(self, ):
		return self.params



