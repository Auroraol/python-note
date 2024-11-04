# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.open_materialToken.param.OpenMaterialTokenParam import OpenMaterialTokenParam


class OpenMaterialTokenRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OpenMaterialTokenParam()

	def getUrlPath(self, ):
		return "/open/materialToken"

	def getParams(self, ):
		return self.params



