# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.spu_queryBookNameByISBN.param.SpuQueryBookNameByISBNParam import SpuQueryBookNameByISBNParam


class SpuQueryBookNameByISBNRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = SpuQueryBookNameByISBNParam()

	def getUrlPath(self, ):
		return "/spu/queryBookNameByISBN"

	def getParams(self, ):
		return self.params



