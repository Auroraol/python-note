# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.freightTemplate_list.param.FreightTemplateListParam import FreightTemplateListParam


class FreightTemplateListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = FreightTemplateListParam()

	def getUrlPath(self, ):
		return "/freightTemplate/list"

	def getParams(self, ):
		return self.params



