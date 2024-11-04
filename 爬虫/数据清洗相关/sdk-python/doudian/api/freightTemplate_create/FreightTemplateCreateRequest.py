# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.freightTemplate_create.param.FreightTemplateCreateParam import FreightTemplateCreateParam


class FreightTemplateCreateRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = FreightTemplateCreateParam()

	def getUrlPath(self, ):
		return "/freightTemplate/create"

	def getParams(self, ):
		return self.params



