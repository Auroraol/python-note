# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_batchUploadImg.param.SpuBatchUploadImgParam import SpuBatchUploadImgParam


class SpuBatchUploadImgRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuBatchUploadImgParam()

	def getUrlPath(self, ):
		return "/spu/batchUploadImg"

	def getParams(self, ):
		return self.params



