import os

import requests
import json
import urllib.parse

# 读取json文件
# 读取 JSON 文件的函数
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

# 示例调用
file_path = 'C:/PCTMoveData/Desktop/temp/shopid/json/product_name_text.json'
try:
    json_data = read_json_file(file_path)
    print("读取的 JSON 数据:", json_data)
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
except json.JSONDecodeError:
    print("文件内容不是有效的 JSON 格式。")



def fetch_shop_info(encoded_shop_name):
    url = f'http://alihz-prod-pdd-all.pdd.myjjing.com/user_service/internal/shop/info_by_plat_user_id?plat_user_id={encoded_shop_name}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'vscode-restclient'
    }

    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    # 检查响应状态
    if response.status_code == 200:
        data = response.json()

        # 检查 'shop' 是否在响应中
        if 'shop' in data and 'id' in data['shop']:
            shop_id = data['shop']['id']

            # 定义文件名
            filename = 'shop_info.json'

            # 读取现有内容（如果文件存在）
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    existing_data = json.load(file)
                    # 确保 existing_data 是一个列表
                    if not isinstance(existing_data, list):
                        existing_data = []
            else:
                existing_data = []

            # 追加新数据
            existing_data.append(shop_id)  # 直接追加 shop_id

            # 保存到 JSON 文件
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)

        else:
            print("错误: ", encoded_shop_name)

    else:
        print(f"Error: {response.status_code} - {response.text}")

# 使用示例
if __name__ == "__main__":
    json_data = read_json_file(file_path)

    for data in json_data:
        fetch_shop_info(data)

