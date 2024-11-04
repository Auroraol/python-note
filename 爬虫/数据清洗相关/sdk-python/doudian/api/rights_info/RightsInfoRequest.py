# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.rights_info.param.RightsInfoParam import RightsInfoParam


class RightsInfoRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = RightsInfoParam()

	def getUrlPath(self, ):
		return "/rights/info"

	def getParams(self, ):
		return self.params



