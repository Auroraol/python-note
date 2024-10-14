# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# from lxml import etree
# import re
# # from fake_useragent import UserAgent
# import requests
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# import shutil
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # 将请求头添加到ChromeOptions
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# import openpyxl
# from datetime import datetime
#
# # 定义计费标准（元/百次）
# billing_rates = {
#     "基础API": [0.018, 0.18],
#     "增值API": [0.05, 0.5],
#     "免费API": [0, 0]
# }
#
#
# def html_parser(html_content):
#     # 解析HTML
#     tree = etree.HTML(html_content)
#
#
#
#     # 找到所有class="auxo-table-tbody"的tbody元素
#     tbody_list = tree.xpath('//tbody[@class="auxo-table-tbody"]')
#
#     # 检查是否有至少两个tbody元素
#     if len(tbody_list) < 2:
#         print("没有找到第二个tbody")
#         return
#
#     # 选择第二个tbody元素
#     tbody = tbody_list[1]
#
#     # 从第二个tr开始遍历
#     all_data = []
#     for i, tr in enumerate(tbody.xpath('.//tr')):
#         if i == 0:
#             # 跳过第一个tr
#             continue
#         # 获取除了第二个td之外的所有td
#         tds = tr.xpath('.//td[position() != 2]')
#         row_data = []
#         for td in tds:
#             # print(etree.tostring(td, method='text', encoding='unicode').strip())
#             # 打印结果:
#             # /order/orderDetail   商品API
#             # 基础API              计费类型
#             # 4, 851, 874         调用次数-云内
#             # 0                   调用次数-云外
#             text = etree.tostring(td, method='text', encoding='unicode').strip()
#             # 如果该单元格内容作为计费类型，并且存在于 billing_rates 中
#             if text in billing_rates:
#                 cloud_in_rate, cloud_out_rate = billing_rates[text]
#                 row_data.append(cloud_in_rate)
#                 row_data.append(cloud_out_rate)
#             else:
#                 # 如果不是计费类型，直接添加到 row_data
#                 row_data.append(text)
#
#         all_data.append(row_data)
#
#     # 保存
#     save_to_excel(all_data)
#
#
# # api名称 API云内单价 API云外单价 API调用次数（云内） API调用测数（云外） 日期（具体到天）
# def save_to_excel(all_data, filename='api_data.xlsx'):
#     """
#     将提取的数据保存到 Excel 文件中。
#
#     :param all_data: 包含要保存到 Excel 的数据的列表
#     :param filename: 保存的 Excel 文件名，默认是 'api_data.xlsx'
#     """
#     # 创建 Excel 工作簿
#     wb = openpyxl.Workbook()
#     ws = wb.active
#
#     # 写入表头
#     ws.append(['API名称', 'API云内单价', 'API云外单价', 'API调用次数（云内）', 'API调用次数（云外）', '日期'])
#
#     # 写入数据
#     for row in all_data:
#         row.append(datetime.now().date())  # 添加当前日期
#         ws.append(row)
#
#     # 保存为 .xlsx 文件
#     wb.save(filename)
#     print(f"数据已成功保存到 {filename}")
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     # 安装驱动
#     # driver_path = EdgeChromiumDriverManager().install()
#     # # print(driver_path)
#     new_path = 'driver/'
#     # shutil.copy(driver_path, new_path)
#
#     # # 设置Selenium WebDriver
#     # firefox_options = Options()
#     # firefox_options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
#
#     url = "https://op.jinritemai.com/console/cost/bill?appId=6891458366200186375&billTimeEnd=1722441599&billTimeStart=1719763200&date=1719936000&pageIndex=1&pageSize=10&tab=daily"
#
#     # 设置WebDriver
#     s = Service(new_path + 'msedgedriver.exe')  # 替换为你的msedgedriver路径
#     driver = webdriver.Edge(service=s)
#
#     try:
#         driver.get(url)
#
#         # 选择邮箱登录
#         email_login_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "email"))
#         )
#         email_login_button.click()
#
#         # 输入邮箱地址
#         email_input = driver.find_element(By.NAME, "email")
#         email_input.send_keys("aifuwushichang@163.com")  # 替换为你的邮箱地址
#
#         # 输入密码
#         password_input = driver.find_element(By.NAME, "password")
#         password_input.send_keys(" XinXiaoduodd@AI1121")  # 替换为你的密码
#
#         # 提交登录信息
#         login_button = driver.find_element(By.CLASS_NAME, "ace-ui-btn-primary")
#         login_button.click()
#
#         time.sleep(15)
#         link = driver.find_element(By.CLASS_NAME, "ecom-open-operation-link")
#         link.click()
#
#         time.sleep(1)
#         # 获取当前页面的HTML内容
#         html_content = driver.page_source
#
#         # 调用解析函数
#         html_parser(html_content)
#         #
#         # # 等待输入框元素加载完成
#         # date_input = WebDriverWait(driver, 20).until(
#         #     EC.presence_of_element_located((By.ID, "date"))
#         # )
#         #
#         # # date_input = driver.find_element(By.ID, "date")
#         #
#         # # # 清除输入框中的内容并输入新的日期
#         # date_input.clear()
#         # date_input.send_keys("2024-01-01")
#         # date_input.submit()
#
#         #
#         # # 等待查询按钮元素加载完成并使其可点击
#         # search_button = WebDriverWait(driver, 10).until(
#         #     EC.element_to_be_clickable((By.XPATH, "//button[@data-module='search']"))
#         # )
#
#         # 点击查询按钮
#         # search_button.click()
#
#
#
#
#     except Exception as e:
#         print(e)
#     finally:
#         pass
#         # 关闭浏览器窗口
#         # driver.quit()
