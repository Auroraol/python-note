# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_mergeV2.param.OrderMergeV2Param import OrderMergeV2Param


class OrderMergeV2Request(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderMergeV2Param()

	def getUrlPath(self, ):
		return "/order/mergeV2"

	def getParams(self, ):
		return self.params



