pip 是 Python 的包管理工具

<a name="4EgbH"></a>
## 查看pip版本
```bash
pip -V
```

<a name="84c1e457"></a>
## 查看已安装的包
使用以下命令查看已安装的包：
```
pip list
```

<a name="837d8a64"></a>
## 配置管理
pip config 有以下子命令:
```
pip config list
pip config edit
pip config get
pip config set
pip config unset
```

<a name="03070d08"></a>
## 安装依赖包
使用以下命令安装需要的包：
```
pip install <packageName>
```

列举一些常用的包：
```bash
pip install scrapy
pip install pylint
pip install wheel
pip install flask
```

<a name="zJGbx"></a>
## 升级依赖包
使用 `pip install --upgrade xxx` 可以升级依赖包，比如：
```bash
pip install --upgrade flask
```

**升级pip**<br />如果发现新版本的pip，则在执行命令的时候会提示：

```
WARNING: You are using pip version 20.1; however, version 20.2.1 is available.
You should consider upgrading via the 'c:\program files\python\python.exe -m pip install --upgrade pip' command.
```

这时只需要执行以下命令即可升级pip：
```bash
pip install --upgrade pip
```

<a name="026f4d20"></a>
## pip 换源
<a name="47413d66"></a>
### pip国内的一些镜像

- 阿里云 [http://mirrors.aliyun.com/pypi/simple/](http://mirrors.aliyun.com/pypi/simple/)
- 中国科技大学 [https://pypi.mirrors.ustc.edu.cn/simple/](https://pypi.mirrors.ustc.edu.cn/simple/)
- 豆瓣(douban) [http://pypi.douban.com/simple/](http://pypi.douban.com/simple/)
- 清华大学 [https://pypi.tuna.tsinghua.edu.cn/simple/](https://pypi.tuna.tsinghua.edu.cn/simple/)
- 中国科学技术大学 [http://pypi.mirrors.ustc.edu.cn/simple/](http://pypi.mirrors.ustc.edu.cn/simple/)

<a name="a2aeed80"></a>
### 临时换源
```bash
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

<a name="47cb10d2"></a>
### 永久换源
Linux: 在 `~/.pip/pip.conf` 中:
```properties
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

Windows下的配置路径：

- `%HOMEPATH%/pip/pip.ini` 
- `%APPDATA%/pip/pip.ini` 
- `%HOMEPATH%/AppData/Roaming/pip/pip.ini`
```toml
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

也可使用命令修改：
```python
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn
pip config set global.timeout 6000
```
保存位置会直接输出到控制台，比如：
```python
C:\Users\quanzaiyu\AppData\Roaming\pip\pip.ini
```
查看修改后的源：
```python
>>> pip config list

global.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
global.timeout='6000'
global.trusted-host='pypi.tuna.tsinghua.edu.cn'
```

<a name="lbFne"></a>
### 一些国内可用的源
阿里源：
```toml
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

中科大源
```toml
[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple/
[install]
trusted-host = pypi.mirrors.ustc.edu.cn
```

清华大学源
```toml
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host = mirrors.tsinghua.com
```

豆瓣源
```toml
[global]
index-url = http://pypi.douban.com/simple/
[install]
trusted-host = mirrors.douban.com
```

<a name="e1f06255"></a>
## 依赖管理
我们从GitHub下载的项目，通常需要我们自己安装依赖，可以使用以下方式来进行依赖的安装。

`requirements.txt` 用来记录项目所有的依赖包和版本号，只需要一个简单的pip命令就能完成。
```bash
pip freeze >requirements.txt
```

然后就可以用
```bash
pip install -r requirements.txt
```

来一次性安装requirements.txt里面所有的依赖包，非常方便。

<a name="3991c7a9"></a>
## 离线安装第三方包
我们可以下载第三方包(whl文件)进行离线安装, 常用的whl下载地址: [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

安装举例：
```bash
pip install pywin32-224-cp37-cp37m-win_amd64.whl
```

<a name="e0XoW"></a>
## 常见问题
<a name="caYtJ"></a>
### encode_chunked=req.has_header('Transfer-encoding'))
错误详情：
```
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\ProgramData\Anaconda3\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\ProgramData\Anaconda3\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\ProgramData\Anaconda3\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\ProgramData\Anaconda3\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\ProgramData\Anaconda3\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\ProgramData\Anaconda3\lib\http\client.py", line 1392, in connect
    server_hostname=server_hostname)
  File "C:\ProgramData\Anaconda3\lib\ssl.py", line 412, in wrap_socket
    session=session
  File "C:\ProgramData\Anaconda3\lib\ssl.py", line 853, in _create
    self.do_handshake()
  File "C:\ProgramData\Anaconda3\lib\ssl.py", line 1117, in do_handshake
    self._sslobj.do_handshake()
ConnectionResetError: [WinError 10054] Զ▒▒▒▒▒▒ǿ▒ȹر▒▒▒һ▒▒▒▒▒е▒▒▒▒ӡ▒

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "get-source.py", line 26, in <module>
    with urllib.request.urlopen('https://raw.githubusercontent.com/docker-library/official-images/master/library/' + image) as f:
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\ProgramData\Anaconda3\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [WinError 10054] Զ▒▒▒▒▒▒ǿ▒ȹر▒▒▒һ▒▒▒▒▒е▒▒▒▒ӡ▒>
```

解决方案：<br />在py源文件中添加如下代码：
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

<a name="oCiUw"></a>
### pip is configured with locations that require TLS/SSL, however ...
**linux环境下：**<br />首先明确问题出现原因，是因为openssl版本过低或者不存在 so：

1. 查看openssl安装包，发现缺少openssl-devel包
```
[root@localhost ~]# rpm -aq|grep openssl 
openssl-0.9.8e-20.el5 
openssl-0.9.8e-20.el5 
[root@localhost ~]#
```

2. yum安装openssl-devel
```
[root@localhost ~]# yum install openssl-devel -y
```

3. 查看安装结果
```
[root@localhost ~]# rpm -aq|grep openssl 
openssl-0.9.8e-26.el5_9.1 
openssl-0.9.8e-26.el5_9.1 
openssl-devel-0.9.8e-26.el5_9.1 
openssl-devel-0.9.8e-26.el5_9.1
```

4. 重新对python3.6进行编译安装，用一下过程来实现编译安装：
```
cd Python-3.6.4
./configure --with-ssl
make
sudo make install
```

**Windows环境下：**<br />到[https://slproweb.com/products/Win32OpenSSL.html](https://slproweb.com/products/Win32OpenSSL.html)下载winopessl，直接下载第一个MSI安装即可：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596789756830-f715628e-5693-41be-a0d3-4333966c2c07.png#averageHue=%23e9e7dc&height=440&id=rk8Lq&originHeight=440&originWidth=1652&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1652)<br />参考：

- [windows/linux环境python3出现pip is configured with locations that require TLS/SSL, however the..不可用的解决方法](https://blog.csdn.net/wbj_code_life/article/details/97887891)

<a name="RsMOG"></a>
### THESE PACKAGES DO NOT MATCH THE HASHES FROM Pipfile.lock!
使用以下命令升级依赖即可，比如：
```bash
pip install --upgrade numpy
```

<a name="8FVva"></a>
## 参考资料

- [pycharm加速安装python包的速度](https://blog.csdn.net/appleyuchi/article/details/73472513)
- [修改pip的源repository](https://blog.csdn.net/appleyuchi/article/details/73473516)
