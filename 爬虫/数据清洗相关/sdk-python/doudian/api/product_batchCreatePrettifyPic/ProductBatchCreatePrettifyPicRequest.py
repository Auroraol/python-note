# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.product_batchCreatePrettifyPic.param.ProductBatchCreatePrettifyPicParam import ProductBatchCreatePrettifyPicParam


class ProductBatchCreatePrettifyPicRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ProductBatchCreatePrettifyPicParam()

	def getUrlPath(self, ):
		return "/product/batchCreatePrettifyPic"

	def getParams(self, ):
		return self.params



