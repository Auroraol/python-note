# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.freightTemplate_update.param.FreightTemplateUpdateParam import FreightTemplateUpdateParam


class FreightTemplateUpdateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = FreightTemplateUpdateParam()

	def getUrlPath(self, ):
		return "/freightTemplate/update"

	def getParams(self, ):
		return self.params



