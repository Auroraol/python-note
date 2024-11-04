# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.afterSale_List.param.AfterSaleListParam import AfterSaleListParam


class AfterSaleListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = AfterSaleListParam()

	def getUrlPath(self, ):
		return "/afterSale/List"

	def getParams(self, ):
		return self.params



