import pandas as pd
from datetime import datetime, timedelta
from douyinApi.utils.is_empty import is_not_empty, key_exists_in_dict
import requests

# # 定义计费标准（元/百次）
billing_rates = {
    2: [0.018, 0.18], # 基础
    3: [0.05, 0.5], #增值
    1: [0, 0] # 免费
}

def generate_timestamps(start_date, end_date):
    """
    生成给定日期范围内的所有日期的时间戳列表。

    参数:
    - start_date (str): 开始日期，格式为 'YYYY-MM-DD'。
    - end_date (str): 结束日期，格式为 'YYYY-MM-DD'。

    返回:
    - list: 包含从开始日期到结束日期（包括结束日期）的所有日期的时间戳列表。
    """
    # 将字符串转换为日期对象
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    # 初始化一个空列表来存储时间戳
    timestamps = []

    # 当前日期初始化为开始日期
    current_date = start

    # 循环直到当前日期大于等于结束日期
    while current_date <= end:
        # 将当前日期添加到列表中
        timestamps.append(int(current_date.timestamp()))
        # 增加一天
        current_date += timedelta(days=1)

    return timestamps


def timestamp_to_date_string(timestamp, date_format='%Y-%m-%d'):
    """
    将时间戳转换为指定格式的日期字符串。

    :param timestamp: 时间戳（秒）
    :param date_format: 目标日期格式字符串，默认为 'YYYY-MM-DD'
    :return: 格式化后的日期字符串
    """
    # 将时间戳转换为 datetime 对象
    dt_object = datetime.fromtimestamp(timestamp)

    # 返回格式化后的日期字符串
    return dt_object.strftime(date_format)


def check_api_call_infos(d):
    """ 检查 apiCallInfos 是否存在且非空 """
    if key_exists_in_dict(d, "data"):
        if key_exists_in_dict(d["data"], "apiCallInfos"):
            return is_not_empty(d["data"]["apiCallInfos"])
    return False


if __name__ == '__main__':
    url = "https://op.jinritemai.com/captain/charge/getApiCallRecord?"

    # 自定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Cookie': "csrf_session_id=25c252bbaaaf6be05d2ebb5fbd96cf74; x-jupiter-uuid=17288744533943404; passport_csrf_token=4f15ec9feb9725794ea85606ecaf174b; passport_csrf_token_default=4f15ec9feb9725794ea85606ecaf174b; s_v_web_id=verify_m28fazxf_6291d2bd_6cf3_772e_a46b_605de816f7a6; odin_tt=d9eb11558aefa5e72ff006f0620377c0af373000670fa0d8cc024ad2ffda2d107857526fca6f7280c2f4686b5341f163e3e002d72bb854f9099dc30b1e95494a; uid_tt_op=c8005ad7edae12e217b4599f128d728d; uid_tt_ss_op=c8005ad7edae12e217b4599f128d728d; sid_tt_op=68fda269a22072e2202266088a2cac6a; sessionid_op=68fda269a22072e2202266088a2cac6a; sessionid_ss_op=68fda269a22072e2202266088a2cac6a; is_staff_user_op=false; store-region=cn-sc; store-region-src=uid; need_choose_shop=0; op_session=a5ec510219b8a61fcf498da0058863c2:7274478cf99a21f4e8d1c8efdf9bcb701631f313a7dd4908f488f1819977dda6; ttwid=1%7C98va07-1WyGGKSM4VLD1f-BbHPFwcX-4CQJox48LzGo%7C1728887380%7Ccf163e028e309d1cd6aaef93ae8e7217950ed442cfeb682d16acc5d2772018f1; ucas_c0_op=CkEKBTEuMC4wEIqIiOD2ya6GZxjBPiC7oIDk44xaKL8-ML704Kjy9PUEQNT0srgGSNSo77oGUIS8kaKkue-xYViHARIUx8zLfJSyNsaxUtLDdOSJUelezW4; ucas_c0_ss_op=CkEKBTEuMC4wEIqIiOD2ya6GZxjBPiC7oIDk44xaKL8-ML704Kjy9PUEQNT0srgGSNSo77oGUIS8kaKkue-xYViHARIUx8zLfJSyNsaxUtLDdOSJUelezW4; sid_guard_op=68fda269a22072e2202266088a2cac6a%7C1728887380%7C5184000%7CFri%2C+13-Dec-2024+06%3A29%3A40+GMT; sid_ucp_v1_op=1.0.0-KDQyNTM3YjllNDBlNTQ1MTFjOTZmZTdhMjAzOTY3MWEwYzQ2MzZmNDAKGQi-9OCo8vT1BBDU9LK4BhiwISAMOAFA6wcaAmxmIiA2OGZkYTI2OWEyMjA3MmUyMjAyMjY2MDg4YTJjYWM2YQ; ssid_ucp_v1_op=1.0.0-KDQyNTM3YjllNDBlNTQ1MTFjOTZmZTdhMjAzOTY3MWEwYzQ2MzZmNDAKGQi-9OCo8vT1BBDU9LK4BhiwISAMOAFA6wcaAmxmIiA2OGZkYTI2OWEyMjA3MmUyMjAyMjY2MDg4YTJjYWM2YQ"
    }
    start_date = '2024-01-01'
    end_date = '2024-10-14'
    timestamps = generate_timestamps(start_date, end_date)

    all_data = []  # 在循环外部初始化 all_data 列表
    for ts in timestamps:
        # print(ts)
        # 请求数据
        data = {"date": ts, "pageNo": 1, "pageSize": 10, "appId": "6891458366200186375"}

        # 发送 POST 请求
        response = requests.post(url, headers=headers, data=data)

        res = response.json()
        if check_api_call_infos(res):
            apiCallInfos = res['data']['apiCallInfos']
            # 或者打印具体的 data 部分
            print(apiCallInfos)
            # all_data = []
            for infos in apiCallInfos:
                row_data = []
                row_data.append(infos['apiName'])
                if infos['apiChargeType'] in billing_rates:
                    cloud_in_rate, cloud_out_rate = billing_rates[infos['apiChargeType']]
                    row_data.append(cloud_in_rate)
                    row_data.append(cloud_out_rate)
                row_data.append(infos['cloudInCallCount'])
                row_data.append(infos['cloudOutCallCount'])
                formatted_date = timestamp_to_date_string(ts)
                row_data.append(formatted_date)
                #
                all_data.append(row_data)
        else:
            print(res)
    # 利用 pandas 创建 DataFrame
    columns = ['API名称', 'API云内单价', 'API云外单价', 'API调用次数（云内）', 'API调用次数（云外）', '日期']
    df = pd.DataFrame(all_data, columns= columns)
    df.to_excel('api_data.xlsx', index=False)  # 索引不写入
