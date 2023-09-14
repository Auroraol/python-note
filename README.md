"# python-note" 



```python
import requests
import random

def generate_random_number():
    return str(random.randint(1000, 9999))

def login(username, password):
    url = "https://example.com/login"  # 替换成实际的登录URL

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("登录成功！")
    else:
        print("登录失败！")

# 生成随机4位数
random_number = generate_random_number()

# 构造账号
username = "1939002" + random_number

# 替换成你要验证的密码
password = "your_password"

login(username, password)

```

