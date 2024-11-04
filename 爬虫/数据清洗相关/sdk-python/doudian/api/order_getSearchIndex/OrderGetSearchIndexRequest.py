# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_getSearchIndex.param.OrderGetSearchIndexParam import OrderGetSearchIndexParam


class OrderGetSearchIndexRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderGetSearchIndexParam()

	def getUrlPath(self, ):
		return "/order/getSearchIndex"

	def getParams(self, ):
		return self.params



