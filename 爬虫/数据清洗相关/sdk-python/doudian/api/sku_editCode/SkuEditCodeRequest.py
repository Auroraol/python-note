# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sku_editCode.param.SkuEditCodeParam import SkuEditCodeParam


class SkuEditCodeRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SkuEditCodeParam()

	def getUrlPath(self, ):
		return "/sku/editCode"

	def getParams(self, ):
		return self.params



