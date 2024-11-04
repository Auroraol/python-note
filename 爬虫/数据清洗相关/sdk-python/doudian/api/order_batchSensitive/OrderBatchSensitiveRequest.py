# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_batchSensitive.param.OrderBatchSensitiveParam import OrderBatchSensitiveParam


class OrderBatchSensitiveRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderBatchSensitiveParam()

	def getUrlPath(self, ):
		return "/order/batchSensitive"

	def getParams(self, ):
		return self.params



