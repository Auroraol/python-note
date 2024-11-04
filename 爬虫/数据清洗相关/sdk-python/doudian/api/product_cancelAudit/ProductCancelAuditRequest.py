# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_cancelAudit.param.ProductCancelAuditParam import ProductCancelAuditParam


class ProductCancelAuditRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductCancelAuditParam()

	def getUrlPath(self, ):
		return "/product/cancelAudit"

	def getParams(self, ):
		return self.params



