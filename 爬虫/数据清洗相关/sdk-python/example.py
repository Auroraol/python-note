import pandas as pd
import chardet
import json
from doudian.api.afterSale_Detail.param.AfterSaleDetailParam import AfterSaleDetailParam
from doudian.api.open_getAuthInfo.OpenGetAuthInfoRequest import OpenGetAuthInfoRequest
from doudian.api.order_orderDetail.OrderOrderDetailRequest import OrderOrderDetailRequest
from doudian.core.AccessToken import AccessToken
from doudian.core.AccessTokenBuilder import AccessTokenBuilder
from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.core.DoudianOpConfig import GlobalConfig
from doudian.core.DoudianOpSpiRequest import DoudianOpSpiRequest
# 定义自己的全局变量

GlobalConfig.appKey = "6891458366200186375"  # appKey
GlobalConfig.appSecret = "02f11349-4d31-4f73-9361-6a3e81c2818f"  # appSecret

# 测试
def Test():
	class OpenCloudDdpGetShopListRequestParam:
		def __init__(self):
			self.instance_fuzzy_name = None
			pass

	class OpenCloudDdpGetShopListRequest(DoudianOpApiRequest):

		def __init__(self):
			DoudianOpApiRequest.__init__(self)
			self.params = OpenCloudDdpGetShopListRequestParam()

		def getUrlPath(self, ):
			return "/openCloud/ddpGetShopList"

		def getParams(self, ):
			return self.params

	request = OpenCloudDdpGetShopListRequest()
	param = request.getParams()
	response = request.execute()
	print(response.code)
	print(response.msg)
	print(response.data)

def Test2(id):
	class OpenCloudddpAddShopRequestParam:
		def __init__(self):
			self.shop_id = None
			self.rds_instance_id = None

	class OpenCloudddpAddShopRequest(DoudianOpApiRequest):

		def __init__(self):
			DoudianOpApiRequest.__init__(self)
			self.params = OpenCloudddpAddShopRequestParam()

		def getUrlPath(self, ):
			return "/openCloud/ddpAddShop"

		def getParams(self, ):
			return self.params

	request = OpenCloudddpAddShopRequest()
	param = request.getParams()
	param.shop_id = id
	param.rds_instance_id = "mysql-d8afba2f39b8"
	response = request.execute()
	if response.code != 10000:
		with open('err_plat_shop_ids.txt', 'w', encoding='utf-8') as file:
			file.write(str(id) + '\n')
	# print(response.code)
	# print(response.msg)

def Test3():
	df = pd.read_csv('dy_shop2.csv', header=None, encoding='utf-8')
	plat_user_ids = df[0].dropna()
	return plat_user_ids

def Test4():
	# 读取 filtered_output.csv 文件
	df_filtered = pd.read_csv('unique_to_output11.csv')
	# 检测文件编码
	with open('unique_to_output11.csv', 'rb') as file:
		raw_data = file.read()
		result = chardet.detect(raw_data)
		encoding = result['encoding']

	# 使用检测到的编码读取文件
	plat_user_ids = []
	with open('unique_to_output11.csv', 'r', encoding=encoding) as file:
		for line in file:
			data = json.loads(line.strip())
			plat_user_ids.append(data['plat_user_id'])
	return plat_user_ids


if __name__ == '__main__':
	#
	# res = Test4()
	# # print(res[0])
	# for id in res:
	# 	# Test2(id)


