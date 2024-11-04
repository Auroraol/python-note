# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.security_batchReportOrderSecurityEvent.param.SecurityBatchReportOrderSecurityEventParam import SecurityBatchReportOrderSecurityEventParam


class SecurityBatchReportOrderSecurityEventRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SecurityBatchReportOrderSecurityEventParam()

	def getUrlPath(self, ):
		return "/security/batchReportOrderSecurityEvent"

	def getParams(self, ):
		return self.params



