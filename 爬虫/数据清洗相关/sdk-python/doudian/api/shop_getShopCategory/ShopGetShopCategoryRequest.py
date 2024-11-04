# auto generated file
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.api.shop_getShopCategory.param.ShopGetShopCategoryParam import ShopGetShopCategoryParam


class ShopGetShopCategoryRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = ShopGetShopCategoryParam()

	def getUrlPath(self, ):
		return "/shop/getShopCategory"

	def getParams(self, ):
		return self.params



