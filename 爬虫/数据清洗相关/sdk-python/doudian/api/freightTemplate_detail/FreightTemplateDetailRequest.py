# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.freightTemplate_detail.param.FreightTemplateDetailParam import FreightTemplateDetailParam


class FreightTemplateDetailRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = FreightTemplateDetailParam()

	def getUrlPath(self, ):
		return "/freightTemplate/detail"

	def getParams(self, ):
		return self.params



