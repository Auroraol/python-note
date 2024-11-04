# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_BatchSearchIndex.param.OrderBatchSearchIndexParam import OrderBatchSearchIndexParam


class OrderBatchSearchIndexRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderBatchSearchIndexParam()

	def getUrlPath(self, ):
		return "/order/BatchSearchIndex"

	def getParams(self, ):
		return self.params



