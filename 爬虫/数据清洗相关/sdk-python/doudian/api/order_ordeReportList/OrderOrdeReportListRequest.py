# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_ordeReportList.param.OrderOrdeReportListParam import OrderOrdeReportListParam


class OrderOrdeReportListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderOrdeReportListParam()

	def getUrlPath(self, ):
		return "/order/ordeReportList"

	def getParams(self, ):
		return self.params



