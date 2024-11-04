# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.afterSale_rejectReasonCodeList.param.AfterSaleRejectReasonCodeListParam import AfterSaleRejectReasonCodeListParam


class AfterSaleRejectReasonCodeListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = AfterSaleRejectReasonCodeListParam()

	def getUrlPath(self, ):
		return "/afterSale/rejectReasonCodeList"

	def getParams(self, ):
		return self.params



