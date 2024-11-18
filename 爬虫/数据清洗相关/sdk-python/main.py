# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import xlrd
import json
import openpyxl
from pathlib import Path


def extract_product_ids(file_path):
    # 打开Excel文件
    workbook = xlrd.open_workbook(file_path)
    # 选择第一个sheet
    sheet = workbook.sheet_by_index(0)  # 第几

    # 使用集合来存储商品ID，自动去重
    product_ids = set()

    # 遍历每一行
    for row_idx in range(1, sheet.nrows):
        # 假设商品ID在第一列
        product_id = sheet.cell_value(row_idx, 0)   # 第n,第m列
        if product_id:  # 确保商品ID不是空值
            product_ids.add(product_id)

    # 如果需要返回列表格式
    return list(product_ids)

def save_to_json(data, file_path):
    # 将数据保存为JSON格式
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

def list_files_in_directory(directory_path):
    path = Path(directory_path)
    return [file for file in path.iterdir() if file.is_file()]

if __name__ == '__main__':
    # directory_path = '26'  # 替换为你的目录路径
    # output_path = 'josn'
    #
    # all_files = list_files_in_directory(directory_path)
    #
    # file_paths = all_files  # 文件路径列表
    #
    # for file_path in file_paths:
    #     str_id = file_path.stem  # 获取文件名，不包括扩展名
    #     json_output_path = f'{output_path}/product_ids_{str_id}.json'
    #
    #     unique_product_ids = extract_product_ids(file_path)
    #     save_to_json(unique_product_ids, json_output_path)
    #
    #     print(f"商品ID已保存到 {json_output_path}")

    unique_product_ids = extract_product_ids("29/text2.xls")
    save_to_json(unique_product_ids, "29/json/product_ids_text2.json")
    #
    # print(f"商品ID已保存到")