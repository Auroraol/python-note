# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_auditList.param.ProductAuditListParam import ProductAuditListParam


class ProductAuditListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductAuditListParam()

	def getUrlPath(self, ):
		return "/product/auditList"

	def getParams(self, ):
		return self.params



