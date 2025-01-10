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

def is_empty(value):
    if value is False:
        return True
    if value in (0, 0.0, 0j):  # 包含整数、浮点数和复数的零
        return True
    if value == "":
        return True
    if value is None:
        return True
    if isinstance(value, (list, tuple, set)):
        return len(value) == 0
    if isinstance(value, dict):
        return len(value) == 0
    if isinstance(value, float) and (value != value):  # 检查 NaN
        return True
    return False

def is_not_empty(value):
    return not is_empty(value)

def key_exists_in_dict(d, key):
    """ 检查字典中是否存在指定的键 """
    return key in d

def key_value_is_empty(d, key):
    """ 检查字典中指定键的值是否为空 """
    if key_exists_in_dict(d, key):
        return is_empty(d[key])
    return True  # 如果键不存在，返回 True（认为其值为空）

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

# 添加推送
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

def Test4_a():
	res = Test4()
	# print(res[0])
	for id in res:
		Test2(id)

lit1 = []
lit2 = []

def Test5(id):
	class ddpGetShopListRequestParam:
		def __init__(self):
			self.shop_id = None
			self.page_no = None
			self.page_size = None

	class ddpGetShopListRequest(DoudianOpApiRequest):

		def __init__(self):
			DoudianOpApiRequest.__init__(self)
			self.params = ddpGetShopListRequestParam()

		def getUrlPath(self, ):
			return "/openCloud/ddpGetShopList"

		def getParams(self, ):
			return self.params

	request = ddpGetShopListRequest()
	param = request.getParams()
	param.shop_id = id
	response = request.execute()
	if response.code != 10000:
		lit2.append(id)
		print(id)
		# with open('code_ids.txt', 'w', encoding='utf-8') as file:
		# 	file.write(str(id) + '\n')
		# with open('err_plat_shop_ids.txt', 'w', encoding='utf-8') as file:
		# 	file.write(str(id) + '\n')
	if is_empty(response.data["shops"]):
		print(id)
		lit1.append(id)

def Test5_a():
	#
	# 使用更具描述性的变量名
	numbers = [176432027,
187516818,
192414248,
196478136,
196671416,
196800017,
197447724,
407573,
55954254,
69173218,
84969621,
86329983,
984602,]
	# 假设 Test5 是一个已经定义的函数
	for li in numbers:
		Test5(li)

	# 写入 lit1 到 'ids.txt'
	with open('ids.txt', 'a', encoding='utf-8') as file:
		for li in lit1:
			file.write(str(li) + '\n')

	# 写入 lit2 到 'code_ids.txt'
	with open('code_ids.txt', 'a', encoding='utf-8') as file:
		for li in lit2:
			file.write(str(li) + '\n')



	# print(response.code)
	# print(response.msg)
	# print(response.data["shops"])
def Test6():
	class ddpGetShopListRequestParam:
		def __init__(self):
			self.page_no = None
			self.page_size = None

	class ddpGetShopListRequest(DoudianOpApiRequest):

		def __init__(self):
			DoudianOpApiRequest.__init__(self)
			self.params = ddpGetShopListRequestParam()

		def getUrlPath(self, ):
			return "/openCloud/ddpGetShopList"

		def getParams(self, ):
			return self.params

	request = ddpGetShopListRequest()
	param = request.getParams()
	param.page_no = 3
	param.page_size = 20
	# param.shop_id = id
	response = request.execute()
	print(response.code)
	print(response.msg)
	l = []
	for id in response.data["shops"]:
		print(id["shop_id"])
		l.append(id["shop_id"])
	return l

# 添加
def Test6_a():
	res = Test6()
	for id in res:
		# print(id)
		Test2(id)

#添加白名单
def Test7(user_ids):
	import requests
	import json

	url = 'https://script-center.xiaoduoai.com/api/conf-engine/v1/conf_data/set'
	headers = {
		'content-type': 'application/json',
		'user-agent': 'vscode-restclient'
	}

	# 动态构建 plat_user_ids 字段
	plat_user_ids = {}
	for user_id in user_ids:
		plat_user_ids[str(user_id)] = {
			"is_white": True  # 你可以根据需要修改这个字段的值
		}

	data = {
		"conf": {
			"ns": "rs",
			"app": "app",
			"conf_name": "rds_goods"
		},
		"uid": "dy",
		"data": {
			# "default_delay_time": 5,
			# "is_complete": False,
			"plat_user_ids": plat_user_ids
		},
		"is_search": True
	}

	response = requests.post(url, headers=headers, data=json.dumps(data))

	# 打印响应内容
	print(response.status_code)
	print(response.text)

# 添加
def Test7_a():
	res = Test6()
	Test7(res)


if __name__ == '__main__':
	Test7_a()

	# numbers = [176432027,
	# 		   187516818,
	# 		   192414248,
	# 		   196478136,
	# 		   196671416,
	# 		   196800017,
	# 		   197447724,
	# 		   407573,
	# 		   55954254,
	# 		   69173218,
	# 		   84969621,
	# 		   86329983,
	# 		   984602, ]
	# for id in numbers:
	# 	Test2(id)



