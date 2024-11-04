# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.supplyCenter_cargo_getCategoryPropertyValue.param.SupplyCenterCargoGetCategoryPropertyValueParam import SupplyCenterCargoGetCategoryPropertyValueParam


class SupplyCenterCargoGetCategoryPropertyValueRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SupplyCenterCargoGetCategoryPropertyValueParam()

	def getUrlPath(self, ):
		return "/supplyCenter/cargo/getCategoryPropertyValue"

	def getParams(self, ):
		return self.params



