# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_searchList.param.OrderSearchListParam import OrderSearchListParam


class OrderSearchListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderSearchListParam()

	def getUrlPath(self, ):
		return "/order/searchList"

	def getParams(self, ):
		return self.params



