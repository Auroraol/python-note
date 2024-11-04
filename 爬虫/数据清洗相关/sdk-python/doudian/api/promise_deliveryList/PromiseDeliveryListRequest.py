# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.promise_deliveryList.param.PromiseDeliveryListParam import PromiseDeliveryListParam


class PromiseDeliveryListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = PromiseDeliveryListParam()

	def getUrlPath(self, ):
		return "/promise/deliveryList"

	def getParams(self, ):
		return self.params



