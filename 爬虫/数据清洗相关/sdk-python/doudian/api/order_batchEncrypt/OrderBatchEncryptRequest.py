# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_batchEncrypt.param.OrderBatchEncryptParam import OrderBatchEncryptParam


class OrderBatchEncryptRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderBatchEncryptParam()

	def getUrlPath(self, ):
		return "/order/batchEncrypt"

	def getParams(self, ):
		return self.params



