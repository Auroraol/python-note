# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.sms_template_apply_list.param.SmsTemplateApplyListParam import SmsTemplateApplyListParam


class SmsTemplateApplyListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SmsTemplateApplyListParam()

	def getUrlPath(self, ):
		return "/sms/template/apply/list"

	def getParams(self, ):
		return self.params



