from doudian.api.afterSale_Detail.param.AfterSaleDetailParam import AfterSaleDetailParam
from doudian.api.open_getAuthInfo.OpenGetAuthInfoRequest import OpenGetAuthInfoRequest
from doudian.core.AccessTokenBuilder import AccessTokenBuilder
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.core.DoudianOpConfig import GlobalConfig
from doudian.core.DoudianOpSpiRequest import DoudianOpSpiRequest
# 定义自己的全局变量

GlobalConfig.appKey = "6891458366200186375"  # appKey
GlobalConfig.appSecret = "02f11349-4d31-4f73-9361-6a3e81c2818f"  # appSecret


# ====API使用示例=====
# 获取token

# 创建Request对象，假设调用的方法名称是: demo.method
# DemoMethodRequest request = DemoMethodRequest()
# 发起API调用
# response = request.execute(token)

class OpenCloudDdpGetShopListRequestParam:
	def __init__(self):
		self.instance_fuzzy_name = None


class OpenCloudDdpGetShopListRequest(DoudianOpApiRequest):

	def __init__(self):
		DoudianOpApiRequest.__init__(self)
		self.params = OpenCloudDdpGetShopListRequestParam()

	def getUrlPath(self, ):
		return "/openCloud/ddpGetShopList"

	def getParams(self, ):
		return self.params



if __name__ == '__main__':
	# 创建Access Token
	# token = AccessTokenBuilder.buildTokenByShopId("9991393")
	# # 构建Open Api请求参数
	# request = OpenGetAuthInfoRequest();
	# request.getParams().page_no = 1
	# request.getParams().page_size = 20
	# request.getParams().shop_id = 123456
	# # 调用Open Api
	# response = request.execute(token)

	# request = OpenCloudDdpAddShopRequest()
	# param = request.getParams()
	# param.shop_id = ""
	# param.rds_instance_id = "mysql-d8afba2f39b8"
	# param.history_days = 7
	# param.interval_calc = 0
	# response = request.execute()
	# request = OpenCloudDdpGetShopListRequest()
	# param = request.getParams()
	# param.instance_fuzzy_name = "mysql-d8afba2f39b8"
	# response = request.execute()
	# print(response.data)
	# 获取token
	# token = AccessTokenBuilder.buildTokenByShopId("9991393")
	# print(token)
	request = OpenCloudDdpGetShopListRequest()
	param = request.getParams()
	# param.shop_id = 536994151673726
	# param.start_modified = 1632835639
	# param.end_modified = 1632835639
	# param.page_no = 1
	# param.page_size = 200
	param.instance_fuzzy_name = "mysql-d8afba2f39b8"
	# param.filter_rules = [1, 2]
	response = request.execute()
	print(response.code)
	print(response.msg)
# ====SPI使用示例=====
# 定义spi处理器
# def bizHandler(context):
#     # 获取服务器传入的paramJson（已经反序列化成object）
#     param = context.getParamJsonObject()
#
#     # 如果处理成功执行下面代码
#     context.wrapSuccess()
#     data = {"xxxx": "xxxx"}
#     context.setResponseData(data)
#
#     # 如果处理失败执行下面的代码
#     context.wrapError(10001, "internal error")


# request = DoudianOpSpiRequest()
# 服务端调用spi接口时的链接参数
# request.init(appKey="7037989963426022956", sign="a68b72f8ccc9c43acc79b2fbbeac392555e042d0c690e5fba1dc9355c50fb548",
#              signV2="xxx", signMethod="hmac-sha256", timestamp="2022-02-10 10:59:24",
#              paramJson="{}")
# 注册一个处理器
# request.registerHandler(bizHandler)
# 执行处理器
# response = request.execute(parseAsJsonString=True)
# 将response返回给服务器
# write return code here
