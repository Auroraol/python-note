# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.order_review.param.OrderReviewParam import OrderReviewParam


class OrderReviewRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OrderReviewParam()

	def getUrlPath(self, ):
		return "/order/review"

	def getParams(self, ):
		return self.params



