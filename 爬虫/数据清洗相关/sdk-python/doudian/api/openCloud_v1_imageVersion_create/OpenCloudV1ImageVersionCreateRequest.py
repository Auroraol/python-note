# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.openCloud_v1_imageVersion_create.param.OpenCloudV1ImageVersionCreateParam import OpenCloudV1ImageVersionCreateParam


class OpenCloudV1ImageVersionCreateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OpenCloudV1ImageVersionCreateParam()

	def getUrlPath(self, ):
		return "/openCloud/v1/imageVersion/create"

	def getParams(self, ):
		return self.params



