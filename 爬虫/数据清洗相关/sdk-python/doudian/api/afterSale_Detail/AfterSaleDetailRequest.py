# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.afterSale_Detail.param.AfterSaleDetailParam import AfterSaleDetailParam


class AfterSaleDetailRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = AfterSaleDetailParam()

	def getUrlPath(self, ):
		return "/afterSale/Detail"

	def getParams(self, ):
		return self.params



