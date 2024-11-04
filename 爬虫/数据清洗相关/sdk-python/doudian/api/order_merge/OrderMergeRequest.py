# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_merge.param.OrderMergeParam import OrderMergeParam


class OrderMergeRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderMergeParam()

	def getUrlPath(self, ):
		return "/order/merge"

	def getParams(self, ):
		return self.params



