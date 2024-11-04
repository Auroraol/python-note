# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.open_binaryupload.param.OpenBinaryuploadParam import OpenBinaryuploadParam


class OpenBinaryuploadRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OpenBinaryuploadParam()

	def getUrlPath(self, ):
		return "/open/binaryupload"

	def getParams(self, ):
		return self.params



